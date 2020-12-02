import os
import cv2
from logger import log
from filters import grayscale as g, blur as b, dilate as d
import sys

args = sys.argv
print(args)

img_dest = args[1]

for img_file in os.listdir(img_dest):
    # g.grayscale(image)
    # b.blur(image, 15)
    # d.dilate(image, 15)
    img_path = f"{img_dest}/{img_file}"
    new_dest = f"output/"
    # On vérifie se type de l'image est correct
    if img_path.lower().endswith((".jpg", ".png", ".jpeg")):
        # On essaie de convertir l'image
        try:
            image = cv2.imread(img_path)
            image = g.grayscale(image)
            new_img = f"{new_dest}{img_file}"
            # On vérifie si le dossier n'existe pas, on le cree
            if not os.path.exists(new_dest):
                os.makedirs(new_dest)
            cv2.imwrite(new_img, image)

            # Leve une erreur si le nom du fichier n'existe pas
        except cv2.error:
            print("Le fichier est introuvable ou n'existe pas")
            log(f"Dilate => Tentative echouee, le fichier est introuvable ou n'existe pas")
            # Ce n'est pas une image
    else:
        print("Veuillez saisir un fichier de type image (.jpg, .png)")
        log(f"Dilate => Tentative echouee, le type du fichier est incorrect")
