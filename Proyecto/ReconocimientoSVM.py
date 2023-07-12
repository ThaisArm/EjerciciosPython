import cv2
import os
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Directorio que contiene el dataset con las fotos de las personas
dataset_path = 'C:/Users/USER/Documents/THAIS_U/SEPTIMO/Inteligencia Artificial/EjerciciosPython/Proyecto/dataset'

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

# Preprocesar las imágenes para el entrenamiento de SVM
def preprocesar_imagenes(imagenes):
    imagenes_procesadas = []
    for imagen in imagenes:
        imagen = cv2.resize(imagen, (150, 150))  # Redimensionar las imágenes a un tamaño común
        imagen = imagen.flatten()  # Aplanar la imagen en un vector
        imagenes_procesadas.append(imagen)
    imagenes_procesadas = np.array(imagenes_procesadas)
    return imagenes_procesadas

# Codificar las etiquetas de las personas en forma numérica
def codificar_etiquetas(etiquetas):
    encoder = LabelEncoder()
    etiquetas_codificadas = encoder.fit_transform(etiquetas)
    return etiquetas_codificadas, encoder.classes_

# Dividir el dataset en conjuntos de entrenamiento y prueba
def dividir_dataset(imagenes, etiquetas, test_size=0.2):
    X_train, X_test, y_train, y_test = train_test_split(imagenes, etiquetas, test_size=test_size, random_state=42)
    return X_train, X_test, y_train, y_test

# Entrenar el modelo de reconocimiento facial SVM
def entrenar_modelo(imagenes, etiquetas):
    X_train, X_test, y_train, y_test = dividir_dataset(imagenes, etiquetas)
    modelo = SVC(kernel='linear')
    modelo.fit(X_train, y_train)
    precision_entrenamiento = modelo.score(X_train, y_train)
    precision_testeo = modelo.score(X_test, y_test)
    return modelo, precision_entrenamiento, precision_testeo

# Inicializar la cámara
camara = cv2.VideoCapture(0)

# Cargar el dataset
imagenes, etiquetas = cargar_dataset()

# Preprocesar las imágenes
imagenes_procesadas = preprocesar_imagenes(imagenes)

# Codificar las etiquetas
etiquetas_codificadas, clases_etiquetas = codificar_etiquetas(etiquetas)

# Entrenar el modelo SVM
modelo, precision_entrenamiento, precision_testeo = entrenar_modelo(imagenes_procesadas, etiquetas_codificadas)

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
        roi_gray_resized = cv2.resize(roi_gray, (150, 150))  # Redimensionar la región de interés
        roi_gray_resized = roi_gray_resized.flatten()  # Aplanar la imagen en un vector

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
