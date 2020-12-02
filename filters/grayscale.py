import cv2
from logger import log
import os

def grayscale(img):
    log(f"Dilate => Conversion de l'image avec un gris")
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)