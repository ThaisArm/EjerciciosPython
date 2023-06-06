import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def aplicar_filtro(imagen, filas_filtro, columnas_filtro):
    # Obtener el ancho y alto de la imagen original
    ancho, alto = imagen.size

    # Cargar los píxeles de la imagen original
    pixeles = imagen.load()

    # Matriz del filtro con todos los elementos iguales a 1
    matriz_filtro = [[1] * columnas_filtro for _ in range(filas_filtro)]

    # Crear una nueva imagen filtrada con dimensiones reducidas
    ancho_reducido = ancho // columnas_filtro
    alto_reducido = alto // filas_filtro
    nueva_imagen = Image.new("RGB", (ancho_reducido, alto_reducido))

    # Cargar los píxeles de la nueva imagen filtrada
    nuevos_pixeles = nueva_imagen.load()

    # Recorrer cada píxel de la imagen original
    for y in range(alto_reducido):
        for x in range(ancho_reducido):
            # Inicializar las variables para acumular los valores de color
            r_total, g_total, b_total = 0, 0, 0
            contador = 0

            # Recorrer los píxeles vecinos alrededor del píxel actual usando el tamaño del filtro
            for i in range(filas_filtro):
                for j in range(columnas_filtro):
                    # Calcular las coordenadas de los píxeles vecinos
                    nx = x * columnas_filtro + j
                    ny = y * filas_filtro + i

                    # Obtener el color del píxel vecino
                    pixel = pixeles[nx, ny]
                    r, g, b = pixel

                    # Multiplicar el valor de cada canal de color por el elemento correspondiente
                    # en la matriz del filtro
                    r_total += r * matriz_filtro[i][j]
                    g_total += g * matriz_filtro[i][j]
                    b_total += b * matriz_filtro[i][j]

                    # Incrementar el contador de píxeles vecinos válidos
                    contador += 1

            # Calcular el promedio de los valores de color
            r_promedio = r_total // contador
            g_promedio = g_total // contador
            b_promedio = b_total // contador

            # Establecer el píxel resultante en la nueva imagen filtrada
            nuevos_pixeles[x, y] = (r_promedio, g_promedio, b_promedio)

    # Devolver la nueva imagen filtrada
    return nueva_imagen

def abrir_imagen():
    ruta = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg")])

    if ruta:
        global imagen
        imagen = Image.open(ruta)

        # Convertir la imagen original en un objeto ImageTk.PhotoImage
        foto_original = ImageTk.PhotoImage(imagen.resize((400, 400)))

        # Actualizar el tamaño del lienzo de la imagen original
        canvas_original.configure(width=400, height=400)
        canvas_original.delete("all")
        canvas_original.image = foto_original
        canvas_original.create_image(0, 0, anchor="nw", image=foto_original)

def aplicar_filtro_y_mostrar():
    filas_filtro = int(entry_filas_filtro.get())
    columnas_filtro = int(entry_columnas_filtro.get())
    nueva_imagen = aplicar_filtro(imagen, filas_filtro, columnas_filtro)

    # Convertir la imagen filtrada en un objeto ImageTk.PhotoImage
    foto_filtrada = ImageTk.PhotoImage(nueva_imagen.resize((400, 400)))

    # Actualizar el tamaño del lienzo de la imagen filtrada
    canvas_filtrada.configure(width=400, height=400)
    canvas_filtrada.delete("all")
    canvas_filtrada.image = foto_filtrada
    canvas_filtrada.create_image(0, 0, anchor="nw", image=foto_filtrada)

root = tk.Tk()
root.title("Redimensionar Imagen")

# Frame para los botones y la caja de texto
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

boton_abrir = tk.Button(frame_botones, text="Abrir Imagen", command=abrir_imagen)
boton_abrir.pack(side="left", padx=5)

label_filas_filtro = tk.Label(frame_botones, text="Filas del filtro:")
label_filas_filtro.pack(side="left", padx=5)

entry_filas_filtro = tk.Entry(frame_botones)
entry_filas_filtro.pack(side="left", padx=5)

label_columnas_filtro = tk.Label(frame_botones, text="Columnas del filtro:")
label_columnas_filtro.pack(side="left", padx=5)

entry_columnas_filtro = tk.Entry(frame_botones)
entry_columnas_filtro.pack(side="left", padx=5)

boton_aplicar = tk.Button(frame_botones, text="Aplicar Filtro", command=aplicar_filtro_y_mostrar)
boton_aplicar.pack(side="left", padx=5)

# Frame para la imagen original y la imagen filtrada
frame_imagenes = tk.Frame(root)
frame_imagenes.pack()

canvas_original = tk.Canvas(frame_imagenes)
canvas_original.pack(side="left", padx=10)

canvas_filtrada = tk.Canvas(frame_imagenes)
canvas_filtrada.pack(side="left", padx=10)

root.mainloop()
