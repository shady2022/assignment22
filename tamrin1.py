import cv2

img1 = cv2.imread("a.tif", 0)
img2 = cv2.imread("b.tif", 0)

result = img2 - img1

cv2.imshow("NEW_IMAGE", result)
cv2.waitKey()