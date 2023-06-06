import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def apply_filter(image, filter_rows, filter_columns):
    # Obtener el ancho y alto de la imagen original
    width, height = image.size

    # Cargamos los píxeles de la imagen original
    pixels = image.load()

    # Matriz del filtro con todos los elementos iguales a 1
    filter_matrix = [[1] * filter_columns for _ in range(filter_rows)]

    # Creamos una nueva imagen filtrada con dimensiones reducidas
    reduced_width = width // filter_columns
    reduced_height = height // filter_rows
    new_image = Image.new("RGB", (reduced_width, reduced_height))

    # Cargamos los píxeles de la nueva imagen filtrada
    new_pixels = new_image.load()

    # Recorremos cada píxel de la imagen original
    for y in range(reduced_height):
        for x in range(reduced_width):
            # Inicializamos las variables para acumular los valores de color
            r_total, g_total, b_total = 0, 0, 0
            count = 0

            # Recorremos los píxeles vecinos alrededor del píxel actual usando el tamaño del filtro
            for i in range(filter_rows):
                for j in range(filter_columns):
                    # Calculamos las coordenadas de los píxeles vecinos
                    nx = x * filter_columns + j
                    ny = y * filter_rows + i

                    # Obtenemos el color del píxel vecino
                    pixel = pixels[nx, ny]
                    r, g, b = pixel

                    # Multiplicamos el valor de cada canal de color por el elemento correspondiente
                    # en la matriz del filtro
                    r_total += r * filter_matrix[i][j]
                    g_total += g * filter_matrix[i][j]
                    b_total += b * filter_matrix[i][j]

                    # Incrementamos el contador de píxeles vecinos válidos
                    count += 1

            # Calculamos el promedio de los valores de color
            r_avg = r_total // count
            g_avg = g_total // count
            b_avg = b_total // count

            # Establecemos el píxel resultante en la nueva imagen filtrada
            new_pixels[x, y] = (r_avg, g_avg, b_avg)

    # Devolvemos la nueva imagen filtrada
    return new_image

def open_image():
    path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

    if path:
        global image
        image = Image.open(path)

        # Obtener el tamaño original de la imagen original
        original_width, original_height = image.size

        # Convertir la imagen original en un objeto ImageTk.PhotoImage
        original_photo = ImageTk.PhotoImage(image)

        # Actualizar el tamaño del lienzo de la imagen original
        original_canvas.configure(width=original_width, height=original_height)
        original_canvas.delete("all")
        original_canvas.image = original_photo
        original_canvas.create_image(0, 0, anchor="nw", image=original_photo)

def apply_filter_and_show():
    filter_rows = int(filter_rows_entry.get())
    filter_columns = int(filter_columns_entry.get())
    new_image = apply_filter(image, filter_rows, filter_columns)

    # Obtener el tamaño actualizado de la imagen filtrada
    filtered_width, filtered_height = new_image.size

    # Convertir la imagen filtrada en un objeto ImageTk.PhotoImage
    filtered_photo = ImageTk.PhotoImage(new_image)

    # Actualizar el tamaño del lienzo de la imagen filtrada
    filtered_canvas.configure(width=filtered_width, height=filtered_height)
    filtered_canvas.delete("all")
    filtered_canvas.image = filtered_photo
    filtered_canvas.create_image(0, 0, anchor="nw", image=filtered_photo)

root = tk.Tk()
root.title("Redimensionar Imagen")

# Frame para los botones y la caja de texto
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

open_button = tk.Button(buttons_frame, text="Cargar Imagen", command=open_image)
open_button.pack(side="left", padx=5)

filter_rows_label = tk.Label(buttons_frame, text="Filas del filtro:")
filter_rows_label.pack(side="left", padx=5)

filter_rows_entry = tk.Entry(buttons_frame)
filter_rows_entry.pack(side="left", padx=5)

filter_columns_label = tk.Label(buttons_frame, text="Columnas del filtro:")
filter_columns_label.pack(side="left", padx=5)

filter_columns_entry = tk.Entry(buttons_frame)
filter_columns_entry.pack(side="left", padx=5)

apply_button = tk.Button(buttons_frame, text="Redimensionar", command=apply_filter_and_show)
apply_button.pack(side="left", padx=5)

# Frame para la imagen original y la imagen filtrada
images_frame = tk.Frame(root)
images_frame.pack()

original_canvas = tk.Canvas(images_frame)
original_canvas.pack(side="left", padx=10)

filtered_canvas = tk.Canvas(images_frame)
filtered_canvas.pack(side="left", padx=10)

root.mainloop()
