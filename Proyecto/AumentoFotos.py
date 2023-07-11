import cv2
import os
import numpy as np
import shutil

# Directorio raíz que contiene las subcarpetas de las personas
root_dir = 'C:/Users/USER/Documents/THAIS_U/SEPTIMO/Inteligencia Artificial/EjerciciosPython/Proyecto/FotosSoloRostros/'

# Directorio de destino para el dataset
dataset_dir = 'C:/Users/USER/Documents/THAIS_U/SEPTIMO/Inteligencia Artificial/EjerciciosPython/Proyecto/dataset'

# Lista de transformaciones de aumento de datos a aplicar
transformations = [
    ('rotation', 10),
    ('horizontal_flip', 0.5),
    ('scale', 0.2),
    ('crop', 0.1),
    ('brightness', 0.1),
    ('shift', 0.2)
]

def apply_rotation(image, angle):
    rows, cols = image.shape[:2]
    matrix = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    rotated = cv2.warpAffine(image, matrix, (cols, rows))
    return rotated

def apply_horizontal_flip(image):
    flipped = cv2.flip(image, 1)
    return flipped

def apply_scale(image, factor):
    rows, cols = image.shape[:2]
    scaled = cv2.resize(image, (int(cols*(1+factor)), int(rows*(1+factor))))
    return scaled

def apply_crop(image, ratio):
    rows, cols = image.shape[:2]
    cropped = image[int(rows*ratio):int(rows*(1-ratio)), int(cols*ratio):int(cols*(1-ratio))]
    return cropped

def apply_brightness(image, factor):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv[..., 2] = hsv[..., 2] * factor
    brightened = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return brightened

def apply_shift(image, shift):
    rows, cols = image.shape[:2]
    M = np.float32([[1, 0, shift], [0, 1, shift]])
    shifted = cv2.warpAffine(image, M, (cols, rows))
    return shifted

# Crear el directorio de destino del dataset
if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)
    print("Nueva carpeta: dataset")

# Iterar sobre las subcarpetas de las personas
for person_dir in os.listdir(root_dir):
    person_path = os.path.join(root_dir, person_dir)

    # Crear una subcarpeta en el directorio del dataset para la persona actual
    person_dataset_dir = os.path.join(dataset_dir, person_dir)
    if not os.path.exists(person_dataset_dir):
        os.makedirs(person_dataset_dir)
    
    # Iterar sobre las imágenes en la subcarpeta actual
    for image_file in os.listdir(person_path):
        image_path = os.path.join(person_path, image_file)
        image = cv2.imread(image_path)
        
        # Guardar la imagen original en el directorio del dataset
        output_path = os.path.join(person_dataset_dir, image_file)
        cv2.imwrite(output_path, image)
        
        # Aplicar las transformaciones de aumento de datos y guardar las imágenes generadas
        for transform, param in transformations:
            if np.random.uniform() < param:
                transformed_image = None
                
                if transform == 'rotation':
                    transformed_image = apply_rotation(image, 10)
                elif transform == 'horizontal_flip':
                    transformed_image = apply_horizontal_flip(image)
                elif transform == 'scale':
                    transformed_image = apply_scale(image, 0.2)
                elif transform == 'crop':
                    transformed_image = apply_crop(image, 0.1)
                elif transform == 'brightness':
                    transformed_image = apply_brightness(image, 0.6)
                elif transform == 'shift':
                    transformed_image = apply_shift(image, 10)
                
                if transformed_image is not None:
                    transformed_output_path = os.path.join(person_dataset_dir, f'{transform}_{image_file}')
                    cv2.imwrite(transformed_output_path, transformed_image)
