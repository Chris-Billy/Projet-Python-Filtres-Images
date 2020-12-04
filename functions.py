import cv2
import os
from logger import log
from filters import grayscale as g, blur as b, dilate as d, filterZeTeam as z

def application_filter(img_dest, new_dest, filters_list, log_file):
    """
    Application du ou des filtres à toutes les images d'un dossier et enregistre une copie des images filtrées dans un dossier de sorti
    :param img_dest: le nom du dossier d'entrée ou sont les images d'ogirine (a string)
    :param new_dest: le nom du dossier de sortie ou seront enregistrés les images filtrées (a string)
    :param filters_list: une liste des filtres appliqués (a list [])
    :param log_file: le nom du fichier où stocker les log de l'application (file.log)
    """
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
    """
    Appliqué les filtres indiqué par l'utilisateur
    :param img: l'image sur laquelle appliqué le/les filtres
    :param filters_list: une liste des filtres appliqués (a list [])
    :param log_file: le nom du fichier où stocker les log de l'application (file.log)
    :return:
    """
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
        if filter["name"] == "message":
            new_image = z.zeteam(new_image, filter["text"])
            log(f"filterZeTeam => Conversion de l'image, application du texte {filter['text']} sur l'image", log_file)
    return new_image

def next_arg_exist(i, args):
    """
    Vérifie dans les arguments de la cli s'il y a un argument suivant
    :param i: indice de l'argument en cours
    :param args: un list de tous les arguments fournis en cli (a list [])
    :return: retourne True s'il y a un argument, sinon False
    """
    try:
        if not args[i+1]:
            print("Add arguments please")
            return False
        else:
            return True
    except IndexError:
        print("Add arguments please")
        return False

def config_filter(content, log_file):
    """
    Récupère les filtres fournis par l'utilisateur pour les enregistrer sous forme de dictionnaire dans une list
    :param content: les filtres donnés par l'utilisateur (a string)
    :param log_file: le nom du fichier où stocker les log de l'application (file.log)
    :return:
    """
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
        if "message" in filter:
            message = filter.split(":")
            text = message[1]
            filters_list.append({"name": message[0], "text": text})

    return filters_list