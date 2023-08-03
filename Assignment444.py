import cv2

image_one=cv2.imread("Input/spaces_1.webp")
image_two=cv2.imread("Input/spaces_2.webp")
# image_one=cv2.cvtColor(image_one,cv2.COLOR_BGR2GRAY)
# image_two=cv2.cvtColor(image_two,cv2.COLOR_BGR2GRAY)
image_one=255-image_one
image_two=255-image_two
result=cv2.subtract(image_one,image_two)
result=255-result
cv2.imwrite("Output/Secretsentence.webp",result)