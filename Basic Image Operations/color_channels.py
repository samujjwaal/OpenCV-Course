import numpy as np
import cv2

# import image
color = cv2.imread("butterfly.jpg", 1)
cv2.imshow("Image", color)
cv2.moveWindow("Image", 0, 0)
print(color.shape)

# get the dimensions of image
height, width, channels = color.shape

# split each color channel into respective channel arrays
b, g, r = cv2.split(color)

rgb_split = np.empty([height, width * 3, channels], "uint8")

rgb_split[:, 0:width] = cv2.merge([b, b, b])
rgb_split[:, width : width * 2] = cv2.merge([g, g, g])
rgb_split[:, width * 2 : width * 3] = cv2.merge([r, r, r])

cv2.imshow("Channels", rgb_split)
cv2.moveWindow("Channels", 0, height)

cv2.waitKey(0)
cv2.destroyAllWindows()
