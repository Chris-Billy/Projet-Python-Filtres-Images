import cv2
import numpy as np

def dilate(img, dilate):

    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(img, kernel, iterations = dilate)