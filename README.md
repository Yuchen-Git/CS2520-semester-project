
# Tkinter Image Editor

## Overview
This project provides a versatile image editing tool that supports both command-line and graphical user interfaces. It allows users to perform basic image manipulations such as flipping, rotating, and drawing on images.

## Requirements
- Python 3.x
- Pillow (PIL Fork)
- Tkinter (included with standard Python installation on Windows)

## Installation
To set up the image editor, you need to install the required Python libraries. You can install Pillow using pip:

```bash
pip install Pillow
```

## Quick Start
Get started with the Tkinter Image Editor quickly using these commands:

**For GUI:**
```bash
python main.py
```

**For CLI (Example: Rotate an image right):**
```bash
python main.py -i path/to/your/image.jpg -o path/to/save/edited_image.jpg -rotr
```

## Usage

### CLI Mode
To use the command-line interface, run the following command:

```bash
python main.py -i <input_path> -o <output_path> [options]
```

**Options:**
- `-nogui`: Runs the tool in CLI mode without launching the GUI.
- `-fliph`: Flips the image horizontally.
- `-flipv`: Flips the image vertically.
- `-rotr`: Rotates the image to the right (270 degrees).
- `-rotl`: Rotates the image to the left (90 degrees).

### GUI Mode
If no `-nogui` flag is specified, the GUI mode is activated by default. You can start the GUI without any command-line arguments or specify an input image to open initially:

```bash
python main.py
```

## Features
- **CLI and GUI Modes**: Choose between command-line or graphical interfaces depending on your needs.
- **Image Manipulations**: Supports flipping, rotating, and basic drawing on images.
- **Extensible**: The project is structured to be easily extendable for additional features.

## Examples
**Rotate an Image:**
```bash
python main.py -i input.jpg -o output.jpg -rotl
```
This command rotates the image located at `input.jpg` 90 degrees to the left and saves the result to `output.jpg`.

## Troubleshooting
If you encounter any issues with installation or running the editor, ensure you have the latest version of Python and Pillow installed. Check if Tkinter is properly installed by running `python -m tkinter` from your command line.

## License
This project is open-source and available under the MIT License.
