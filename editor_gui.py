import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
from enum import Enum
from PIL import Image

class DrawAction(Enum):
    PEN = range(1)


class EditGui:
    def __init__(self, root):
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack()
        self.tools_frame = ttk.LabelFrame(self.main_frame, text="Tools")
        self.tools_frame.pack()

        self.draw_frame = ttk.LabelFrame(self.main_frame, text="Image")
        self.draw_frame.pack()

        self.canvas = tk.Canvas(self.draw_frame, width=800, height=600)
        self.canvas.pack()

        # Save button, temporary
        ttk.Button(self.main_frame, text="Save", command=self.save_image).pack()

        self.draw_action = DrawAction.PEN
        self.is_drawing = False
        self.color1 = "#000000"
        self.pen_size = tk.IntVar(value=1)

        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.release)

        # x/y coordinate of last mouse pos
        self.last_mouse_pos = type("MousePos", (), {"x": 0, "y": 0})()

        self.create_tools_gui()

    def save_image(self):
        self.canvas.postscript(file="temp.eps")
        img = Image.open("temp.eps")
        img.save("test.png", "png")

    def create_tools_gui(self):
        self.color_frame = ttk.LabelFrame(self.tools_frame, text="Color1")
        self.color_frame.pack(side=tk.LEFT)
        self.color_button = tk.Button(self.color_frame, command=self.set_color1, bg=self.color1)
        self.color_button.pack()

        self.pen_size_frame = ttk.LabelFrame(self.tools_frame, text="Pen Size")
        self.pen_size_frame.pack(side=tk.LEFT)

        tk.Scale(self.pen_size_frame, orient="horizontal", showvalue=0, from_=1, to=25, variable=self.pen_size).pack(side=tk.LEFT)
        ttk.Label(self.pen_size_frame, textvariable=self.pen_size).pack(side=tk.LEFT)

    def set_color1(self):
        color_tup, hex_color = colorchooser.askcolor(color=self.color1)

        if hex_color:
            self.color1 = hex_color
            self.color_button.configure(bg=self.color1)

    def draw(self, event):

        if self.draw_action == DrawAction.PEN:
            if not self.is_drawing:
                self.last_mouse_pos.x, self.last_mouse_pos.y = event.x, event.y
                self.is_drawing = True
            # self.canvas.create_oval(event.x, event.y, event.x, event.y, fill="#FF0000", outline="#FF0000")
            self.canvas.create_line(self.last_mouse_pos.x, self.last_mouse_pos.y, event.x, event.y, width=self.pen_size.get(),
                                    joinstyle="round", capstyle="round", fill=self.color1)
            self.last_mouse_pos.x = event.x
            self.last_mouse_pos.y = event.y

    def release(self, event):
        self.is_drawing = False

