import cv2
from logger import log

def blur(img, format, flou):

    image = cv2.imread(f"./../imgs/{img}{format}")
    img_blur = cv2.GaussianBlur(image, (flou, flou), 0)

    new_dest = f"./../output/{img}-copyFlou.jpg"
    cv2.imwrite(new_dest, img_blur)

    log(f"Gossian Blur => Conversion de l'image {img}{format} avec un flou de {flou}, enregistré dans {new_dest}")

# blur("tigre", ".jpg", 15)