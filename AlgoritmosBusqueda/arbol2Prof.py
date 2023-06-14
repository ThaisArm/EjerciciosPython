import random
from queue import Queue

# Definir el laberinto
maze = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1],
]

# Definir la posición inicial del agente
start_pos = (random.randint(0, len(maze)-1), random.randint(0, len(maze[0])-1))

# Definir una función para crear un árbol de decisión a partir de una posición dada
def build_decision_tree(maze, current_pos):
    tree = {current_pos: []}
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for move in moves:
        new_pos = (current_pos[0]+move[0], current_pos[1]+move[1])
        if new_pos[0] < 0 or new_pos[0] >= len(maze) or new_pos[1] < 0 or new_pos[1] >= len(maze[0]):
            continue
        if maze[new_pos[0]][new_pos[1]] == 0:
            continue
        if new_pos in tree:
            continue
        tree[current_pos].append(new_pos)
        sub_tree = build_decision_tree(maze, new_pos)
        tree.update(sub_tree)
    return tree

# Definir una función para buscar la salida del laberinto utilizando búsqueda por profundidad
def bfs_search(tree, start):
    queue = Queue()
    visited = set()
    queue.put(start)
    visited.add(start)
    while not queue.empty():
        node = queue.get()
        if node not in tree:
            continue
        for neighbor in tree[node]:
            if neighbor == 'exit':
                return [start] + tree[node] + [neighbor]
            elif neighbor not in visited:
                queue.put(neighbor)
                visited.add(neighbor)
    return None

# Construir el árbol de decisión
decision_tree = build_decision_tree(maze, start_pos)

# Buscar la salida del laberinto utilizando búsqueda por profundidad
solution = bfs_search(decision_tree, start_pos)

# Imprimir la solución encontrada
print("Laberinto:")
for row in maze:
    print(row)
print("Posición inicial:", start_pos)
if solution:
    print("Solución encontrada:", solution)
else:
    print("No se encontró solución.")
