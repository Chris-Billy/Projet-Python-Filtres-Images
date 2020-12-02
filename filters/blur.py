import cv2
from logger import log

def blur(img, format, flou):

    try:
        image = cv2.imread(f"imgs/{img}{format}")
        img_blur = cv2.GaussianBlur(image, (flou, flou), 0)

        new_dest = f"output/{img}-copyFlou{format}"
        cv2.imwrite(new_dest, img_blur)

        log(f"Gossian Blur => Conversion de l'image {img}{format} avec un flou de {flou}, enregistre dans {new_dest}")

    except cv2.error:
        print("Le fichier est introuvable ou n'existe pas")
        log(f"Gossian Blur => Tentative echouee, le fichier est introuvable ou n'existe pas")

blur("tigre", ".jpg", 15)