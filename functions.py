import cv2
import os
from logger import log
from filters import grayscale as g, blur as b, dilate as d

def application_filter(img_dest, new_dest, filters_list):
    for img_file in os.listdir(img_dest):

        img_path = f"{img_dest}/{img_file}"
        # On vérifie que le type de l'image est correct
        if img_path.lower().endswith((".jpg", ".png", ".jpeg")):
            # On essaie de convertir l'image
            try:
                image = cv2.imread(img_path)
                image = filter_number(image, filters_list)
                new_img = f"{new_dest}/{img_file}"
                # On vérifie si le dossier n'existe pas, on le cree
                if not os.path.exists(new_dest):
                    os.makedirs(new_dest)
                cv2.imwrite(new_img, image)

            # Leve une erreur si le nom du fichier n'existe pas
            except cv2.error:
                print("Le fichier est introuvable ou n'existe pas")
                log(f"Tentative echouee, le fichier {img_file} est introuvable ou n'existe pas")
        # Ce n'est pas une image
        else:
            print("Veuillez saisir un fichier de type image (.jpg, .png, .jpeg)")
            log(f"Tentative echouee, le type du fichier ({img_file}) est incorrect")

def filter_number(img, filters_list):
    new_image = img
    for filter in filters_list:
        if filter["name"] == "grayscale":
            new_image = g.grayscale(new_image)
        if filter["name"] == "blur":
            new_image = b.blur(new_image, filter["intensity"])
        if filter["name"] == "dilate":
            new_image = d.dilate(new_image, filter["intensity"])
    return new_image

def next_arg_exist(i, args):
    try:
        if not args[i+1]:
            print("Add arguments please")
            quit()
        else:
            return True
    except IndexError:
        print("Add arguments please")
        quit()