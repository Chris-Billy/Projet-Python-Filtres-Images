import cv2
import os
from logger import log
from filters import grayscale as g, blur as b, dilate as d

def application_filter(img_dest, new_dest, filters_list, log_file):
    for img_file in os.listdir(img_dest):

        img_path = f"{img_dest}/{img_file}"
        # On vérifie que le type de l'image est correct
        if img_path.lower().endswith((".jpg", ".png", ".jpeg")):
            # On essaie de convertir l'image
            try:
                image = cv2.imread(img_path)
                image = filter_number(image, filters_list, log_file)
                new_img = f"{new_dest}/{img_file}"
                # On vérifie si le dossier n'existe pas, on le cree
                if not os.path.exists(new_dest):
                    os.makedirs(new_dest)
                cv2.imwrite(new_img, image)

            # Leve une erreur si le nom du fichier n'existe pas
            except cv2.error:
                print(f"Le fichier {img_file} est introuvable ou n'existe pas")
                log(f"Tentative echouee, le fichier {img_file} est introuvable ou n'existe pas", log_file)
        # Ce n'est pas une image
        else:
            print(f"Le fichier {img_file} n'est pas de type image (.jpg, .png, .jpeg)")
            log(f"Tentative echouee, le type du fichier ({img_file}) est incorrect", log_file)

def filter_number(img, filters_list, log_file):
    new_image = img
    for filter in filters_list:
        if filter["name"] == "grayscale":
            new_image = g.grayscale(new_image)
            log("Gray Scale => Conversion de l'image en noir et blanc", log_file)
        if filter["name"] == "blur":
            new_image = b.blur(new_image, filter["intensity"])
            log(f"Gossian Blur => Conversion de l'image, application d'un flou de {filter['intensity']} sur l'image", log_file)
        if filter["name"] == "dilate":
            new_image = d.dilate(new_image, filter["intensity"])
            log(f"Dilate => Conversion de l'image, application d'une dilatation de {filter['intensity']} sur l'image", log_file)
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

def config_filter(content, log_file):

    filters_list = []
    # On récupère tous nos filtres dans un tableau
    all_filters = content.split("|")
    for filter in all_filters:
        # filter.split(":") = ['grayscale'] - ['blur', '10'] - ['dilate', '15']
        if "grayscale" in filter:
            grayscale = filter.split(":")
            filters_list.append({"name": grayscale[0]})
        if "blur" in filter:
            blur_split = filter.split(":")
            intensity = int(blur_split[1])
            # On vérifie que le flou soit positif ET impaire
            if intensity < 0 or intensity % 2 == 0:
                print("La valeur du flou doit etre positive ET impaire")
                log("Gossian Blur => Tentative echouee, la valeur du flou est incorrect", log_file)
                quit()
            else:
                filters_list.append({"name": blur_split[0], "intensity": intensity})
        if "dilate" in filter:
            dilate_split = filter.split(":")
            intensity = int(dilate_split[1])
            filters_list.append({"name": dilate_split[0], "intensity": intensity})

    return filters_list