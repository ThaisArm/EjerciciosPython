import os
from PIL import Image

def quitar_fondo_verde(imagen):
    # Obtener los píxeles de la imagen
    pixels = imagen.load()

    # Dimensiones de la imagen
    width, height = imagen.size

    # Recorrer cada píxel de la imagen
    for y in range(height):
        for x in range(width):
            # Obtener el valor de píxel
            pixel = pixels[x, y]

            # Comprobar si el píxel tiene un tono de verde
            if pixel[1] > pixel[0] and pixel[1] > pixel[2]:
                # Asignar un píxel transparente
                pixels[x, y] = (0, 0, 0, 0)

    return imagen

def quitar_fondo_verde_carpeta(carpeta_principal, carpeta_destino):
    # Recorre todas las subcarpetas en la carpeta principal
    for nombre_subcarpeta in os.listdir(carpeta_principal):
        ruta_subcarpeta = os.path.join(carpeta_principal, nombre_subcarpeta)

        # Comprueba si es una carpeta
        if os.path.isdir(ruta_subcarpeta):
            # Crea la carpeta de destino si no existe
            carpeta_estudiante = os.path.join(carpeta_destino, nombre_subcarpeta.replace (" ", ""))
            os.makedirs(carpeta_estudiante, exist_ok=True)

            # Recorre todos los archivos en la subcarpeta
            for nombre_archivo in os.listdir(ruta_subcarpeta):
                if nombre_archivo.endswith(".png"):
                    ruta_png = os.path.join(ruta_subcarpeta, nombre_archivo)

                    # Abre la imagen PNG utilizando PIL
                    imagen_png = Image.open(ruta_png).convert("RGBA")

                    # Quita el fondo verde de la imagen
                    imagen_sin_fondo = quitar_fondo_verde(imagen_png)

                    # Genera el nombre de archivo de salida PNG
                    nombre_archivo_sin_fondo = nombre_archivo[:-4] + "_sin_fondo.png"
                    ruta_sin_fondo = os.path.join(carpeta_estudiante, nombre_archivo_sin_fondo)

                    # Guarda la imagen sin fondo en la carpeta de destino
                    imagen_sin_fondo.save(ruta_sin_fondo, "PNG")

# Ruta de la carpeta principal que contiene las carpetas de los estudiantes
#carpeta_principal = 'C:/REPOSITORIOIA/Proyecto/FotosPng'
carpeta_principal = 'C:/Users/USER/Documents/THAIS_U/SEPTIMO/Inteligencia Artificial/EjerciciosPython/Proyecto/FotosPng'

# Ruta de la carpeta donde se guardarán las imágenes sin fondo
#carpeta_destino = 'C:/REPOSITORIOIA/Proyecto/FotosSinFondo'
carpeta_destino = 'C:/Users/USER/Documents/THAIS_U/SEPTIMO/Inteligencia Artificial/EjerciciosPython/Proyecto/FotosSinFondo/'

# Quita el fondo verde de las imágenes en la carpeta principal y las guarda en la carpeta de destino
quitar_fondo_verde_carpeta(carpeta_principal, carpeta_destino)