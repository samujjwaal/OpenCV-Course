import cv2

img = cv2.imread("faces.jpeg", 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# path of pre trained model
path = "haarcascade_eye.xml"

# load pre trained model as cascaded classifier
eye_cascade = cv2.CascadeClassifier(path)

# perform face detection
eyes = eye_cascade.detectMultiScale(
    gray, scaleFactor=1.02, minNeighbors=20, minSize=(10, 10)
)
print(len(eyes))

# draw bounded box of each face detected
for (x, y, w, h) in eyes:
    xc = (x + x + w) / 2
    yc = (y + y + h) / 2
    radius = w / 2
    cv2.circle(img, (int(xc), int(yc)), int(radius), (0, 0, 255), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
