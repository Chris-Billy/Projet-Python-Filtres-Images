import cv2
import numpy as np
from logger import log

def dilate(img, format, dilate):

    image = cv2.imread(f"./../imgs/{img}{format}")
    kernel = np.ones((5, 5), np.uint8)
    img_dilate = cv2.dilate(image, kernel, iterations = dilate)

    new_dest = f"./../output/{img}-copyDilate.jpg"
    cv2.imwrite(new_dest, img_dilate)

    log(f"Dilate => Conversion de l'image {img}{format} avec un flou de {dilate}, enregistré dans {new_dest}")

# dilate("tigre", ".jpg", 3)