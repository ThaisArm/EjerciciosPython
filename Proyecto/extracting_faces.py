import cv2
import os

imagesPath = "C:/Users/USER/Documents/THAIS_U/SEPTIMO/Inteligencia Artificial/ProyectoIntento/fotosIA2/Abrahamm"
#imagesPath = "C:/Users/USER/Documents/THAIS_U/SEPTIMO/Inteligencia Artificial/ProyectoIntento/fotosIA/ThaisElianaArmijosTroya"

if not os.path.exists("faces"):
     os.makedirs("faces")
     print("Nueva carpeta: faces")

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

count = 0
for imageName in os.listdir(imagesPath):
     print(imageName)
     image = cv2.imread(imagesPath + "/" + imageName)
     faces = faceClassif.detectMultiScale(image, 1.1, 5)
     for (x, y, w, h) in faces:
          face = image[y:y + h, x:x + w]
          face = cv2.resize(face, (150, 150))
          cv2.imwrite("faces/" + str(count) + ".jpg", face)
          count += 1
