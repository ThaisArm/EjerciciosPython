import random
import numpy as np

tamaño_poblacion=50
max_generaciones=200
dimension_matriz=3
crossover_point = random.randint(0, 1)
estado_objetivo=np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
])

# Definir la función de heuristica
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

def controlar_estado_repetido(madre, padre):
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
        if controlar_estado_repetido(estado_seleccionado1, estado_seleccionado2):
            poblacion_seleccionada.append(estado_seleccionado2)
            break
    """print(".... PRIMERO")
    print(poblacion_seleccionada[0])
    print("..................")
    print("....SEGUNDO")
    print(poblacion_seleccionada[1])"""
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
    tamaño_poblacion = len(poblacion)
    seleccion_size = int(0.25 * tamaño_poblacion) # Generar 25% para cada hijo
    
    #----ya entendi lo de aqui abajo pero te lo dejo por si acaso-> total lo que hice fue cambiar el metodo para que 
    #en lugar de seleccionar el 50% de optimos solo selccione los padres al azar 
    #v
    #v
    #poblacion_seleccionada = seleccion(poblacion, heuristica) #segun yo esta no sirve pero si le quito no encuentra resultado
    #segun entiendo lo que hace es de la poblacion original como que gira la rueda y genera una nueva poblacion con 
    #los que tienen mas probabilidades, con eso se va quedando con los mejores y de esos mejores escoger los padres
    #aunque no me queda claro que pasa si hay repetidos creo que eso no controla

    for i in range(seleccion_size):#le podemos explicar que es para acelerar el procesos en lugar de generar 2 hijos por iteracion generamos un 50%de hijos nuevos porque es 25% de cada hijo
        poblacion_seleccionada = seleccion(poblacion, heuristica)
        # falta controlar que no sean los mismo esto se hace en la funcion seleccion
        #padre = random.choice(poblacion_seleccionada)
        #madre = random.choice(poblacion_seleccionada)
        padre = poblacion_seleccionada[0]
        madre = poblacion_seleccionada[1]
        
        hijo1 = np.concatenate((padre[:crossover_point+1,:], madre[crossover_point+1:,:]), axis=0)
        hijo2 = np.concatenate((madre[:crossover_point+1,:], padre[crossover_point+1:,:]), axis=0)
        
        #hijo = np.vstack((padre[:crossover_point,:], madre[crossover_point:,:]))

        #corregir
        hijo1 = corregir_hijo(hijo1)
        hijo2 = corregir_hijo(hijo2)

        probabilidad_mutacion = 0.2 # Probabilidad de mutación

        #la mutacion no se maneja con el 0 selecciona 2 fichas al azar e intercambia su posicion
        #falta que seleccion un hijo al azar en lugar de solo seleccionar el hijo1
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
        #nueva_generacion.append(hijo)

    #nueva_generacion += poblacion_seleccionada[:tamaño_poblacion - seleccion_size*2]
    #aqui una vez que se llena con la nueva generacion con los hijos(50% esta lleno) se llena el otro 50% con el resto de la poblacion
    #eso entiendo yo si le entiendes mejor me explicas porfis
    nueva_generacion += poblacion[:tamaño_poblacion - seleccion_size*2]
    return nueva_generacion

# Algoritmo genético principal
def encontrar_solucion():
    #estado_objetivo = np.arange(dimension_matriz**2).reshape((dimension_matriz, dimension_matriz))
    poblacion = crear_poblacion_inicial(tamaño_poblacion)
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
            print(f"Solución encontrada en la generación {i}!")
            return poblacion[heuristica_valores.index(max_heuristica)]
        poblacion = crear_nueva_generacion(poblacion, heuristica_valores)
    print("Solución no encontrada.")
    return None

# Ejecutar el algoritmo genético con una población inicial de 300 individuos, un máximo de 300 generaciones y una matriz de 3x3
solution = encontrar_solucion()
print("Solución encontrada:\n", solution)
