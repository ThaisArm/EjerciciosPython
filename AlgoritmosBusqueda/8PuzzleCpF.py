from collections import Counter
import random
import numpy as np

MAXIMO_ERRORES = 8
NUMERO_ESTADOS_INICIALES = 5
PROBABILIDAD_MUTACION = 15
cross_over = random.randint(0, 1)
ruleta_mutacion = [0]*100
ruleta = [0]*100
maxima_profundidad = 600
#Por qué el arreglo de correctos?
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
        """for row in muestra[i].estado:
            print(row)
        print("------------")"""
    if sum(correctos) == 0:
        generar_estados_iniciales()
    else:
        return muestra

def encontrar_posicion_cero(estado_actual):
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

#verificar si solo una ruleta o separadas?
#generar ruleta para la mutación (ver si se puede unir a la función de llenar ruleta)
contador = 0
while(contador < PROBABILIDAD_MUTACION):
  posicion = random.randint(0, 99)
  if ruleta_mutacion[posicion] == 0:
      ruleta_mutacion[posicion] = 1
      contador +=1
print(ruleta_mutacion)
print("Número de probabilidad de mutación = ",ruleta_mutacion.count(1))

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

def comprobar_estado_objetivo(poblacion):
  for i in range(len(poblacion)):
    if np.all(poblacion[i].estado == estado_objetivo):
      return True
  return False

def comprobar_estado_usado(estado):
  if np.array_equal(estado, estados_usados):
      return True
  return False

def mutar(hijo):
    hijo_mutado = Puzzle(estado=[], heuristica=0, correctos=[])
    hijo_mutado.estado = hijo.estado.copy()
    posicion_cero = encontrar_posicion_cero(hijo_mutado.estado)
    contador_movimientos = 0  # contador de movimientos realizados
    ultimo_movimiento = None  # registro del último movimiento realizado

    while contador_movimientos <= MAXIMO_ERRORES:  # realizar 8 movimientos
        # Movimientos
        movimientos_disponibles = []  # lista de movimientos disponibles
        # movimiento hacia arriba
        if posicion_cero[0] > 0 and ultimo_movimiento != "abajo":
            movimientos_disponibles.append("arriba")
        # movimiento hacia abajo
        if posicion_cero[0] < 2 and ultimo_movimiento != "arriba":
            movimientos_disponibles.append("abajo")
        # movimiento hacia la izquierda
        if posicion_cero[1] > 0 and ultimo_movimiento != "derecha":
            movimientos_disponibles.append("izquierda")
        # movimiento hacia la derecha
        if posicion_cero[1] < 2 and ultimo_movimiento != "izquierda":
            movimientos_disponibles.append("derecha")

        # verificar si hay movimientos disponibles
        if not movimientos_disponibles:
            break  # no se pueden realizar más movimientos

        # seleccionar un movimiento aleatorio de la lista de movimientos disponibles
        movimiento_seleccionado = random.choice(movimientos_disponibles)

        # actualizar el registro del último movimiento
        ultimo_movimiento = movimiento_seleccionado

        # realizar el movimiento seleccionado
        if movimiento_seleccionado == "arriba":
            numero_arriba = hijo_mutado.estado[posicion_cero[0]-1][posicion_cero[1]]
            hijo_mutado.estado[posicion_cero[0]-1][posicion_cero[1]] = 0
            hijo_mutado.estado[posicion_cero[0]][posicion_cero[1]] = numero_arriba
            posicion_cero[0] -= 1  # actualizar la posición del cero
        elif movimiento_seleccionado == "abajo":
            numero_abajo = hijo_mutado.estado[posicion_cero[0]+1][posicion_cero[1]]
            hijo_mutado.estado[posicion_cero[0]+1][posicion_cero[1]] = 0
            hijo_mutado.estado[posicion_cero[0]][posicion_cero[1]] = numero_abajo
            posicion_cero[0] += 1  # actualizar la posición del cero
        elif movimiento_seleccionado == "izquierda":
            numero_izquierda = hijo_mutado.estado[posicion_cero[0]][posicion_cero[1]-1]
            hijo_mutado.estado[posicion_cero[0]][posicion_cero[1]-1] = 0
            hijo_mutado.estado[posicion_cero[0]][posicion_cero[1]] = numero_izquierda
            posicion_cero[1] -= 1  # actualizar la posición del cero
        elif movimiento_seleccionado == "derecha":
            numero_derecha = hijo_mutado.estado[posicion_cero[0]][posicion_cero[1]+1]
            hijo_mutado.estado[posicion_cero[0]][posicion_cero[1]+1]
            hijo_mutado.estado[posicion_cero[0]][posicion_cero[1]] = numero_derecha
            posicion_cero[1] += 1  # actualizar la posición del cero
        contador_movimientos += 1  # incrementar el contador de movimientos realizados
    print(hijo_mutado.estado)
    return hijo_mutado


def encontrar_solucion(poblacion_inicial):
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
    #print(ruleta)

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
    print("Decisión mutación: ",decision_mutar)
    hijo_mutado = Puzzle(estado = [], heuristica=0, correctos=[])
    if(decision_mutar == 1):
      #decidir hijo a mutar
      decision_hijo = random.randint(1,2)
      print("Hijo a mutar: ",decision_hijo)
      if decision_hijo == 1:
          hijo_mutado = mutar(hijo_1)
      else:
        hijo_mutado = mutar(hijo_2)   
#   Eliminar estados padres, agregar los hijos
    if(len(hijo_mutado.estado) != 0):
        if(decision_hijo == 1):
          hijo_1 = hijo_mutado
          """ while comprobar_estado_usado(hijo_mutado.estado):
          hijo_1 = hijo_mutado""" 
        else:
          hijo_2 = hijo_mutado
        """while comprobar_estado_usado(hijo_mutado.estado):
          hijo_2 = hijo_mutado  """

    #se eliminan todos los elementos???
    a = ganador_p-1
    b = ganador_m-1
    poblacion_inicial.pop(a)
    poblacion_inicial.pop(b)
    hijo_1.heuristica = calculo_euristica(hijo_1.estado)
    hijo_1.correctos = MAXIMO_ERRORES-hijo_1.heuristica
    correctos.append(hijo_1.correctos)
    estados_usados.append(hijo_1.estado)
    hijo_2.heuristica = calculo_euristica(hijo_2.estado)
    hijo_2.correctos = MAXIMO_ERRORES-hijo_2.heuristica
    correctos.append(hijo_2.correctos)
    estados_usados.append(hijo_2.estado)
    poblacion_inicial.extend([hijo_1, hijo_2])
    global maxima_profundidad
    if comprobar_estado_objetivo(poblacion_inicial) or maxima_profundidad==0:
      print("POBLACION")
      for i in range(len(poblacion_inicial)):
        print(poblacion_inicial[i].estado, "HEURÍSTICA =", poblacion_inicial[i].heuristica)
      return
    else:
      maxima_profundidad -= 1
      encontrar_solucion(poblacion_inicial)

#EJECUCIÓN-----
poblacion = generar_estados_iniciales()
#try:  
encontrar_solucion(poblacion)
#except:
#  print("----NO HAY SOLUCIÓN-----")

