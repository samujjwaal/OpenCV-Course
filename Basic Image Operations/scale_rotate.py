import cv2

img = cv2.imread("players.jpg", 1)

# Scaling image
img_half = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img_stretch = cv2.resize(img, (600, 600))
img_stretch_near = cv2.resize(img, (600, 600), interpolation=cv2.INTER_NEAREST)

cv2.imshow("Half", img_half)
cv2.imshow("Stretch", img_stretch)
cv2.imshow("Stretch near", img_stretch_near)

# Rotating image
M = cv2.getRotationMatrix2D((img.shape[1] / 2, img.shape[0] / 2), -30, 1)
rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("Rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
