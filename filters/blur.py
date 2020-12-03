import cv2

def blur(img, flou):

    return cv2.GaussianBlur(img, (flou, flou), 0)