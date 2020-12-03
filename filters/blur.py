import cv2
from logger import log

def blur(img, flou):

    log(f"Gossian Blur => Conversion de l'image, application d'un flou de {flou} sur l'image")
    return cv2.GaussianBlur(img, (flou, flou), 0)