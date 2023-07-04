import os
from heic2png import HEIC2PNG

def convertir_carpeta_heic_a_png(carpeta_heic, carpeta_png):
    # Crea la carpeta de destino si no existe
    os.makedirs(carpeta_png, exist_ok=True)

    # Recorre todos los archivos en la carpeta HEIC
    for nombre_archivo in os.listdir(carpeta_heic):
        if nombre_archivo.endswith(".heic"):
            ruta_heic = os.path.join(carpeta_heic, nombre_archivo)

            # Genera el nombre de archivo de salida PNG
            nombre_archivo_png = nombre_archivo[:-5] + ".png"
            ruta_png = os.path.join(carpeta_png, nombre_archivo_png)

            # Convierte el archivo HEIC a PNG
            heic_img = HEIC2PNG(ruta_heic)
            heic_img.save(ruta_png)

# Ruta de la carpeta que contiene las fotos HEIC
carpeta_heic = 'C:/REPOSITORIOIA/Proyecto/FotosAlumnos/Abraham Danilo Miranda López'

# Ruta de la carpeta donde se guardarán las fotos PNG
carpeta_png = 'C:/REPOSITORIOIA/Proyecto/FotosAlumnos/Abraham Danilo Miranda López'

# Convierte la carpeta de fotos HEIC a formato PNG
convertir_carpeta_heic_a_png(carpeta_heic, carpeta_png)
