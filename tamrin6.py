import cv2

img = cv2.imread('Mona_Lisa.jpg', 0)

inverted = 255 - img
blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
inverted_blurred = 255 - blurred

sketch = img / inverted_blurred
sketch = sketch * 255

cv2.imwrite('out_put.jpg', sketch)