import cv2

def blur(img, flou):
    """
    Appliquer un filtre gaussian blur sur une image
    :param img: l'image sur laquelle appliquer le filtre
    :param flou: l'intensité de la dilatation à appliquer (a int)
    :return: l'image modifié avec le filtre appliqué
    """
    return cv2.GaussianBlur(img, (flou, flou), 0)