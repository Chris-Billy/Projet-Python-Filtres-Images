import cv2
from logger import log

def grayscale(img):

    log("Gray Scale => Conversion de l'image en noir et blanc")
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)