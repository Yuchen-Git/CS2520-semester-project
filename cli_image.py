import argparse
from PIL import Image as PImage


parser = argparse.ArgumentParser(description="CLI control")
# Avoid gui
parser.add_argument("-nogui", "-ng", action="store_true")
# Input file path
parser.add_argument("-i")
# Output file path
parser.add_argument("-o")
# Flip horizontally
parser.add_argument("-fliph", action="store_true")
# Flip Vertically
parser.add_argument("-flipv", action="store_true")
# Rotate right
parser.add_argument("-rotr", action="store_true")
# Rotate left
parser.add_argument("-rotl", action="store_true")
args = parser.parse_args()

# No Default image
IMAGE = None
NO_GUI = args.nogui

# Only take action if input file exists
if args.i:
    # Open image
    IMAGE = PImage.open(args.i)
    if IMAGE:
        IMAGE = IMAGE.transpose(PImage.TRANSPOSE)
        if args.fliph:
            IMAGE = IMAGE.transpose(PImage.FLIP_LEFT_RIGHT)
        if args.flipv:
            IMAGE = IMAGE.transpose(PImage.FLIP_TOP_BOTTOM)
        if args.rotl:
            IMAGE = IMAGE.transpose(PImage.ROTATE_90)
        if args.rotr:
            IMAGE = IMAGE.transpose(PImage.ROTATE_270)

        # Save output
        if args.o:
            IMAGE.save(args.o)
