import cv2
import os

imagesPath = "C:/REPOSITORIOIA/Proyecto/fotos"

if not os.path.exists("faces"):
    os.makedirs("faces")
    print("Nueva carpeta: faces")

# Detector facial
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

count = 0
for imageName in os.listdir(imagesPath):
    print(imageName)
    image = cv2.imread(imagesPath + "/" + imageName)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convertir la imagen a escala de grises
    faces = faceClassif.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(200, 200))
    for (x, y, w, h) in faces:
        face = image[y:y + h, x:x + w]
        face = cv2.resize(face, (150, 150))
        cv2.imwrite("faces/" + str(count) + ".png", face)
        count += 1
