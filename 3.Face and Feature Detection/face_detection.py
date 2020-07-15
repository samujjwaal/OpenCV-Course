import cv2

img = cv2.imread("faces.jpeg", 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# path of pre trained model
path = "haarcascade_frontalface_default.xml"
# load pre trained model as cascaded classifier
face_cascade = cv2.CascadeClassifier(path)

# perform face detection
faces = face_cascade.detectMultiScale(
    gray, scaleFactor=1.06, minNeighbors=5, minSize=(55, 55)
)
print(len(faces))

# draw bounded box of each face detected
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
