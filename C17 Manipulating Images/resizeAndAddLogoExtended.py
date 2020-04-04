#! python3
# resizeAndAddLogoExtended.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'
# added global variable with extensions
EXTNSNS = (".png", ".jpg", ".gif", ".bmp")

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.lower().endswith(tuple(EXTNSNS))) \
            or filename == LOGO_FILENAME:   # added lower() to ignore case
        continue    # skip non-image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size

    # added statement to check if image should be processed
    if width < logoWidth * 2 or height < logoHeight * 2:
        print("Skipping %s..." % (filename))
        continue    # skip images that are too small

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        print("Resizing %s..." % (filename))
        im = im.resize((width, height))

    # Add the logo.
    print("Adding logo to %s..." % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes.
    im.save(os.path.join('withLogo', filename))
