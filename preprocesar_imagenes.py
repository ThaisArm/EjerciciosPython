import cv2
import numpy as np
import joblib
from cargar_imagenes import cargar_dataset

# Cargar el dataset
imagenes, etiquetas = cargar_dataset()

def preprocesar_imagen(imagen_path):
    imagen = cv2.imread(imagen_path)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    imagen = cv2.resize(imagen, (150, 150))
    imagen = imagen.flatten()
    return imagen

# Preprocesar las imágenes
imagenes_procesadas = [preprocesar_imagen(imagen) for imagen in imagenes]

# Guardar las imágenes preprocesadas en un archivo
joblib.dump(imagenes_procesadas, 'imagenes_procesadas.pkl')
