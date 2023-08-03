import cv2

image=cv2.imread("Input/EmilyinParis.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

inverted=255-image

blurred=cv2.GaussianBlur(inverted,(21,21),0)
inverted_blurred=255-blurred

sketch=image/inverted_blurred
sketch=sketch*255

cv2.imwrite("Output/sketchphotoemily.jpg",sketch)