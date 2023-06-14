import random

# Calcular la heurística
def calcular_heuristica(puzzle):
    estado_objetivo = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    heuristica = 0
    for i in range(len(puzzle)):
        if puzzle[i] == estado_objetivo[i]:
            heuristica += 1
    return heuristica

# Población inicial aleatoria
def generar_poblacion_inicial(tamanio):
    poblacion = []
    for i in range(tamanio):
        puzzle = list(range(9))
        random.shuffle(puzzle)
        poblacion.append(puzzle)
    return poblacion

# Seleccionar candidatos a padres
def seleccion(poblacion, heuristica):
    heuristica_sum = sum(heuristica)
    probabilidades = [h/heuristica_sum for h in heuristica]
    poblacion_seleccionada = []
    for i in range(len(poblacion)):
        candidato = random.choices(poblacion, weights=probabilidades)
        poblacion_seleccionada.append(candidato[0])
    return poblacion_seleccionada

# Cruzar padres
def generar_nueva_generacion(poblacion, heuristica):
    nueva_generacion= []
    poblacion_tamanio = len(poblacion)
    tamanio_seleccion = int(0.5 * poblacion_tamanio) # Seleccionar el 50% de los mejores individuos
    poblacion_seleccionada = seleccion(poblacion,heuristica)
    for i in range(tamanio_seleccion):
        padre = random.choice(poblacion_seleccionada)
        madre = random.choice(poblacion_seleccionada)
        crossover = random.randint(1, 7)
        hijo = padre[:crossover] + madre[crossover:]
        mutacion_prob = 0.15 # Probabilidad de mutación
        if random.random() < mutacion_prob:
            mutacion_1 = random.randint(0, 7)
            mutacion_2 = random.randint(0, 7)
            hijo[mutacion_1], hijo[mutacion_2] = hijo[mutacion_2], hijo[mutacion_1]
        nueva_generacion.append(hijo)
    nueva_generacion += poblacion_seleccionada[:poblacion_tamanio - tamanio_seleccion]
    return nueva_generacion

# Solución
def resolver_puzzle(poblacion_tamanio, num_generaciones):
    poblacion = generar_poblacion_inicial(poblacion_tamanio)
    for i in range(num_generaciones):
        heuristica_val = [calcular_heuristica(puzzle) for puzzle in poblacion]
        max_heuristica = max(heuristica_val)
        if max_heuristica == 9:
            print(f"Solución encontrada en la generación {i}")
            for j in range(len(poblacion)):
              print(poblacion[j])
            return poblacion[heuristica_val.index(max_heuristica)]
        poblacion = generar_nueva_generacion(poblacion, heuristica_val)
    print("Solución no encontrada.")
    return None

# Ejecutar
solucion= resolver_puzzle(poblacion_tamanio=100, num_generaciones=100)
print("Solución encontrada:", solucion)
