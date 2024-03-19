import ttkbootstrap as ttk
from tkinter import filedialog
from tkinter.messagebox import showerror, askyesno
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter, ImageGrab
import pyqrcode
import cv2

# Process command line arguments
import cli_image

if __name__ == '__main__':
    if not cli_image.NO_GUI:
        input_image = cli_image.IMAGE  # If none, no input specified
        # Launch gui here, open input_image if available
