from collections import Counter
import random
import numpy as np

MAXIMO_ERRORES = 8
NUMERO_ESTADOS_INICIALES = 5
PROBABILIDAD_MUTACION = 15
cross_over = random.randint(0, 1)

poblacion_inicial = []
ruleta = [0]*100
ruleta_mutacion = [0]*100
correctos = []


#verificar si solo una ruleta o separadas
#generar ruleta para la mutación (ver función de llenar ruleta)
contador = 0
while(contador < 15):
  posicion = random.randint(0, 99)
  if ruleta_mutacion[posicion] == 0:
      ruleta_mutacion[posicion] = 1
      contador +=1
#print(ruleta_mutacion)
#print("Número de probabilidad de mutación = ",ruleta_mutacion.count(1))

estado_objetivo=np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
])

class Puzzle:
    def __init__(self, estado, heuristica, correctos):
        self.estado:np.array() = estado
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

ganador_p = 0
while ganador_p==0:
    ganador_p = girar_ruleta()
padre:Puzzle = poblacion_inicial[ganador_p-1]

ganador_m = 0
while ganador_m==0 and ganador_m==ganador_p:
    ganador_m = girar_ruleta()
madre:Puzzle = poblacion_inicial[ganador_m-1]

#separar padres ---> Falta hacer que se genere random
izq_madre = madre.estado[:, 0]
der_madre = madre.estado[:, 1:]
izq_padre = padre.estado[:, 0]
der_padre = padre.estado[:, 1:]

hijo_1 = np.concatenate((izq_madre[:, np.newaxis], der_padre), axis=1)
hijo_2 = np.concatenate((izq_padre[:, np.newaxis], der_madre), axis=1)

hijo_1 = corregir_hijo(hijo_1)
hijo_2 = corregir_hijo(hijo_2)

print(hijo_1)
print("-----------")
print(hijo_2)

#Decidir si clonar o no 
decision_clonar = ruleta_mutacion[random.randint(0, 99)]
#print(decision_clonar)
if(decision_clonar == 1):
    decision_hijo = random.randint(1,2)
    #print(decision_hijo)
    if decision_hijo == 1:
      hijo_mutado = [row[:] for row in hijo_1]
    else:
      hijo_mutado = [row[:] for row in hijo_2]
    #print(hijo_mutado)




