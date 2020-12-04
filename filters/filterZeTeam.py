import cv2

def zeteam(img, text):

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