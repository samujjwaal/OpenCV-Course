import cv2

# import image
color = cv2.imread("butterfly.jpg", 1)

# convert to grayscale image
gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
cv2.imwrite("gray.jpg", gray)

b = color[:, :, 0]
g = color[:, :, 1]
r = color[:, :, 2]

rgba = cv2.merge((b, g, r, g))
cv2.imwrite("rgba.png", rgba)
