import cv2
from heic2png import HEIC2PNG
import numpy as np

# Resto del código...


import numpy as np

def remove_background(image_path):
    print(image_path)
    # Cargar la imagen
    image = cv2.imread(image_path)

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar un umbral para separar el fondo de la persona
    _, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

    # Realizar una operación de apertura para eliminar pequeños ruidos en el fondo
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel, iterations=2)

    # Encontrar los contornos de los objetos en la imagen
    contours, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Crear una máscara del fondo
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    for contour in contours:
        cv2.drawContours(mask, [contour], 0, (255), -1)

    # Aplicar la máscara a la imagen original
    result = cv2.bitwise_and(image, image, mask=mask)

    return result


# Función para convertir una imagen HEIC a formato compatible con OpenCV
def convert_heic_to_png(image_path):
    png_path = image_path.replace('.heic', '.png')
    HEIC2PNG(image_path, png_path)
    return png_path

# Ruta de la imagen HEIC de entrada
image_path = 'C:\\Users\\USER\\Documents\\THAIS_U\\SEPTIMO\\Inteligencia Artificial\\EjerciciosPython\\Proyecto\\foto.heic'

# Convertir la imagen HEIC a formato PNG
output_path = image_path.replace('.heic', 'nv.png')
heic_img = HEIC2PNG(image_path)
heic_img.save(output_path)

# Cargar la imagen PNG convertida
image_cv2 = cv2.imread(output_path)

# Borrar el fondo de la imagen
output_image = remove_background(output_path)

# Mostrar la imagen de entrada y la imagen con el fondo borrado
cv2.imshow('Imagen Original', image_cv2)
cv2.imshow('Imagen con Fondo Borrado', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()