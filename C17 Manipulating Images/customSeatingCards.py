#!python3
# customSeatingCards - generates an image file with the guest name and some
# flowery decorations

# 1. Process the 'guests.txt' file
#   open the file
#   read its contents
#   store the contents in a list
# 2. Create a folder for the images
# 3. For each item in a list generate an image
#   create a new image
#   draw a rectangle with black outline on the image
#   prepare the font object
#   count the coordinates so the text will appear in the center
#   draw the name from the list
#   add decorations
#   save the file

import os
from PIL import Image, ImageDraw, ImageFont

# useful, global variables
IMWIDTH = 360
IMHEIGHT = 288
GFOLDER = "Guest_Images"
FNTFOLDER = 'c:\\Windows\Fonts'
guestList = []

# 1. Process the 'guests.txt' file
#   open the file
with open("guests.txt", 'r') as guestFile:
    #   read its contents
    #   store the contents in a list
    guestList = guestFile.readlines()

# 2. Create a folder for the images
os.makedirs(GFOLDER, exist_ok=True)

# 3. For each item in a list generate an image
for guest in guestList:
    #   create a new image
    im = Image.new('RGBA', (IMWIDTH, IMHEIGHT))

    #   draw a rectangle with black outline on the image
    draw = ImageDraw.Draw(im)
    draw.rectangle((0, 0, IMWIDTH-1, IMHEIGHT-1),
                   fill='white', outline='black')

    #   prepare the font object
    curlzFont = ImageFont.truetype(os.path.join(FNTFOLDER, 'Curlz___.TTF'), 50)

    #   count the coordinates so the text will appear in the center
    w, h = draw.textsize(guest, curlzFont)
    wd = (IMWIDTH - w) / 2  # text: 50, width: 100; (100-50)/2=25 ._.t.x._.
    hg = (IMHEIGHT - h) / 2

    #   draw the name from the list
    draw.text((wd, hg), guest, fill='violet', font=curlzFont)

    #   add decorations
    dec = Image.open("img1.png")
    im.paste(dec, (4, 4), dec)
    dec = Image.open("img2.png")
    im.paste(dec, (IMWIDTH-dec.size[0], 4), dec)
    dec = Image.open("img3.png")
    im.paste(dec, (int((IMWIDTH-dec.size[0])/2), IMHEIGHT-dec.size[1]), dec)

    #   save the file
    im.save(os.path.join(GFOLDER, guest.rstrip() + ".png"))
