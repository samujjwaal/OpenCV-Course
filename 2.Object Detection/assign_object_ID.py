import numpy as np
import cv2
import random

# import color image
img = cv2.imread("fuzzy.png", 1)
cv2.imshow("Original", img)
# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# apply Gaussian Blur
blur = cv2.GaussianBlur(gray, (3, 3), 0)
# apply Adaptive Thresholding
thresh = cv2.adaptiveThreshold(
    blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 205, 1
)
cv2.imshow("Binary", thresh)

# find the contours in the image
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

# selecting shapes with area > 1000 px2
filtered = []
for c in contours:
    if cv2.contourArea(c) > 1000:
        filtered.append(c)
print(len(filtered))

# create new image to display contours
objects = np.zeros([img.shape[0], img.shape[1], 3], "uint8")
for c in filtered:
    # generate random colors
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(objects, [c], -1, color, -1)
    area = cv2.contourArea(c)
    p = cv2.arcLength(c, True)
    # print area and perimeter on console
    print(area, p)

cv2.imshow("Contours", objects)


cv2.waitKey(0)
cv2.destroyAllWindows()
