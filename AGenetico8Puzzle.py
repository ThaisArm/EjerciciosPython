import random
import numpy as np

tamanio_poblacion=50
max_generaciones=200
dimension_matriz=3
crossover_point = random.randint(0, 1)
estado_objetivo=np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
])

# Definir la función de heurística
def heuristica(estado):
    heuristica = 0
    for i in range(3):
        for j in range(3):
            if estado[i][j] == estado_objetivo[i][j]:
                heuristica += 1
    return heuristica

# Crear una población inicial aleatoria
def crear_poblacion_inicial(tamaño_poblacion):
    poblacion_inicial = []
    for i in range(tamaño_poblacion):
        estado = np.random.permutation(np.arange(9)).reshape((3, 3))
        poblacion_inicial.append(estado)
    return poblacion_inicial

def controlar_estado_seleccion(madre, padre):
    for i in range(3):
        for j in range(3):
            if madre[i][j] != padre[i][j]:
                return True
    return False

# Seleccionar individuos para la siguiente generación
def seleccion(poblacion, heuristica):
    heuristica_sum = sum(heuristica)
    probabilidad = [f/heuristica_sum for f in heuristica]
    poblacion_seleccionada = []
    
    # Seleccionar primer estado
    estado_seleccionado1 = random.choices(poblacion, weights=probabilidad)[0]
    poblacion_seleccionada.append(estado_seleccionado1)
    
    # Seleccionar segundo estado 
    while True:
        estado_seleccionado2 = random.choices(poblacion, weights=probabilidad)[0]
        if controlar_estado_seleccion(estado_seleccionado1, estado_seleccionado2):
            poblacion_seleccionada.append(estado_seleccionado2)
            break
    return poblacion_seleccionada

def corregir_hijo(estado):
    numeros_faltantes = set(range(9))
    for i in range(len(estado)):
        for j in range(len(estado[0])):
            numero = estado[i, j]
            if numero in numeros_faltantes:
                numeros_faltantes.remove(numero)
            else:
                nuevo_numero = numeros_faltantes.pop()
                estado[i, j] = nuevo_numero
    return estado

# Crear una nueva generación a partir de la selección y cruce de individuos
def crear_nueva_generacion(poblacion, heuristica):
    nueva_generacion = []
    tamanio_poblacion = len(poblacion)
    seleccion_size = int(0.25 * tamanio_poblacion) # Generar 25% para cada hijo
    
    for i in range(seleccion_size):
        poblacion_seleccionada = seleccion(poblacion, heuristica)
        padre = poblacion_seleccionada[0]
        madre = poblacion_seleccionada[1]
        
        hijo1 = np.concatenate((padre[:crossover_point+1,:], madre[crossover_point+1:,:]), axis=0)
        hijo2 = np.concatenate((madre[:crossover_point+1,:], padre[crossover_point+1:,:]), axis=0)

        #corregir
        hijo1 = corregir_hijo(hijo1)
        hijo2 = corregir_hijo(hijo2)

        probabilidad_mutacion = 0.2 # Probabilidad de mutación

        if random.random() < probabilidad_mutacion:
            mutation_point1 = tuple(np.random.choice(3, size=2))
            mutation_point2 = tuple(np.random.choice(3, size=2))
            hijo_a_mutar = random.randint(1,2)
            if hijo_a_mutar == 1:
                hijo1[mutation_point1], hijo1[mutation_point2] = hijo1[mutation_point2], hijo1[mutation_point1]
                hijo1 = corregir_hijo(hijo1)
            else:
                hijo2[mutation_point1], hijo2[mutation_point2] = hijo2[mutation_point2], hijo2[mutation_point1]
                hijo2 = corregir_hijo(hijo2)

        nueva_generacion.append(hijo1)
        nueva_generacion.append(hijo2)

    nueva_generacion += poblacion[:tamanio_poblacion - seleccion_size*2]
    return nueva_generacion

# Algoritmo genético principal
def encontrar_solucion():
    poblacion = crear_poblacion_inicial(tamanio_poblacion)
    for i in range(max_generaciones):
        heuristica_valores = [heuristica(estado) for estado in poblacion]
        max_heuristica = max(heuristica_valores)
        print(f"Generación {i}, heuristica máximo: {max_heuristica}")
        #for estado in poblacion:
        #    for row in estado:
        #        print(row)
        #    print("-----")
        #print(".........................")
        if max_heuristica == dimension_matriz**2:
            print(f"Solución encontrada en la generación {i}")
            return poblacion[heuristica_valores.index(max_heuristica)]
        poblacion = crear_nueva_generacion(poblacion, heuristica_valores)
    print("Solución no encontrada.")
    return None

# Ejecutar el algoritmo genético con una población inicial de 300 individuos, un máximo de 300 generaciones y una matriz de 3x3
solution = encontrar_solucion()
print("Solución encontrada:\n", solution)
