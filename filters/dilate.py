import cv2
import numpy as np
from logger import log
import os

def dilate(img, dilate):

    img_dest = f"imgs/{img}"
    new_dest = f"output/"
    # On vérifie se type de l'image est correct
    if img_dest.lower().endswith((".jpg", ".png", ".jpeg")):
        # On essaie de convertir l'image
        try:
            image = cv2.imread(img_dest)
            kernel = np.ones((5, 5), np.uint8)
            img_dilate = cv2.dilate(image, kernel, iterations = dilate)

            new_img = f"{new_dest}{img}"
            # On vérifie si le dossier n'existe pas, on le cree
            if not os.path.exists(new_dest):
                os.makedirs(new_dest)
            cv2.imwrite(new_img, img_dilate)

            log(f"Dilate => Conversion de l'image {img} avec un flou de {dilate}, enregistre dans {new_img}")
        # Leve une erreur si le nom du fichier n'existe pas
        except cv2.error:
            print("Le fichier est introuvable ou n'existe pas")
            log(f"Dilate => Tentative echouee, le fichier est introuvable ou n'existe pas")
    # Ce n'est pas une image
    else:
        print("Veuillez saisir un fichier de type image (.jpg, .png)")
        log(f"Dilate => Tentative echouee, le type du fichier est incorrect")


# dilate("tigre.jpg", 3)