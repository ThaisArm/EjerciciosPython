from collections import Counter
import random
import numpy as np

MAXIMO_ERRORES = 8
NUMERO_ESTADOS_INICIALES = 5
PROBABILIDAD_MUTACION = 15
maxima_recursion = 500
cross_over = 0
ruleta = [0]*100
ruleta_mutacion = [0]*100
correctos = []
estado_objetivo=np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
])
estados_usados = ([])
class Puzzle:
    def __init__(self, estado, heuristica, correctos):
        self.estado:np.array() = estado
        self.heuristica = heuristica
        self.correctos = correctos
        self.probabilidad = 0

def encontrar_cero(estado_actual):
    for i in range(len(estado_actual)):
        for j in range(len(estado_actual[0])):
            if estado_actual[i][j]==0:
                return [i,j]
            
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
        for i in range(len(muestra)):
          estados_usados.append(muestra[i].estado)
        for row in muestra[i].estado:
            print(row)
        print("------------")

    if sum(correctos) == 0:
        generar_estados_iniciales()
    else:
        return muestra

def calcular_probabilidad(poblacion):
    total_errores_iniciales = sum(correctos)
    for i in range(len(poblacion)):
        poblacion[i].probabilidad = int((poblacion[i].correctos/total_errores_iniciales)*100)
        print(poblacion[i].probabilidad)

def llenar_ruleta(nuevo_valor, numero_maximo):
    contador=numero_maximo
    for i in range(100):
        if ruleta[i] == 0 and contador != 0:
            ruleta[i] = nuevo_valor
            contador-=1

def girar_ruleta(ruleta):
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
def comprobar_estado_objetivo(poblacion):
  for i in range(len(poblacion)):
    if np.all(poblacion[i].estado == estado_objetivo):
      return True
  return False
def mutar(hijo):
  hijo_mutado = Puzzle(estado = [], heuristica=0, correctos=[])
  hijo_mutado.estado = hijo.estado.copy()
  posicion_cero = encontrar_cero(hijo_mutado.estado)
  #Movimientos
  #movimientos hacia arriba
  if posicion_cero[0]>0:                
        numero_arriba=hijo_mutado.estado[posicion_cero[0]-1][posicion_cero[1]]
        hijo_mutado.estado[posicion_cero[0]-1][posicion_cero[1]]=0
        hijo_mutado.estado[posicion_cero[0]][posicion_cero[1]]=numero_arriba
      #movimiento hacia abajo
  if posicion_cero[0]<=1:
        numero_abajo=hijo_mutado.estado[posicion_cero[0]+1][posicion_cero[1]]
        hijo_mutado.estado[posicion_cero[0]+1][posicion_cero[1]]=0
        hijo_mutado.estado[posicion_cero[0]][posicion_cero[1]]=numero_abajo
      #movimiento hacia la izquierda
  if posicion_cero[1]>=1:
        numero_izquierda=hijo_mutado.estado[posicion_cero[0]][posicion_cero[1]-1]
        hijo_mutado.estado[posicion_cero[0]][posicion_cero[1]-1]=0
        hijo_mutado.estado[posicion_cero[0]][posicion_cero[1]]=numero_izquierda
      #movimiento hacia la derecha
  if posicion_cero[1]<=1:
        numero_derecha=hijo_mutado.estado[posicion_cero[0]][posicion_cero[1]+1]
        hijo_mutado.estado[posicion_cero[0]][posicion_cero[1]+1]=0
        hijo_mutado.estado[posicion_cero[0]][posicion_cero[1]]=numero_derecha
  print(hijo_mutado.estado)
  return hijo_mutado
#comprobar estado_usado
def comprobar_estado_usado(hijo):
  if np.array_equal(hijo.estado, estados_usados):
      return True
  return False
def comprobar_estado_usado_correcion(estado):
  if np.array_equal(estado, estados_usados):
      return True
  return False
#FUNCION
def encontrar_solucion(poblacion_inicial):
    if(comprobar_estado_objetivo(poblacion_inicial)):
        return poblacion_inicial
    calcular_probabilidad(poblacion)
    for i in range(len(poblacion_inicial)):
      ruleta = [0]*100
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
      ganador_p = girar_ruleta(ruleta)
    padre:Puzzle = poblacion_inicial[ganador_p-1]
    ganador_m = 0
    while ganador_m==0 and ganador_m==ganador_p:
      ganador_m = girar_ruleta(ruleta)
    madre:Puzzle = poblacion_inicial[ganador_m-1]
    izq_madre = madre.estado[:, :cross_over+1]
    izq_padre = padre.estado[:, :cross_over+1]
    der_madre = madre.estado[:, cross_over+1:]
    der_padre = padre.estado[:, cross_over+1:]
    hijo_1 = Puzzle(estado=np.concatenate((izq_madre, der_padre), axis=1), heuristica=0, correctos=[])
    hijo_2= Puzzle(estado=np.concatenate((izq_padre, der_madre), axis=1), heuristica=0, correctos=[])
    print("MADRE")
    print(madre.estado)
    print("PADRE")
    print(padre.estado)
    print("HIJO")
    print(hijo_1.estado)
    print("HIJO2")
    print(hijo_2.estado)
    hijo_1.estado = corregir_hijo(hijo_1.estado)
    hijo_2.estado = corregir_hijo(hijo_2.estado)
    print("HIJO")
    print(hijo_1.estado)
    print("HIJO2")
    print(hijo_2.estado)
    #Decidir si mutar o no 
    decision_mutar = ruleta_mutacion[random.randint(0, 99)]
    print(decision_mutar)
    hijo_mutado = Puzzle(estado = [], heuristica=0, correctos=[])
    if(decision_mutar == 1):
      #decidir hijo a mutar
      decision_hijo = random.randint(1,2)
      print("Hijo a mutar: ",decision_hijo)
      if decision_hijo == 1:
        hijo_mutado = mutar(hijo_1)
      else:
        hijo_mutado = mutar(hijo_2)   
    #Eliminar estados padres, agregar los hijos
    if(len(hijo_mutado.estado) != 0):
      if(decision_hijo == 1):
        hijo_1 = hijo_mutado
        while comprobar_estado_usado_correcion(hijo_mutado.estado):
          hijo_1 = hijo_mutado 
      else:
        hijo_2 = hijo_mutado
        while comprobar_estado_usado_correcion(hijo_mutado.estado):
          hijo_2 = hijo_mutado  

    #se eliminan todos los elementos? 
    poblacion_inicial.clear()
    hijo_1.heuristica = calculo_euristica(hijo_1.estado)
    hijo_1.correctos = MAXIMO_ERRORES-hijo_1.heuristica
    correctos.append(hijo_1.correctos)
    estados_usados.append(hijo_1.estado)
    hijo_2.heuristica = calculo_euristica(hijo_2.estado)
    hijo_2.correctos = MAXIMO_ERRORES-hijo_2.heuristica
    correctos.append(hijo_2.correctos)
    estados_usados.append(hijo_2.estado)
    poblacion_inicial.extend([hijo_1, hijo_2])
    #print("POBLACION")
    #for i in range(len(poblacion_inicial)):
    #  print(poblacion_inicial[i].estado)
    global maxima_recursion
    if comprobar_estado_objetivo(poblacion_inicial):
      print("POBLACION")
      for i in range(len(poblacion_inicial)):
        print(poblacion_inicial[i].estado)
      return
    else:
      maxima_recursion-=1
      encontrar_solucion(poblacion_inicial)

#EJECUCIÓN-----
poblacion = generar_estados_iniciales()
encontrar_solucion(poblacion)
#print(estados_usados)
