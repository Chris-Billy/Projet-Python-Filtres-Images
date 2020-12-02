import cv2
from logger import log

def blur(img, flou):

    # TODO détecter dès le début si le blur a une mauvaise valeur
    # On vérifie que le flou soit positif ET impaire
    if flou < 0 or flou % 2 == 0:
        print("La valeur du flou doit etre positive ET impaire")
        log(f"Gossian Blur => Tentative echouee, la valeur du flou est incorrect")
    else:
        log(f"Gossian Blur => Conversion de l'image, application d'un flou de {flou} sur l'image")
        return cv2.GaussianBlur(img, (flou, flou), 0)