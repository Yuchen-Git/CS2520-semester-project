import tkinter

# Process command line arguments
import cli_image
# Project GUI
from editor_gui import EditGui
# Project CLI
if __name__ == '__main__':
    # If no gui is specified, run the command line interface
    if not cli_image.NO_GUI:
        input_image = cli_image.IMAGE  # If none, no input specified
        # Launch gui here, open input_image if available
        root = tkinter.Tk()
        root.title("Tkinter Image Editor")
        gui = EditGui(root)
        root.mainloop()