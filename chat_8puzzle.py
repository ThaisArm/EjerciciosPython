import random
import numpy as np

tamaño_poblacion=300
max_generaciones=300
dimension_matriz=3

estado_objetivo=np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
])

# Definir la función de heuristica
def heuristica(estado, estado_objetivo):
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

# Seleccionar individuos para la siguiente generación
def seleccion(poblacion, heuristica):
    heuristica_sum = sum(heuristica)
    probabilidad = [f/heuristica_sum for f in heuristica]
    poblacion_seleccionada = []
    for i in range(len(poblacion)):
        estado_seleccionado = random.choices(poblacion, weights=probabilidad)
        poblacion_seleccionada.append(estado_seleccionado[0])
    return poblacion_seleccionada

# Crear una nueva generación a partir de la selección y cruce de individuos
def crear_nueva_generacion(poblacion, heuristica):
    nueva_generacion = []
    tamaño_poblacion = len(poblacion)
    seleccion_size = int(0.5 * tamaño_poblacion) # Seleccionar el 50% de los mejores individuos
    poblacion_seleccionada = seleccion(poblacion, heuristica)
    for i in range(seleccion_size):
        padre = random.choice(poblacion_seleccionada)
        madre = random.choice(poblacion_seleccionada)
        crossover_point = random.randint(1, 7)
        hijo = np.vstack((padre[:crossover_point,:], madre[crossover_point:,:]))
        probabilidad_mutacion = 0.2 # Probabilidad de mutación
        if random.random() < probabilidad_mutacion:
            mutation_point1 = tuple(np.random.choice(3, size=2))
            mutation_point2 = tuple(np.random.choice(3, size=2))
            hijo[mutation_point1], hijo[mutation_point2] = hijo[mutation_point2], hijo[mutation_point1]
        nueva_generacion.append(hijo)
    nueva_generacion += poblacion_seleccionada[:tamaño_poblacion - seleccion_size]
    return nueva_generacion

# Algoritmo genético principal
def encontrar_solucion():
    #estado_objetivo = np.arange(dimension_matriz**2).reshape((dimension_matriz, dimension_matriz))
    poblacion = crear_poblacion_inicial(tamaño_poblacion)
    for i in range(max_generaciones):
        heuristica_valores = [heuristica(estado, estado_objetivo) for estado in poblacion]
        max_heuristica = max(heuristica_valores)
        print(f"Generación {i}, heuristica máximo: {max_heuristica}")
        #for estado in poblacion:
        #    for row in estado:
        #        print(row)
        #    print("-----")
        #print(".........................")
        if max_heuristica == dimension_matriz**2:
            print(f"Solución encontrada en la generación {i}!")
            return poblacion[heuristica_valores.index(max_heuristica)]
        poblacion = crear_nueva_generacion(poblacion, heuristica_valores)
    print("Solución no encontrada.")
    return None

# Ejecutar el algoritmo genético con una población inicial de 100 individuos, un máximo de 100 generaciones y una matriz de 3x3
solution = encontrar_solucion()
print("Solución encontrada:\n", solution)
