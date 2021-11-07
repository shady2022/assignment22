import cv2
import numpy as numPy

img1 = cv2.imread('h13.jpg',0)
img2 = cv2.imread('h10.jpg',0)

img1 = cv2.resize(img1,(150,250))
img2 = cv2.resize(img2,(150,250))


result1 = img1//2 + img2//8
result2 = img1//2 + img2//4
result3 = img1//2 + img2//2
result4 = img1//4 + img2//2
result5 = img1//8 + img2//2

Result = numPy.concatenate((img1,result1,result2,result3,result4,result5,img2),axis=1)

cv2.imshow('Photo',Result)
cv2.waitKey()
