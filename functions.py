import cv2
import os
from filters import blur as b

#enregistrer l'image dans output

# Afficher le dossier sous forme de liste
def browse_folder(folder):
    folder_list = os.listdir(folder)
    return folder_list

def filtre(list_folder):
    for picture in list_folder:
        b.blur(picture, )



# Appliquer un filtre pour chaque image du dossier


imgg = browse_folder('./imgs/')
print(imgg)