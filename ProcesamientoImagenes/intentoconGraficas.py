import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

def cargar_imagen():
    ruta_imagen = filedialog.askopenfilename(filetypes=(("Archivos de imagen", "*.jpg;*.png;*.jpeg"), ("Todos los archivos", "*.*")))
    if ruta_imagen:
        global imagen_original
        imagen_original = Image.open(ruta_imagen)
        imagen_original.thumbnail((400, 400))
        imagen_tk = ImageTk.PhotoImage(imagen_original)
        label_imagen_original.configure(image=imagen_tk)
        label_imagen_original.image = imagen_tk
        cargar_valores_rgb(imagen_original)

def cargar_valores_rgb(imagen):
    r, g, b = imagen.split()
    valor_r = r.getextrema()[1]
    valor_g = g.getextrema()[1]
    valor_b = b.getextrema()[1]
    scale_r.set(valor_r)
    scale_g.set(valor_g)
    scale_b.set(valor_b)
    modificar_imagen()

def modificar_imagen(*args):
    valor_r = scale_r.get()
    valor_g = scale_g.get()
    valor_b = scale_b.get()
    imagen_modificada = imagen_original.copy()
    r, g, b = imagen_modificada.split()
    r = r.point(lambda x: x + int(valor_r))
    g = g.point(lambda x: x + int(valor_g))
    b = b.point(lambda x: x + int(valor_b))
    imagen_modificada = Image.merge("RGB", (r, g, b))
    imagen_modificada.thumbnail((400, 400))
    imagen_tk = ImageTk.PhotoImage(imagen_modificada)
    label_imagen_modificada.configure(image=imagen_tk)
    label_imagen_modificada.image = imagen_tk
    mostrar_imagenes_rgb(r, g, b)

def mostrar_imagenes_rgb(imagen_r, imagen_g, imagen_b):
    imagen_r.thumbnail((200, 200))
    imagen_g.thumbnail((200, 200))
    imagen_b.thumbnail((200, 200))
    imagen_tk_r = ImageTk.PhotoImage(imagen_r)
    imagen_tk_g = ImageTk.PhotoImage(imagen_g)
    imagen_tk_b = ImageTk.PhotoImage(imagen_b)
    label_imagen_r.configure(image=imagen_tk_r)
    label_imagen_g.configure(image=imagen_tk_g)
    label_imagen_b.configure(image=imagen_tk_b)
    label_imagen_r.image = imagen_tk_r
    label_imagen_g.image = imagen_tk_g
    label_imagen_b.image = imagen_tk_b

def establecer_valores_por_defecto():
    scale_r.set(0)
    scale_g.set(0)
    scale_b.set(0)

# Crear ventana
ventana = tk.Tk()
ventana.title("Editor de Imágenes")

# Botón para cargar imagen
boton_cargar = tk.Button(ventana, text="Cargar Imagen", command=cargar_imagen)
boton_cargar.pack(pady=10)

# Frame para mostrar las imágenes
frame_imagenes = tk.Frame(ventana)
frame_imagenes.pack()

# Label para mostrar imagen original
label_imagen_original = tk.Label(frame_imagenes)
label_imagen_original.pack(side=tk.LEFT, padx=10, pady=10)

# Label para mostrar imagen R
label_imagen_r = tk.Label(frame_imagenes)
label_imagen_r.pack(side=tk.LEFT, padx=10)

# Label para mostrar imagen G
label_imagen_g = tk.Label(frame_imagenes)
label_imagen_g.pack(side=tk.LEFT, padx=10)

# Label para mostrar imagen B
label_imagen_b = tk.Label(frame_imagenes)
label_imagen_b.pack(side=tk.LEFT, padx=10)

# Label para mostrar imagen modificada
label_imagen_modificada = tk.Label(frame_imagenes)
label_imagen_modificada.pack(side=tk.LEFT, padx=10, pady=10)

# Scales para ajustar los valores RGB
scale_r = tk.Scale(ventana, from_=-255, to=255, orient=tk.HORIZONTAL, command=modificar_imagen)
scale_r.pack(pady=5)
scale_g = tk.Scale(ventana, from_=-255, to=255, orient=tk.HORIZONTAL, command=modificar_imagen)
scale_g.pack(pady=5)
scale_b = tk.Scale(ventana, from_=-255, to=255, orient=tk.HORIZONTAL, command=modificar_imagen)
scale_b.pack(pady=5)

# Crear el botón para establecer valores por defecto
boton_valores_por_defecto = tk.Button(ventana, text="Restaurar", command=establecer_valores_por_defecto)
boton_valores_por_defecto.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()

