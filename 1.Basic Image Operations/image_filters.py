import cv2
import numpy as np

# import image
image = cv2.imread("thresh.jpg", 1)
cv2.imshow("Original", image)

# apply Gaussian Blur on image
# blur values for each axis need to be odd numbers
blur = cv2.GaussianBlur(image, (5, 51), 0)
cv2.imshow("Blur", blur)

# kernel size for each axis need to be odd numbers
kernel = np.ones((5, 5), "uint8")

dilate = cv2.dilate(image, kernel, iterations=1)
erode = cv2.erode(image, kernel, iterations=1)

cv2.imshow("Dilate", dilate)
cv2.imshow("Erode", erode)


cv2.waitKey(0)
cv2.destroyAllWindows()
