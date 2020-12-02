import cv2
from logger import log

def grayscale(img, format):

    try:
        image = cv2.imread(f"imgs/{img}{format}")
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        new_dest = f"output/{img}-copyNB{format}"
        cv2.imwrite(new_dest, img_gray)

        log(f"Gray Scale => Conversion de l'image {img}{format} en Noir et Blanc, enregistre dans {new_dest}")

    except cv2.error:
        print("Le fichier est introuvable ou n'existe pas")
        log(f"Gray Scale => Tentative echouee, le fichier est introuvable ou n'existe pas")

grayscale("tigre", ".jpg")