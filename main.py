import os

img_dest = f"imgs"

for element in os.listdir(img_dest):
    if element.lower().endswith((".jpg", ".png", "jpeg")):
        print(f"{element} est une image")
    else:
        print(f"{element} n'est pas une image")