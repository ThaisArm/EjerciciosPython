from PIL import Image

heic_image_path = 'C:\\IAREPOSITORIO\\Proyecto\\foto.heic'
# Ruta de la imagen HEIC
image_path = 'C:\\IAREPOSITORIO\\Proyecto\\fotonv.png'

# Abrir la imagen PNG y convertirla a RGBA
image = Image.open(image_path).convert('RGBA')

# Obtener los píxeles de la imagen
pixels = image.load()

# Dimensiones de la imagen
width, height = image.size

# Recortar la imagen desde el lado izquierdo en 30000 píxeles
left_offset = 500
image = image.crop((left_offset, 0, width, height))

# Obtener los nuevos píxeles de la imagen recortada
pixels = image.load()

# Recorrer cada píxel de la imagen
for y in range(height):
    for x in range(width - left_offset):
        r, g, b, a = pixels[x, y]

        # Comprobar si el píxel tiene un tono de verde
        if g > r and g > b:
            # Asignar un píxel transparente
            pixels[x, y] = (0, 0, 0, 0)

# Guardar la imagen modificada en formato PNG
output_path = 'Proyecto\\final.png'
image.save(output_path, 'PNG')
