import cv2
import numpy as np
from logger import log

def dilate(img, dilate):
    log(f"Dilate => Conversion de l'image, application d'une dilatation de {dilate} sur l'image")
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(img, kernel, iterations = dilate)