from heic2png import HEIC2PNG
import cv2

# Ruta de la imagen HEIC
heic_image_path = 'Proyecto/foto.heic'

# Ruta de salida para la imagen recortada
output_path = 'Proyecto/foto.png'

# Convertir la imagen HEIC a PNG con heic2png
heic2png = HEIC2PNG(heic_image_path)
heic2png.save(output_path)

# Cargar la imagen PNG con OpenCV
image = cv2.imread(output_path)

# Dimensiones de la imagen
height, width, _ = image.shape

# Definir los valores de recorte en todos los lados
left_offset = 1150
top_offset = 1050
right_offset = width - 1050
bottom_offset = height - 1100

# Aplicar el recorte en todos los lados
cropped_image = image[top_offset:bottom_offset, left_offset:right_offset]

# Guardar la imagen recortada
cv2.imwrite(output_path, cropped_image)
