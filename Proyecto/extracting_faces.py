import cv2
import os
from PIL import Image

#imagesPath = 'C:/Users/USER/Documents/THAIS_U/SEPTIMO/Inteligencia Artificial/EjerciciosPython/Proyecto/FotosSinFondo/AlejandroBenjaminRocanoLopez'
#imagesPath = "C:/Users/USER/Documents/THAIS_U/SEPTIMO/Inteligencia Artificial/ProyectoIntento/fotosIA/ThaisElianaArmijosTroya"

##if not os.path.exists("Proyecto/faces"):
#     os.makedirs("Proyecto/faces")
#     print("Nueva carpeta: faces")
#
#faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#
#count = 0
#for imageName in os.listdir(imagesPath):
#     print(imageName)
#     image = cv2.imread(imagesPath + "/" + imageName)
#     faces = faceClassif.detectMultiScale(image, 1.1, 5)
#     for (x, y, w, h) in faces:
#          face = image[y:y + h, x:x + w]
#          face = cv2.resize(face, (150, 150))
#          cv2.imwrite("Proyecto/faces/" + str(count) + ".png", face)
#          count += 1


def obtener_rostro_fotos(carpeta_principal, carpeta_destino):
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Recorre todas las subcarpetas en la carpeta principal
    for nombre_subcarpeta in os.listdir(carpeta_principal):
        ruta_subcarpeta = os.path.join(carpeta_principal, nombre_subcarpeta)

        # Comprueba si es una carpeta
        if os.path.isdir(ruta_subcarpeta):
            # Crea la carpeta de destino si no existe
            carpeta_estudiante = os.path.join(carpeta_destino, nombre_subcarpeta)

            os.makedirs(carpeta_estudiante, exist_ok=True)

            # Recorre todos los archivos en la subcarpeta
            for nombre_archivo in os.listdir(ruta_subcarpeta):
                if nombre_archivo.endswith(".png"):
                    ruta_png = os.path.join(ruta_subcarpeta, nombre_archivo)

                    # Abre la imagen PNG utilizando PIL
                    imagen_png = cv2.imread(ruta_png)
                    faces = faceClassif.detectMultiScale(imagen_png, 1.1, 5)

                    for (x, y, w, h) in faces:
                         face = imagen_png[y:y + h, x:x + w]
                         face = cv2.resize(face, (150, 150))
                         cv2.imwrite(carpeta_estudiante+"/"+ nombre_archivo, face)


# Ruta de la carpeta principal que contiene las carpetas de los estudiantes
#carpeta_principal = 'C:/REPOSITORIOIA/Proyecto/FotosSinFondo'
carpeta_principal = 'C:/Users/USER/Documents/THAIS_U/SEPTIMO/Inteligencia Artificial/EjerciciosPython/Proyecto/FotosSinFondo'

# Ruta de la carpeta donde se guardarán las imágenes sin fondo
#carpeta_destino = 'C:/REPOSITORIOIA/Proyecto/FotosSoloRostros'
carpeta_destino = 'C:/Users/USER/Documents/THAIS_U/SEPTIMO/Inteligencia Artificial/EjerciciosPython/Proyecto/FotosSoloRostros/'

# Quita el fondo verde de las imágenes en la carpeta principal y las guarda en la carpeta de destino
obtener_rostro_fotos(carpeta_principal, carpeta_destino)