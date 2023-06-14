import random

# Definir el laberinto
maze = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

# Definir la posición inicial del agente
start_pos = (random.randint(0, len(maze)-1), random.randint(0, len(maze[0])-1))

# Definir una función para crear un árbol de decisión a partir de una posición dada
def build_decision_tree(maze, current_pos, visited):
    tree = {current_pos: []}
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for move in moves:
        new_pos = (current_pos[0]+move[0], current_pos[1]+move[1])
        if new_pos[0] < 0 or new_pos[0] >= len(maze) or new_pos[1] < 0 or new_pos[1] >= len(maze[0]):
            continue
        if maze[new_pos[0]][new_pos[1]] == 0:
            continue
        if new_pos in visited:
            continue
        tree[current_pos].append(new_pos)
        visited.add(new_pos)
        sub_tree = build_decision_tree(maze, new_pos, visited)
        tree.update(sub_tree)
    return tree


# Definir una función para buscar la salida del laberinto utilizando búsqueda por profundidad
def dfs_search(tree, start):
    stack = [(start, [start])]
    visited = set()  # conjunto de nodos visitados
    while stack:
        (node, path) = stack.pop()
        if node not in tree or node in visited:  # si el nodo no está en el árbol o ya fue visitado, continuar
            continue
        visited.add(node)
        for neighbor in tree[node]:
            if neighbor == 'exit':
                return path + [neighbor]
            elif neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return None

# Construir el árbol de decisión
visited = set()
decision_tree = build_decision_tree(maze, start_pos, visited)

# Buscar la salida del laberinto utilizando búsqueda por profundidad
solution = dfs_search(decision_tree, start_pos)

# Imprimir la solución encontrada
print("Laberinto:")
for row in maze:
    print(row)
print("Posición inicial:", start_pos)
if solution:
    print("Solución encontrada:", solution)
else:
    print("No se encontró solución.")
