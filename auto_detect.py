from PIL import Image
import numpy as np



def return_mode(img,thresh=80):
  m = np.mean(im)
  if m > 80:
    return "Day"
  else:
    return "Night"

img = "image_1.jpeg"
im = Image.open(img) 
mode = return_mode(img)
print(mode)
