import cv2

img = cv2.imread("sudoku.png", 0)
cv2.imshow("Original", img)

# simple thresholding
ret, thresh_basic = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)
cv2.imshow("Basic Binary", thresh_basic)

# adaptive thresholding
thresh_adapt = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 201, 1
)
cv2.imshow("Adaptive Threshold", thresh_adapt)

cv2.waitKey(0)
cv2.destroyAllWindows()
