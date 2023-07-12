import os

# Directorio que contiene el dataset con las fotos de las personas
"""dataset_path = 'C:/Users/USER/Documents/THAIS_U/SEPTIMO/Inteligencia Artificial/EjerciciosPython/Proyecto/dataset'"""
dataset_path = 'C:/REPOSITORIOIA/Proyecto/dataset'

def cargar_dataset():
    imagenes = []
    etiquetas = []
    personas = os.listdir(dataset_path)
    for persona in personas:
        persona_path = os.path.join(dataset_path, persona)
        for imagen_nombre in os.listdir(persona_path):
            imagen_path = os.path.join(persona_path, imagen_nombre)
            imagenes.append(imagen_path)
            etiquetas.append(persona)
    return imagenes, etiquetas
