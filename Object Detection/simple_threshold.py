import cv2
import numpy as np

bw = cv2.imread("detect_blob.png", 0)
height, width = bw.shape[0:2]

cv2.imshow("Original BW", bw)

#  numpy matrix to crate segmented image
binary = np.zeros([height, width, 1], "uint8")

threshold = 85

for row in range(height):
    for col in range(width):
        if bw[row, col] >= threshold:
            binary[row, col] = 255

cv2.imshow("Slow binary", binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
