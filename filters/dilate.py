import cv2
import numpy as np
from logger import log

def dilate(img, format, dilate):

    try:
        image = cv2.imread(f"imgs/{img}{format}")
        kernel = np.ones((5, 5), np.uint8)
        img_dilate = cv2.dilate(image, kernel, iterations = dilate)

        new_dest = f"output/{img}-copyDilate{format}"
        cv2.imwrite(new_dest, img_dilate)

        log(f"Dilate => Conversion de l'image {img}{format} avec un flou de {dilate}, enregistre dans {new_dest}")

    except cv2.error:
        print("Le fichier est introuvable ou n'existe pas")
        log(f"Dilate => Tentative echouee, le fichier est introuvable ou n'existe pas")

dilate("tigre", ".jpg", 3)