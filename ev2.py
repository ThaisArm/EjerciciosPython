#busqueda en Profundidad

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

def agregar_hijos(nodo:Nodo):
    path = nodo.path + [nodo.valor]
    if nodo.valor < 15:
        nodo.children.append(Nodo(nodo.valor*2, nodo, path))
        nodo.children.append(Nodo(nodo.valor*2+1, nodo, path))

def resolver_profundidad(estado_incial, destino):
    pila = [estado_incial]
    visitados = set()
    while pila:
        nodo = pila.pop()
        if nodo.valor == destino:
            return nodo
        if nodo.valor not in visitados:
            visitados.add(nodo.valor)
            agregar_hijos(nodo)
            for child in nodo.children[::-1]:
                if evaluar_hijos(child, destino):
                    pila.append(child)


estado_0 = Nodo(1, None, [0])
solucion = resolver_profundidad(estado_0, 15)
print(solucion.path + [solucion.valor])

