import cv2

image = "./../imgs/tigre.txt"

if image.endswith((".jpg", ".png")):
    print(f"c'est une image")
else:
    print("Le format du fichier n'est pas bon")