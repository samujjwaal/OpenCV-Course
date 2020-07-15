import cv2

frame = cv2.imread("players.jpg", 0)
template = cv2.imread("template.jpg", 0)

cv2.imshow("Frame", frame)
cv2.imshow("Template", template)

# perform template matching
result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)

# find intensity and coordinates of points with lowest and highest intensity
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(max_val, max_val)
# highlight brightest spot on image
cv2.circle(result, max_loc, 15, 255, 2)
cv2.imshow("Matching", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
