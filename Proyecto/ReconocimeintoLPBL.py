import cv2
import os
import numpy as np

# Directorio que contiene el dataset con las fotos de las personas
dataset_path = "ruta_del_dataset"

# Cargar las imágenes y las etiquetas del dataset
def cargar_dataset():
    imagenes = []
    etiquetas = []
    personas = os.listdir(dataset_path)
    for persona in personas:
        persona_path = os.path.join(dataset_path, persona)
        for imagen_nombre in os.listdir(persona_path):
            imagen_path = os.path.join(persona_path, imagen_nombre)
            imagen = cv2.imread(imagen_path)
            imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises
            imagenes.append(imagen)
            etiquetas.append(persona)
    return imagenes, etiquetas

# Entrenar el modelo de reconocimiento facial
def entrenar_modelo(imagenes, etiquetas):
    modelo = cv2.face.LBPHFaceRecognizer_create()
    modelo.train(imagenes, np.array(etiquetas))
    return modelo

# Inicializar la cámara
camara = cv2.VideoCapture(0)

# Cargar el dataset
imagenes, etiquetas = cargar_dataset()

# Entrenar el modelo de reconocimiento facial
modelo = entrenar_modelo(imagenes, etiquetas)

# Iniciar el bucle principal para la detección y reconocimiento facial
while True:
    # Leer un frame de la cámara
    ret, frame = camara.read()

    # Convertir el frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Realizar la detección de rostros en el frame
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Para cada rostro detectado, realizar el reconocimiento facial
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]

        # Realizar el reconocimiento facial en la región de interés
        etiqueta, confianza = modelo.predict(roi_gray)

        # Dibujar un rectángulo alrededor del rostro detectado
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Mostrar el nombre de la persona reconocida debajo del rectángulo
        cv2.putText(frame, etiquetas[etiqueta], (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    # Mostrar el frame en la ventana
    cv2.imshow('Reconocimiento Facial', frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar todas las ventanas
camara.release()
cv2.destroyAllWindows()
