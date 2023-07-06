import os
from PIL import Image
from heic2png import HEIC2PNG

def recortar_lados_imagen(imagen):
    ancho, alto = imagen.size
    left = 1000
    top = 500
    right = ancho - 700
    bottom = alto - 1200
    return imagen.crop((left, top, right, bottom))

def redimensionar_imagen(imagen, tamaño):
    return imagen.resize(tamaño)

def convertir_carpeta_heic_a_png(carpeta_principal, carpeta_destino, tamaño_redimensionado):
    # Recorre todas las subcarpetas en la carpeta principal
    for nombre_subcarpeta in os.listdir(carpeta_principal):
        ruta_subcarpeta = os.path.join(carpeta_principal, nombre_subcarpeta)

        # Comprueba si es una carpeta
        if os.path.isdir(ruta_subcarpeta):
            # Crea la carpeta de destino si no existe
            carpeta_estudiante = os.path.join(carpeta_destino, nombre_subcarpeta)
            os.makedirs(carpeta_estudiante, exist_ok=True)

            # Recorre todos los archivos en la subcarpeta HEIC
            for nombre_archivo in os.listdir(ruta_subcarpeta):
                if nombre_archivo.endswith(".heic"):
                    ruta_heic = os.path.join(ruta_subcarpeta, nombre_archivo)

                    # Genera el nombre de archivo de salida PNG
                    nombre_archivo_png = nombre_archivo[:-5] + ".png"
                    ruta_png = os.path.join(carpeta_estudiante, nombre_archivo_png)

                    # Abre la imagen HEIC utilizando pyheif-pil
                    heic_img = Image.open(ruta_heic)

                    # Recorta los lados de la imagen
                    heic_img_recortada = recortar_lados_imagen(heic_img)

                    # Redimensiona la imagen recortada
                    heic_img_redimensionada = redimensionar_imagen(heic_img_recortada, tamaño_redimensionado)

                    # Convierte la imagen redimensionada a formato PNG
                    heic_img_redimensionada.save(ruta_png, "PNG")

# Ruta de la carpeta principal que contiene las carpetas de los estudiantes
carpeta_principal = 'C:/REPOSITORIOIA/Proyecto/FotosHeic'

# Ruta de la carpeta donde se guardarán las fotos PNG
carpeta_destino = 'C:/REPOSITORIOIA/Proyecto/FotosPng' 


# Tamaño al que se redimensionarán las imágenes (ancho, alto)
tamaño_redimensionado = (200, 200)

# Convierte las carpetas de fotos HEIC de los estudiantes a formato PNG, recortando los lados de las imágenes y redimensionándolas previamente, y elimina los archivos HEIC
convertir_carpeta_heic_a_png(carpeta_principal, carpeta_destino,  tamaño_redimensionado)
