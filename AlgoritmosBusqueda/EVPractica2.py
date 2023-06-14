#Pregunta 2 practica
#Primero en Anchura

class Nodo:
    def __init__(self, valor, dad, path):
        self.valor = valor
        self.path = path
        self.dad = dad
        self.children = []

def evaluar_hijos(nodo:Nodo, destino):
    for i in range(len(nodo.children)):
        if nodo.children[i].valor == destino:
            return False
    return True

def agregar_hijos_p(nodo:Nodo):
    path = nodo.path + [nodo.valor]
    if nodo.valor < 15:
        nodo.children.append(Nodo(nodo.valor*2, nodo, path))
        nodo.children.append(Nodo(nodo.valor*2+1, nodo, path))

def agregar_hijos_a(nodo:Nodo, cola: list):
    path = nodo.path + [nodo.valor]
    if nodo.valor < 15:
        nodo.children.append(Nodo(nodo.valor*2, nodo, path))
        nodo.children.append(Nodo(nodo.valor*2+1, nodo, path))
    cola.extend(nodo.children)

def agregar_hijos_iter(nodo:Nodo, pila: list):
    path = nodo.path + [nodo.valor]
    if nodo.valor < 15:
        nodo.children.append(Nodo(nodo.valor*2, nodo, path))
        nodo.children.append(Nodo(nodo.valor*2+1, nodo, path))
    pila.extend(nodo.children[::-1])

def resolver_anchura(estado_incial, destino):
    cola = [estado_incial]
    visitados = set()
    while cola:
        nodo = cola.pop(0)
        if nodo.valor == destino:
            return nodo
        if nodo.valor not in visitados:
            #print(nodo.path+[nodo.valor])
            visitados.add(nodo.valor)
            agregar_hijos_a(nodo, cola)
            cola = [nodo for nodo in cola if evaluar_hijos(nodo, destino)]
            


def resolver_profundidad(estado_incial, destino):
    pila = [estado_incial]
    visitados = set()
    while pila:
        nodo = pila.pop()
        if nodo.valor == destino:
            return nodo
        if nodo.valor not in visitados:
            #print(nodo.path+[nodo.valor])
            visitados.add(nodo.valor)
            agregar_hijos_p(nodo)
            for child in nodo.children[::-1]:
                if evaluar_hijos(child, destino):
                    pila.append(child)

#profundidad iterativa

def resolver(estado_incial, destino, limite):
    pila = [estado_incial]
    visitados = set()
    while pila:
        nodo = pila.pop()        
        if nodo.valor == destino:
            return nodo
        if nodo.valor not in visitados and len(nodo.path) < limite:
            #print(nodo.path+[nodo.valor])
            visitados.add(nodo.valor)
            agregar_hijos_iter(nodo, pila)
    return None

def resolver_iterativo(estado_inicial, destino):
    limite = 0
    while True:
        solucion = resolver(estado_inicial, destino, limite)
        if solucion:
            return solucion
        limite += 1

estado_0 = Nodo(1, None, [])
print("anchura")
solucion = resolver_anchura(estado_0, 15)
print(solucion.path + [solucion.valor])
print("profundidad")
solucion = resolver_profundidad(estado_0, 15)
print(solucion.path + [solucion.valor])
print("iterativo")
solucion = resolver_iterativo(estado_0, 15)
print(solucion.path + [solucion.valor])

