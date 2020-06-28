import numpy as np
import cv2

# create black image with dimensions 150x200 and only 1 colour channel
black = np.zeros([150, 200, 1], "uint8")
cv2.imshow("Black", black)
# print color value at pixel 0,0 of all channels
print(black[0, 0, :])

# create almost black image with dimensions 150x200 and 3 colour channels
ones = np.ones([150, 200, 3], "uint8")
cv2.imshow("Ones", ones)
# print color value at pixel 0,0 of all channels
print(ones[0, 0, :])


# create white image with dimensions 150x200 and 3 colour channels
white = np.ones([150, 200, 3], "uint16")
white *= (2 ** 16) - 1
cv2.imshow("White", white)
# print color value at pixel 0,0 of all channels
print(white[0, 0, :])

# create deep copy of ones array
color = ones.copy()
# setting color to green as per BGR color scheme
color[:, :] = (0, 255, 0)
cv2.imshow("Green", color)
print(color[0, 0, :])


cv2.waitKey(0)
cv2.destroyAllWindows()
