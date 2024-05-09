import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser, filedialog
from enum import Enum, auto
from PIL import Image, ImageTk
import os


class DrawAction(Enum):
    PEN = auto()
    OVAL = auto()
    FILLED_OVAL = auto()
    RECTANGLE = auto()
    FILLED_RECTANGLE = auto()
    LINE = auto()


class EditGui:

    def __init__(self, root, load_image=None):
        """
        Initialize the EditGui class with the root Tkinter object
        :param root:
        """
        self.IMAGE_SIZE = (800, 600)
        self.root = root
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack()
        self.tools_frame = ttk.LabelFrame(self.main_frame, text="Tools")
        self.tools_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.draw_frame = ttk.LabelFrame(self.main_frame, text="Image")
        self.draw_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.draw_frame, width=self.IMAGE_SIZE[0], height=self.IMAGE_SIZE[1], background="#FFFFFF")
        self.canvas.pack()

        self.draw_action = DrawAction.PEN
        self.is_drawing = False
        self.color1 = tk.StringVar(value="#000000")
        self.color2 = tk.StringVar(value="#FFFFFF")
        self.pen_size = tk.IntVar(value=1)

        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.release)

        # x/y coordinate of last mouse pos
        self.last_mouse_pos = type("MousePos", (), {"x": 0, "y": 0})()

        self.create_tools_gui()
        self.create_menu()

        if load_image:
            load_image = load_image.resize(self.IMAGE_SIZE)
            self.canvas.image = ImageTk.PhotoImage(load_image)
            self.canvas.create_image(0, 0, image=self.canvas.image, anchor="nw")

    def create_menu(self):
        """
        Create the menu for the GUI
        :return:
        """
        menu = tk.Menu(self.root)
        file_menu = tk.Menu(menu, tearoff=False)
        file_menu.add_command(label="Open", command=self.open_image)
        file_menu.add_command(label="New", command=self.new_image)
        file_menu.add_command(label="Save", command=self.save_image)
        file_menu.add_command(label="Exit", command=exit)
        menu.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menu)

    def save_image(self):
        """
        Save the image as a PNG file
        :return:
        """
        filename = filedialog.asksaveasfilename(title="Save Image", filetypes=[("png", "png")])
        if filename:
            self.root.update()
            self.canvas.postscript(file="temp.eps", x=0, y=0, height=self.canvas.winfo_reqheight(), width=self.canvas.winfo_reqwidth())
            img = Image.open("temp.eps")
            img.save(filename+".png")
            img.close()
            os.remove("temp.eps")

    def new_image(self):
        """
        Clear the canvas
        :return:
        """
        self.canvas.delete("all")

    def open_image(self):
        """
        Open an image and display it on the canvas
        :return:
        """
        filename = filedialog.askopenfilename(title="Open Image", filetypes=[("png", ".png"), ("jpg", ".jpg"), ("jpeg", ".jpeg"), ("All Files", ".*")])
        if filename:
            img = Image.open(filename)
            img = img.resize(self.IMAGE_SIZE)
            self.canvas.image = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, image=self.canvas.image, anchor="nw")

    def create_tools_gui(self):
        """
        Create the tools GUI
        :return:
        """
        # Tool Choice
        self.tool_choice_frame = ttk.LabelFrame(self.tools_frame, text="Choose Tool")
        self.tool_choice_frame.pack(pady=5, padx=5, fill=tk.X, expand=True)

        self.tool_choice = ttk.Combobox(self.tool_choice_frame)
        self.tool_choice.pack()
        self.tool_choice['values'] = [c for c in DrawAction.__members__]
        self.tool_choice.current(0)
        self.tool_choice.bind("<<ComboboxSelected>>", self.update_draw_action)

        # Color1 picker
        self.color_frame = ttk.LabelFrame(self.tools_frame, text="Color")
        self.color_frame.pack(pady=5, padx=5, fill=tk.X, expand=True)

        self.color_button = tk.Button(self.color_frame, command=self.ask_set_color1, bg=self.color1.get(), width=20)
        self.color_button.pack()
        update_color_button = lambda *a: self.color_button.configure(bg=self.color1.get())
        self.color1.trace_add("write", update_color_button)

        # Color2 picker
        self.color_frame2 = ttk.LabelFrame(self.tools_frame, text="Color2")
        self.color_frame2.pack(pady=5, padx=5, fill=tk.X, expand=True)

        self.color_button2 = tk.Button(self.color_frame2, command=self.ask_set_color2, bg=self.color2.get(), width=20)
        self.color_button2.pack()
        update_color_button2 = lambda *a: self.color_button2.configure(bg=self.color2.get())
        self.color2.trace_add("write", update_color_button2)

        # Pen tools widgets
        self.pen_size_frame = ttk.LabelFrame(self.tools_frame, text="Pen Size")
        self.pen_size_frame.pack(pady=5, padx=5, fill=tk.X, expand=True)

        # Pen Size Slider
        tk.Scale(self.pen_size_frame, orient="horizontal", showvalue=False, from_=1, to=25, variable=self.pen_size).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Label(self.pen_size_frame, textvariable=self.pen_size, width=2).pack(side=tk.LEFT)

        # Pen Size/Color Demo view
        pen_size_demo = tk.Canvas(self.pen_size_frame, width=32, height=32)
        pen_size_demo.pack(side=tk.LEFT)
        pen_size_demo.create_line(16, 16, 16, 16, width=self.pen_size.get(), joinstyle="round",
                                  capstyle="round", fill=self.color1.get())

        def pen_size_update(*a):
            """
            Update the pen size demo
            :param a:
            :return:
            """
            pen_size_demo.delete("all")
            mid = pen_size_demo.winfo_width() // 2
            pen_size_demo.create_line(mid, mid, mid, mid, width=self.pen_size.get(), joinstyle="round",
                                      capstyle="round", fill=self.color1.get())

        self.pen_size.trace_add("write", pen_size_update)
        self.color1.trace_add("write", pen_size_update)

    def update_draw_action(self, event):
        """
        Update the draw action based on the event
        :param event: Event object
        """
        self.draw_action = DrawAction[self.tool_choice.get()]

    def ask_set_color1(self):
        """
        Ask the user to set the first color
        :return: None
        """
        color_tup, hex_color = colorchooser.askcolor(color=self.color1.get())
        if hex_color:
            self.color1.set(hex_color)

    def ask_set_color2(self):
        """
        Ask the user to set the second color
        :return: None
        """
        color_tup, hex_color = colorchooser.askcolor(color=self.color2.get())
        if hex_color:
            self.color2.set(hex_color)

    def draw(self, event):
        """
        Draw on the canvas
        :param event:
        :return:
        """
        match self.draw_action:
            case DrawAction.PEN:
                if not self.is_drawing:
                    self.last_mouse_pos.x, self.last_mouse_pos.y = event.x, event.y
                    self.is_drawing = True
                self.canvas.create_line(self.last_mouse_pos.x, self.last_mouse_pos.y, event.x, event.y, width=self.pen_size.get(),
                                        joinstyle="round", capstyle="round", fill=self.color1.get())
                self.last_mouse_pos.x = event.x
                self.last_mouse_pos.y = event.y

            case _:
                if not self.is_drawing:
                    self.last_mouse_pos.x, self.last_mouse_pos.y = event.x, event.y
                    self.is_drawing = True
                else:
                    # If continuing to draw, erase last oval
                    self.canvas.delete(self.canvas.find_all()[-1])

                match self.draw_action:
                    case DrawAction.OVAL:
                        self.canvas.create_oval(self.last_mouse_pos.x, self.last_mouse_pos.y, event.x, event.y, width=self.pen_size.get(), outline=self.color1.get())
                    case DrawAction.FILLED_OVAL:
                        self.canvas.create_oval(self.last_mouse_pos.x, self.last_mouse_pos.y, event.x, event.y,
                                                width=self.pen_size.get(), outline=self.color1.get(), fill=self.color2.get())
                    case DrawAction.RECTANGLE:
                        self.canvas.create_rectangle(self.last_mouse_pos.x, self.last_mouse_pos.y, event.x, event.y, width=self.pen_size.get(), outline=self.color1.get())
                    case DrawAction.FILLED_RECTANGLE:
                        self.canvas.create_rectangle(self.last_mouse_pos.x, self.last_mouse_pos.y, event.x, event.y,
                                                     width=self.pen_size.get(), outline=self.color1.get(), fill=self.color2.get())
                    case DrawAction.LINE:
                        self.canvas.create_line(self.last_mouse_pos.x, self.last_mouse_pos.y, event.x, event.y,
                                                width=self.pen_size.get(),
                                                joinstyle="round", capstyle="round", fill=self.color1.get())

    def release(self, event):
        """
        Release the mouse button
        :param event:
        :return:
        """
        self.is_drawing = False
