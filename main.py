import os
from filters import grayscale as g, blur as b, dilate as d

img_dest = "imgs"

for image in os.listdir(img_dest):
    g.grayscale(image)
    # b.blur(image, 15)
    # d.dilate(image, 15)