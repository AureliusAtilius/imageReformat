#! bin/env/python3 
import os, sys
from PIL import Image
from pathlib import Path


# Move through each file in a folder named in the first command line argument
for file in Path(sys.argv[1]).glob("*.tiff"):

# Open Image
        im = Image(file)
# Rotate image 
        im.Rotate(90)
# Resize image 
        im.Resize((128,128))
# Save image as .jpg
        im.Save(Path('/opt/icons/')/Path(file), format='.jpg')
