#GRUPO F: Allauca Yadira, Armijos Thais
#euristica: numero de ubicaciones malas
estado_inicial=[
    [7, 2, 4],
    [5, 0, 6],
    [8, 3, 1]
]

estado_objetivo=[
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

def calculo_euristica(estado_actual):
    sum = 0
    #comparar cada una de las posiciones
    #si sin iguales 0
    #si no 1
    #devolver suma
    for i in range(len(estado_inicial)):
        for j in range(len(estado_inicial[0])):
            if estado_actual[i][j]==estado_objetivo[i][j]:
                sum+=0
            else:
                sum+=1
    
    return sum-1#de momento



def encontrar_cero(estado_actual):
    for i in range(len(estado_inicial)):
        for j in range(len(estado_inicial[0])):
            if estado_actual[i][j]==0:
                return [i,j]
            


#econtrar la posicion del 0
#en base a la posicion definir los hijos(movimientos posibles)
#si 0 esta en (1,1) -> 4 movimientos

def encontrar_solucion(estado_inicial):
    
    # Definir la estructura de los nodos del árbol de decisiones
    class Node:
        def __init__(self, g, h, estado):
            self.estado = estado
            self.g = g
            self.h = h
            self.f = g+h
            self.children = []

    #encontrar los sucesores 
    def enocontrar_sucesores(estado_actual, g):
        pos_cero = encontrar_cero(estado_actual)
        copia_arriba= [row[:] for row in estado_actual]
        copia_abajo =[row[:] for row in estado_actual]
        copia_izquierda = [row[:] for row in estado_actual]
        copia_derecha =[row[:] for row in estado_actual]
        
        movimientos = []

        #movimientos hacia arriba
        if pos_cero[0]>0:                
            numer_arriba=estado_actual[pos_cero[0]-1][pos_cero[1]]
            copia_arriba[pos_cero[0]-1][pos_cero[1]]=0
            copia_arriba[pos_cero[0]][pos_cero[1]]=numer_arriba
            movimientos.append(Node(g+1,calculo_euristica(copia_arriba),copia_arriba))

        #movimiento hacia abajo
        if pos_cero[0]<=1:
            numer_abajo=copia_abajo[pos_cero[0]+1][pos_cero[1]]
            copia_abajo[pos_cero[0]+1][pos_cero[1]]=0
            copia_abajo[pos_cero[0]][pos_cero[1]]=numer_abajo
            movimientos.append(Node(g+1,calculo_euristica(copia_arriba),copia_abajo))

        #movimiento hacia la izquierda
        if pos_cero[1]>=1:
            numer_izquierda=estado_actual[pos_cero[0]][pos_cero[1]-1]
            copia_izquierda[pos_cero[0]][pos_cero[1]-1]=0
            copia_izquierda[pos_cero[0]][pos_cero[1]]=numer_izquierda
            movimientos.append(Node(g+1,calculo_euristica(copia_arriba),copia_izquierda))

        #movimiento hacia la derecha
        if pos_cero[1]<=1:
            numer_derecha=estado_actual[pos_cero[0]][pos_cero[1]+1]
            copia_derecha[pos_cero[0]][pos_cero[1]+1]=0
            copia_derecha[pos_cero[0]][pos_cero[1]]=numer_derecha
            movimientos.append(Node(g+1,calculo_euristica(copia_arriba),copia_derecha))

        return movimientos

    # Inicializar con el nodo inicial
    
    node_inicial = Node(0, calculo_euristica(estado_inicial), estado_inicial)
    h_nodo = calculo_euristica(node_inicial.estado) 
    menor_nodo = node_inicial 

    while h_nodo != 0:
        menor_nodo.children = enocontrar_sucesores(estado_inicial,node_inicial.g)
        
        for i in range(len(menor_nodo.children)-1):
            if menor_nodo.children[i].f <= menor_nodo.children[i+1].f:
                nuevo_menor_nodo = menor_nodo.children[i]
        menor_nodo = nuevo_menor_nodo
        h_nodo = calculo_euristica(menor_nodo.estado)
    for row in menor_nodo.estado:
        print(row)
    return menor_nodo.estado


encontrar_solucion(estado_inicial)

    

    

        



