import cv2
from logger import log
import os

def blur(img, format, flou):

    img_dest = f"imgs/{img}{format}"
    new_dest = "output/"
    # On vérifie se type de l'image est correct
    if img_dest.endswith((".jpg", ".png")):
        # On vérifie que le flou soit positif ET impaire
        if flou < 0 or flou % 2 == 0:
            print("La valeur du flou doit etre positive ET impaire")
            log(f"Gossian Blur => Tentative echouee, la valeur du flou est incorrect")
            # On essaie de convertir l'image
        else:
            try:
                image = cv2.imread(img_dest)
                img_blur = cv2.GaussianBlur(image, (flou, flou), 0)

                new_img = f"{new_dest}{img}-copyFlou{format}"
                # On vérifie si le dossier n'existe pas, on le cree
                if not os.path.exists(new_dest):
                    os.makedirs(new_dest)
                cv2.imwrite(new_img, img_blur)

                log(f"Gossian Blur => Conversion de l'image {img}{format} avec un flou de {flou}, enregistre dans {new_img}")
                # Leve une erreur si le nom du fichier n'existe pas
            except cv2.error:
                print("Le fichier est introuvable ou n'existe pas")
                log(f"Gossian Blur => Tentative echouee, le fichier est introuvable ou n'existe pas")
    # Ce n'est pas une image
    else:
        print("Veuillez saisir un fichier de type image (.jpg, .png)")
        log(f"Gossian Blur => Tentative echouee, le type du fichier est incorrect")

blur("panda", ".jpg", 15)