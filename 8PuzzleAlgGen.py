from collections import Counter
import random
import numpy as np

MAXIMO_ERRORES = 8
NUMERO_ESTADOS_INICIALES = 5
PROBABILIDAD_MUTACION = 15
cross_over = random.randint(0, 1)

poblacion_inicial = []
ruleta = [0]*100
correctos = []

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
            if estado_inicial[i,j]!=estado_objetivo[i,j]:
                if estado_inicial[i,j] != 0:
                    sum+=1
    return sum 

def generar_estados_iniciales():
    muestra = []
    for i in range(NUMERO_ESTADOS_INICIALES):
        indices = np.random.permutation(9)
        estado_generado = np.reshape(indices, (3, 3))
        heuristica_generado = calculo_euristica(estado_generado)
        correctos_generado = MAXIMO_ERRORES-heuristica_generado
        correctos.append(correctos_generado)
        muestra.append(Puzzle(estado_generado, heuristica_generado,correctos_generado))
            
        for row in muestra[i].estado:
            print(row)
        print("------------")

    if sum(correctos) == 0:
        generar_estados_iniciales()
    else:
        return muestra

def calcular_probabilidad():
    total_errores_iniciales = sum(correctos)
    for i in range(NUMERO_ESTADOS_INICIALES):
        poblacion_inicial[i].probabilidad = int((poblacion_inicial[i].correctos/total_errores_iniciales)*100)
        print(poblacion_inicial[i].probabilidad)

def llenar_ruleta(nuevo_valor, numero_maximo):
    contador=numero_maximo
    for i in range(100):
        if ruleta[i] == 0 and contador != 0:
            ruleta[i] = nuevo_valor
            contador-=1

def girar_ruleta():
    return ruleta[random.randint(0, 99)]-1

poblacion_inicial = generar_estados_iniciales()
calcular_probabilidad()

for i in range(NUMERO_ESTADOS_INICIALES):
    if poblacion_inicial[i].probabilidad != 0:
        numero_casillas = poblacion_inicial[i].probabilidad
        llenar_ruleta(i+1,numero_casillas)
    else:
        if ruleta[99]==0:
            llenar_ruleta(i+1,1)
        else:
            ruleta[random.randint(0, 99)]=i+1

random.shuffle(ruleta)

ganador_p, ganador_m = 0
while ganador_p !=0:
    ganador_p = girar_ruleta()
padre:Puzzle = poblacion_inicial[ganador_p-1]

while ganador_m !=0 and ganador_m!= ganador_p:
    ganador_m = girar_ruleta()
madre:Puzzle = poblacion_inicial[ganador_m-1]



