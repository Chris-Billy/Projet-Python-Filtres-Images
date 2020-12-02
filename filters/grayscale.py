import cv2
from logger import log
import os

def grayscale(img):

    img_dest = f"imgs/{img}"
    new_dest = "output/"
    # On vérifie se type de l'image est correct
    if img_dest.endswith((".jpg", ".png")):
        # On essaie de convertir l'image
        try:
            image = cv2.imread(img_dest)
            img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            new_img = f"{new_dest}{img}"
            # On vérifie si le dossier n'existe pas, on le cree
            if not os.path.exists(new_dest):
                os.makedirs(new_dest)
            cv2.imwrite(new_img, img_gray)

            log(f"Gray Scale => Conversion de l'image {img} en Noir et Blanc, enregistre dans {new_img}")
        # Leve une erreur si le nom du fichier n'existe pas
        except cv2.error:
            print("Le fichier est introuvable ou n'existe pas")
            log(f"Gray Scale => Tentative echouee, le fichier est introuvable ou n'existe pas")
    # Ce n'est pas une image
    else:
        print("Veuillez saisir un fichier de type image (.jpg, .png)")
        log(f"Gray Scale => Tentative echouee, le type du fichier est incorrect")

grayscale("tigre.jpg")