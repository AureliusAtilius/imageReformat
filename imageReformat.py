#! /usr/bin/env/python3 
import os
from PIL import Image
from pathlib import Path


# Move through each file in a folder
for file in os.listdir('.'):
        if file.endwith('.tiff'):

                # Open Image
                im = Image.open(file)
                # Rotate image 
                im.Rotate(90)
                # Resize image 
                im.Resize((128,128))
                # Save image as .jpg
                im.Save(Path('/opt/icons/')/Path(file), format='.jpg')



