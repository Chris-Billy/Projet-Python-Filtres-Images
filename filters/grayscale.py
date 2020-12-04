import cv2

def grayscale(img):
    """
    Appliquer un filtre grayscale sur une image
    :param img: l'image sur laquelle appliquer le filtre
    :return: l'image modifié avec le filtre appliqué
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)