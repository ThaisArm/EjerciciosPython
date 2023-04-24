#analiza el primer nodo
#genera los hijos
#guarda las hojas en un arreglo
#calcula la euristica de los miembros del arreglo
#calcula la funcion objetivo
#encuentra el hijo mas optimo
#saca a ese hijo de la lista de hojas

#GRUPO F: Allauca Yadira, Armijos Thais
#euristica: numero de ubicaciones malas
estado_inicial_0=[
    [7, 2, 4],
    [5, 0, 6],
    [8, 3, 1]
]

estado_inicial=[
    [1, 2, 5],
    [7, 6, 4],
    [3, 8, 0]
]

estado_objetivo=[
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

nodos_hoja=[]

class Nodo:
        def __init__(self, g, h, estado):
            self.estado = estado
            self.g = g
            self.h = h
            self.f = g+h
            self.children = []

def calculo_euristica(estado_actual):
    sum = 0
    for i in range(len(estado_inicial)):
        for j in range(len(estado_inicial[0])):
            if estado_actual[i][j]==estado_objetivo[i][j]:
                sum+=0
            else:
                sum+=1
    return sum  

def encontrar_cero(estado_actual):
    for i in range(len(estado_inicial)):
        for j in range(len(estado_inicial[0])):
            if estado_actual[i][j]==0:
                return [i,j]

def generar_hijos(nodo:Nodo):
    estado_actual = nodo.estado
    pos_cero = encontrar_cero(estado_actual)

    copia_arriba= [row[:] for row in estado_actual]
    copia_abajo =[row[:] for row in estado_actual]
    copia_izquierda = [row[:] for row in estado_actual]
    copia_derecha =[row[:] for row in estado_actual]

    hijos = []

    #movimientos hacia arriba
    if pos_cero[0]>0:                
        numer_arriba=estado_actual[pos_cero[0]-1][pos_cero[1]]
        copia_arriba[pos_cero[0]-1][pos_cero[1]]=0
        copia_arriba[pos_cero[0]][pos_cero[1]]=numer_arriba
        hijos.append(Nodo(nodo.g+1,calculo_euristica(copia_arriba),copia_arriba))

    #movimiento hacia abajo
    if pos_cero[0]<=1:
        numer_abajo=copia_abajo[pos_cero[0]+1][pos_cero[1]]
        copia_abajo[pos_cero[0]+1][pos_cero[1]]=0
        copia_abajo[pos_cero[0]][pos_cero[1]]=numer_abajo
        hijos.append(Nodo(nodo.g+1,calculo_euristica(copia_abajo),copia_abajo))

    #movimiento hacia la izquierda
    if pos_cero[1]>=1:
        numer_izquierda=estado_actual[pos_cero[0]][pos_cero[1]-1]
        copia_izquierda[pos_cero[0]][pos_cero[1]-1]=0
        copia_izquierda[pos_cero[0]][pos_cero[1]]=numer_izquierda
        hijos.append(Nodo(nodo.g+1,calculo_euristica(copia_izquierda),copia_izquierda))

    #movimiento hacia la derecha
    if pos_cero[1]<=1:
        numer_derecha=estado_actual[pos_cero[0]][pos_cero[1]+1]
        copia_derecha[pos_cero[0]][pos_cero[1]+1]=0
        copia_derecha[pos_cero[0]][pos_cero[1]]=numer_derecha
        hijos.append(Nodo(nodo.g+1,calculo_euristica(copia_derecha),copia_derecha))

    return hijos

def hallar_solucion(nodo:Nodo):
    print(" ")
    print("----------------------------")
    print(str(encontrar_cero(nodo.estado))+"g:"+str(nodo.g)+"h:"+str(nodo.h)+"f:"+str(nodo.f))
    if nodo.h !=0:
        hijos_nodo_optimo = generar_hijos(nodo)

        for hijo in hijos_nodo_optimo:
            print(str(encontrar_cero(hijo.estado))+"g:"+str(hijo.g)+"h:"+str(hijo.h)+"f:"+str(hijo.f)+"...",end=" ")
            if isinstance(hijo, Nodo):
                nodos_hoja.append(hijo)
                #print(encontrar_cero(hijo.estado))
                #print(hijo.f)
                #print("^ es hijo")

        nodo_optimo:Nodo = nodos_hoja[0]

        for hoja in nodos_hoja:
            if isinstance(hoja, Nodo):
                if hoja.f <= nodo_optimo.f:
                    nodo_optimo = hoja

        nodos_hoja.remove(nodo_optimo)
        #print(len(nodos_hoja))
        #print("^ hojas")
        #print(len(nodos_padre))
        #print("^ padres")
        #print("-----------------------")
        #print(encontrar_cero(nodo_optimo.estado))
        #print(nodo_optimo.f)
        #print("^ nuevo 0")
                
        nodo = hallar_solucion(nodo_optimo)

    return nodo

nodo_inicial = Nodo(0,calculo_euristica(estado_inicial),estado_inicial)

for row in hallar_solucion(nodo_inicial).estado:
        print(row)
#print(hallar_solucion(nodo_inicial).estado)

