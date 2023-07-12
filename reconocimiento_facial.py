import cv2
import numpy as np
import joblib
from cargar_imagenes import cargar_dataset
from preprocesar_imagenes import preprocesar_imagen

# Cargar el dataset
imagenes, etiquetas = cargar_dataset()

# Preprocesar las imágenes
imagenes_procesadas = [preprocesar_imagen(imagen) for imagen in imagenes]

# Cargar el modelo entrenado y las clases de etiquetas
modelo = joblib.load('modelo.pkl')
clases_etiquetas = np.load('clases_etiquetas.npy')

# Inicializar la cámara
camara = cv2.VideoCapture(0)

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
        roi_gray_resized = cv2.resize(roi_gray, (150, 150))
        roi_gray_resized = roi_gray_resized.flatten()

        # Realizar el reconocimiento facial en la región de interés
        etiqueta_codificada = modelo.predict(np.array([roi_gray_resized]))
        etiqueta = clases_etiquetas[etiqueta_codificada]
        confianza = modelo.decision_function(np.array([roi_gray_resized]))

        # Dibujar un rectángulo alrededor del rostro detectado
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Mostrar el nombre de la persona reconocida y el porcentaje de coincidencia debajo del rectángulo
        texto = f'{etiqueta} ({confianza[0]:.2f})'
        cv2.putText(frame, texto, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    # Mostrar el frame en la ventana
    cv2.imshow('Reconocimiento Facial', frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar todas las ventanas
camara.release()
cv2.destroyAllWindows()
