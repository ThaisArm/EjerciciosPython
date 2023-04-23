import random
import numpy as np

# Definir la función de fitness
def fitness(individual, goal):
    fitness = 0
    for i in range(3):
        for j in range(3):
            if individual[i][j] == goal[i][j]:
                fitness += 1
    return fitness

# Crear una población inicial aleatoria
def create_population(population_size):
    population = []
    for i in range(population_size):
        individual = np.random.permutation(np.arange(9)).reshape((3, 3))
        population.append(individual)
    return population

# Seleccionar individuos para la siguiente generación
def selection(population, fitness):
    fitness_sum = sum(fitness)
    probabilities = [f/fitness_sum for f in fitness]
    selected_population = []
    for i in range(len(population)):
        selected_individual = random.choices(population, weights=probabilities)
        selected_population.append(selected_individual[0])
    return selected_population

# Crear una nueva generación a partir de la selección y cruce de individuos
def generate_new_generation(population, fitness):
    new_generation = []
    population_size = len(population)
    selection_size = int(0.5 * population_size) # Seleccionar el 50% de los mejores individuos
    selected_population = selection(population, fitness)
    for i in range(selection_size):
        parent1 = random.choice(selected_population)
        parent2 = random.choice(selected_population)
        crossover_point = random.randint(1, 7)
        child = np.vstack((parent1[:crossover_point,:], parent2[crossover_point:,:]))
        mutation_prob = 0.2 # Probabilidad de mutación
        if random.random() < mutation_prob:
            mutation_point1 = tuple(np.random.choice(3, size=2))
            mutation_point2 = tuple(np.random.choice(3, size=2))
            child[mutation_point1], child[mutation_point2] = child[mutation_point2], child[mutation_point1]
        new_generation.append(child)
    new_generation += selected_population[:population_size - selection_size]
    return new_generation

# Algoritmo genético principal
def genetic_algorithm(population_size, max_generations, matrix_size):
    goal = np.arange(matrix_size**2).reshape((matrix_size, matrix_size))
    population = create_population(population_size)
    for i in range(max_generations):
        fitness_values = [fitness(individual, goal) for individual in population]
        max_fitness = max(fitness_values)
        print(f"Generación {i}, Fitness máximo: {max_fitness}")
        if max_fitness == matrix_size**2:
            print(f"Solución encontrada en la generación {i}!")
            return population[fitness_values.index(max_fitness)]
        population = generate_new_generation(population, fitness_values)
    print("Solución no encontrada.")
    return None

# Ejecutar el algoritmo genético con una población inicial de 100 individuos, un máximo de 100 generaciones y una matriz de 3x3
solution = genetic_algorithm(population_size=100, max_generations=1000, matrix_size=3)
print("Solución encontrada:\n", solution)
