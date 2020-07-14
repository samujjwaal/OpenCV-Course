import cv2
import numpy as np

img = cv2.imread("faces.jpeg", 1)
# to scale image to fit my screen size
img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)

# convert to hsv color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h = hsv[:, :, 0]
s = hsv[:, :, 1]
v = hsv[:, :, 2]

hsv_split = np.concatenate((h, s, v), axis=1)
cv2.imshow("HSV Split", hsv_split)

ret, min_sat = cv2.threshold(s, 40, 255, cv2.THRESH_BINARY)
cv2.imshow("Sat Filter", min_sat)

ret, min_hue = cv2.threshold(h, 15, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Hue Filter", min_hue)

final = cv2.bitwise_and(min_sat, min_hue)
cv2.imshow("Final", final)
cv2.imshow("Original", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
