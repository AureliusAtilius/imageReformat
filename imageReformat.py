#!/usr/bin/env python3
import os
from PIL import Image
from pathlib import Path

for file in os.listdir('.'):
        
        im = Image.open(file)
        filename, fileExt = os.path.splitext(file)

        rotated_im = im.rotate(270)
        resized_im = rotated_im.resize((128,128))
        #cannot convert from TIFF to JPEG, must convert to RGB first
        resized_im = resized_im.convert("RGB")
        
        resized_im.save("/opt/icons/"+filename, format= "JPEG")
