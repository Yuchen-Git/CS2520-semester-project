import ttkbootstrap as ttk
import tkinter
from tkinter import filedialog
from tkinter.messagebox import showerror, askyesno
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter, ImageGrab
import pyqrcode
import cv2

# Process command line arguments
import cli_image
# Project GUI
from editor_gui import EditGui

if __name__ == '__main__':
    if not cli_image.NO_GUI:
        input_image = cli_image.IMAGE  # If none, no input specified
        # Launch gui here, open input_image if available
        root = tkinter.Tk()
        root.title("Tkinter Image Editor")
        gui = EditGui(root)
        root.mainloop()