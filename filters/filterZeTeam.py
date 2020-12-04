import cv2

def zeteam(img, text):
    """
    Appliquer un filtre qui ajoute un message sur une image
    :param img: l'image sur laquelle appliquer le filtre
    :param text: le message à écrire sur l'image (a string)
    :return: l'image modifié avec le filtre appliqué
    """
    # font
    font = cv2.FONT_HERSHEY_COMPLEX
    # org
    org = (50, 50)
    # fontScale
    fontScale = 1
    # Blue color in BGR
    color = (0, 0, 255)
    # Line thickness (px)
    thickness = 2

    return cv2.putText(img, text, org, font, fontScale, color, thickness, cv2.LINE_AA)