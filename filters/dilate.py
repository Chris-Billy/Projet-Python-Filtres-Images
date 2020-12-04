import cv2
import numpy as np

def dilate(img, dilate):
    """
    Appliquer un filtre dilate sur une image
    :param img: l'image sur laquelle appliquer le filtre
    :param dilate: l'intensité de la dilatation à appliquer (a int)
    :return: l'image modifié avec le filtre appliqué
    """
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(img, kernel, iterations = dilate)