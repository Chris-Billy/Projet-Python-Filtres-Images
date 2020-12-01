import cv2

dossier_img = "./imgs/"
dossier_filter = "./imgs/filter_img/"

image = cv2.imread('./imgs/tigre.jpg')
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite(dossier_filter + "tigreNB.jpg", img_gray)