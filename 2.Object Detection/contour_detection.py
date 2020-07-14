import cv2
import numpy as np

img = cv2.imread("detect_blob.png", 1)
# convert to grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# apply adaptive thresholding
thresh = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1
)
cv2.imshow("Binary", thresh)

# get contours for the image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# create deep copy of the image
img2 = img.copy()
index = -1  # to get all contours
thickness = 4
color = (255, 0, 255)  # pink color

# initialize empty numpy array for blank image
objects = np.zeros([img.shape[0], img.shape[1], 3], "uint8")

for c in contours:
    # draw contour on blank image
    cv2.drawContours(objects, [c], -1, color, -1)

    # calculate area and perimeter of contour
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)

    # calculate moments of image to calculate centroid
    M = cv2.moments(c)
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    cv2.circle(objects, (cx, cy), 4, (0, 0, 255), -1)

    print(f"Area:{area} Perimeter:{perimeter}")

cv2.imshow("Contours", objects)

cv2.waitKey(0)
cv2.destroyAllWindows()
