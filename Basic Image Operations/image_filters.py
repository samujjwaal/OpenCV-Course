import cv2

# import image
image = cv2.imread("thresh.jpg", 1)
cv2.imshow("Original", image)

# apply Gaussian Blur on image
# blur values for each axis need to be odd numbers
blur = cv2.GaussianBlur(image, (5, 51), 0)
cv2.imshow("Blur", blur)


cv2.waitKey(0)
cv2.destroyAllWindows()
