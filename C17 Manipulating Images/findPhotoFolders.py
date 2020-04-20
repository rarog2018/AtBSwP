#! python3
# findoPhotoFolders - program that finds all the folders in which at least 50%
# of the files are photos: have .jpg, .png extensions and > 500 width and height

import os
from PIL import Image

# store the disc letter
disc = input("Type the disc letter: ")
disc += ":\\"

folderCount = 0     # for statistics

for foldername, subfolders, filenames in os.walk(disc):
    # counters
    numPhotoFiles = 0
    numNonPhotoFiles = 0

    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not (filename.endswith('.png') or filename.endswith('.jpg')):
            numNonPhotoFiles += 1
            continue  # skip to next filename

        # store the path to the file
        path = os.path.join(foldername, filename)

        # Try to ppen image file using Pillow.
        try:
            varIm = Image.open(path)
        except (FileNotFoundError, Image.UnidentifiedImageError, Image.DecompressionBombError) as err:
            print(err)
        else:
            # store the size
            width, height = varIm.size

            # Check if width & height are larger than 500.
            if width >= 500 and height >= 500:
                # Image is large enough to be considered a photo.
                numPhotoFiles += 1
            else:
                # Image is too small to be a photo.
                numNonPhotoFiles += 1

    # If at least half of files were photos, and there was at least one file in
    # the folder print the absolute path of the folder.
    fileCount = numPhotoFiles + numNonPhotoFiles
    if numPhotoFiles >= (fileCount / 2) and fileCount > 0:
        print(foldername)
        folderCount += 1

print("Found " + str(folderCount) + " photo folders")
