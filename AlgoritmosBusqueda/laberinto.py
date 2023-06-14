from collections import deque
import random
import time
from collections import deque
import random
from memory_profiler import profile
from colorama import init, Fore

# Medir el tiempo de inicio
inicio = time.time()

#Funcion para buscar la posicion de la salida
def find_exit_possition(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[0][j] == 0:
                return (0,j)
            if maze[len(maze[0])-1][j]==0:
                return (len(maze[0])-1,j)
        if maze[i][0]==0:
            return (i,0)
        if maze[i][len(maze[0])-1]==0:
            return (i,len(maze[0])-1)

@profile
def find_exit_path(maze, start_pos):
            
    # Definir la posición de la salida
    exit_pos = find_exit_possition(maze)

    # Definir la estructura de los nodos del árbol de decisiones
    class Node:
        def __init__(self, pos, path):
            self.pos = pos
            self.path = path
            self.children = []

    # Definir la función para obtener los sucesores de un nodo
    def get_successors(node):
        successors = []
        row, col = node.pos

        # Movimiento hacia arriba
        if row > 0 and maze[row-1][col] == 0:
            pos = (row-1, col)
            path = node.path + [pos]
            successors.append(Node(pos, path))

        # Movimiento hacia abajo
        if row < len(maze) - 1 and maze[row+1][col] == 0:
            pos = (row+1, col)
            path = node.path + [pos]
            successors.append(Node(pos, path))

        # Movimiento hacia la izquierda
        if col > 0 and maze[row][col-1] == 0:
            pos = (row, col-1)
            path = node.path + [pos]
            successors.append(Node(pos, path))

        # Movimiento hacia la derecha
        if col < len(maze[0]) - 1 and maze[row][col+1] == 0:
            pos = (row, col+1)
            path = node.path + [pos]
            successors.append(Node(pos, path))

        return successors

    # Inicializar la cola FIFO con el nodo inicial
    start_node = Node(start_pos, [start_pos])
    queue = deque([start_node])

    # Mantener un conjunto de nodos visitados para evitar ciclos
    visited = set([start_pos])

    # Búsqueda en anchura
    while queue:
        # Tomar el siguiente nodo de la cola
        node = queue.popleft()

        # Comprobar si hemos llegado a la salida
        if node.pos == exit_pos:
            return node.path

        # Generar los sucesores del nodo actual
        successors = get_successors(node)

        # Añadir los sucesores a la cola si no han sido visitados antes
        for successor in successors:
            if successor.pos not in visited:
                node.children.append(successor)
                visited.add(successor.pos)
                queue.append(successor)

    # Si no se encontró la salida, devolver None
    return None

maze=[
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
[1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
[1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
[1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
[1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 0, 1, 1, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Definir la posición inicial del agente 
    #Encotrar las posciciones iniciales validas
def find_valid_star_pos(maze):
    zeros = []
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 0:
                zeros.append((i, j))
    return random.choice(zeros)

    # Seleccionar una posición inicial aleatoria entre las celdas con valor 0
start_pos = find_valid_star_pos(maze)

#encontrar una solucion
solution = find_exit_path(maze, start_pos)

# Medir el tiempo de finalización
final = time.time()
# Calcular la diferencia de tiempo
tiempo_total = final - inicio

# Inicializar colorama
init()

print("Posición inicial:", start_pos)
print("La solución es:", solution)

# Crear una copia de la matriz original
maze_copy = [row[:] for row in maze]

# Cambiar el color de los caracteres correspondientes a la solución en la copia
for i in range(len(solution)):
    row, col = solution[i]
    maze_copy[row][col] = Fore.GREEN + str(maze_copy[row][col]) + Fore.RESET

# Imprimir la matriz con la solución resaltada en rojo
for row in maze_copy:
    print(' '.join(str(col) for col in row))

print(f"El tiempo total de ejecución es: {tiempo_total} segundos.")
