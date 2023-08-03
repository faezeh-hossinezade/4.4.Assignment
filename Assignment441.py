import cv2
import numpy as np

img1=cv2.imread("Input/img1.jpg")
img2=cv2.imread("Input/img2.jpg")

img1=img1.astype(np.float32)
img2=img2.astype(np.float32)
    
result1=(img1*4/5 +img2*1/5)
result1=result1.astype(np.int32)

result2=(img1*3/5 +img2*2/5)
result2=result2.astype(np.int32)

result3=(img1*2/5 +img2*3/5)
result3=result3.astype(np.int32)

result4=(img1*1/5 +img2*4/5)
result4=result4.astype(np.int32)


im_h = np.concatenate((img1,result1,result2,result3,result4, img2), axis=1)
cv2.imwrite("Output/FaceMorphing.jpg",im_h)

cv2.waitKey()