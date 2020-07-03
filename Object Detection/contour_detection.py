import cv2

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

# draw contours on image to display
cv2.drawContours(img2, contours, index, color, thickness)
cv2.imshow("Contours", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
