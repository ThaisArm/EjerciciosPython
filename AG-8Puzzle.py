from collections import Counter
import random
import numpy as np
#comentario
MAXIMO_ERRORES = 8
NUMERO_ESTADOS_INICIALES = 5
PROBABILIDAD_MUTACION = 15
cross_over = random.randint(0, 1)

poblacion_inicial = []
ruleta = [0]*100

estado_objetivo=np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
])

class Puzzle:
    def __init__(self, estado, heuristica, correctos):
        self.estado = estado
        self.heuristica = heuristica
        self.correctos = correctos
        self.probabilidad = 0

def calculo_euristica(estado_inicial):
    sum = 0
    for i in range(len(estado_inicial)):
        for j in range(len(estado_inicial[0])):
            if estado_inicial[i][j]==estado_objetivo[i][j]:
                sum+=0
            else:
                if estado_inicial[i][j] != 0:
                    sum+=1
    return sum 


#Zona de Ejecucion
#Generar estados iniciales
correctos = []
for i in range(NUMERO_ESTADOS_INICIALES):
    numeros = list(range(9))
    random.shuffle(numeros)

    estado_generado = np.array([[numeros.pop() for _ in range(3)] for _ in range(3)])
    heuristica_generado = calculo_euristica(estado_generado)
    correctos_generado = MAXIMO_ERRORES-heuristica_generado
    correctos.append(correctos_generado)
    poblacion_inicial.append(Puzzle(estado_generado, heuristica_generado,correctos_generado))

    for row in poblacion_inicial[i].estado:
        print(row)
    print("------------")

#Calcular probabilidad en base a la heuristicato
total_errores_iniciales = sum(correctos)
##corregir cuando sea 0
print("-----errores "+str(total_errores_iniciales))
for i in range(NUMERO_ESTADOS_INICIALES):
    poblacion_inicial[i].probabilidad = (poblacion_inicial[i].correctos/total_errores_iniciales)*100
    print(poblacion_inicial[i].probabilidad)
#falta redondear
#maybe crear un objeto con estado, heuristica y probabilidad 
indices_utilizados = set() 
for i in range(NUMERO_ESTADOS_INICIALES):
    numero_repetir = int(poblacion_inicial[i].probabilidad)
    for j in range(numero_repetir): 
        while True:
            indice = random.randint(0, 99) # Generar un número aleatorio entre 0 y 99
            if indice not in indices_utilizados:
                indices_utilizados.add(indice)
                ruleta[indice] = i+1
                break
#ubicar probabilidades 0
for i in range(NUMERO_ESTADOS_INICIALES):
    if int(poblacion_inicial[i].probabilidad) == 0:
        indice = random.randint(0, 99)
        ruleta[indice] = i+1

#definir padres
padre:Puzzle = poblacion_inicial[ruleta[random.randint(0, 99)]-1]
madre:Puzzle = poblacion_inicial[ruleta[random.randint(0, 99)]-1] #hacer que sea diferente

#Cruce
izq_madre = madre.estado[:, :2]
der_madre = madre.estado[:, :2]
izq_padre = padre.estado[:, :2]
der_padre = padre.estado[:, :2]

hijo_1 = np.concatenate(izq_madre, der_padre)

print("------------")
for row in hijo_1:
        print(row)

"""print("-------------------")
print(ruleta)

frecuencias = Counter(ruleta)

for elemento, frecuencia in frecuencias.items():
    if frecuencia >= 1:
        print("El elemento", elemento, "se repite", frecuencia, "veces.")

print("---------------Inicio iniciales")

frecuencias = Counter(ruleta)

for elemento, frecuencia in frecuencias.items():
    if frecuencia > 1:
        print("El elemento", elemento, "se repite", frecuencia, "veces.")"""
"""
maximo_errores = 9
1. Definir varios estados iniciales (5)
calcular euristica de todos(calcular numero de posiciones e1rroneas)
Seleccionar Padres
-> calcular heuristica
-> total_errores-heuristica
-> sumo resultados
-> calcular porsentaje de probabilidad con los resultados sobre la suma y x 100
-> rueda = arreglo de 100 posiciones
-> ubicar numero de estado de forma aleatoria en rueda en base al porcentaje ----- preguntar que pasa cuando la probabilidad = 0%
-> seleccionar una posicion randomica hasta obetener 2 resultados diferentes
-> esos 2 son los padres
->limpiar la rueda
Ejecutar Cruze
elegir random un numero de separacion entre cromosomas madre y padre
realizar el cruce
corregir numeros repetidos
Mutar los hijos
definir una probabilidad de mutacion 
llenar la rueba de acuerdo a la probabilidad
Cundo no muta
-> agrega los hijos a la poblacion inicial
cuando si muta
-> se elije randomicamente al hijo mutante
-> mutar: mover el 0 a una posicion random
-> se agregar el mutado y no mutado a la poblacion inicial
Eliminar los padres de la poblacion inicial
Volver a empezar
"""