from PIL import Image
import numpy as np



def return_mode(img,thresh=80):
  m = np.mean(img)
  if m > 80:
    return "Day"
  else:
    return "Night"

img = "image_1.jpeg"
im = Image.open(img).convert('L')
mode = return_mode(im)
print(mode)
