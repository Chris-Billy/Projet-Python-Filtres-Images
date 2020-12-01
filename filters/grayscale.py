import cv2
from logger import log

def grayscale(img, format):

    image = cv2.imread(f"./../imgs/{img}{format}")
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    new_dest = f"./../output/{img}-copyNB.jpg"
    cv2.imwrite(new_dest, img_gray)

    log(f"Gray Scale => Conversion de l'image {img}{format} en Noir et Blanc, enregistré dans {new_dest}")

grayscale("tigre", ".jpg")