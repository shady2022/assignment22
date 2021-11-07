import cv2
import numpy as np


images = []
for i in range(1,4):
    img = cv2.imread(f"{i}.jpg", 0)
    images.append(img)
    rows , cols = img.shape

result = np.zeros((rows, cols), dtype="uint8")

for image in images:
    result += image//4

#img1 = cv2.imread("2.jpg", 0)
#img2 = cv2.imread("3.jpg", 0)
#img3 = cv2.imread("4.jpg", 0)
#img4 = cv2.imread("5.jpg", 0)



#result = img1//4 + img2//4 + img3//4 + img4//4

cv2.imwrite('output.jpg', result)
cv2.imshow('out_put', result)
cv2.waitKey()