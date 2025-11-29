import random

# Parameters
POP_SIZE = 10
GENES_LENGTH = 6  # 6 bits → numbers 0 to 63
GENERATIONS = 16
MUTATION_RATE = 0.1

# Fitness function: linear growth
def fitness(individual):
    x = int("".join(map(str, individual)), 2)
    return x  # higher x = higher fitness

# Create a random individual
def create_individual():
    return [random.randint(0, 1) for _ in range(GENES_LENGTH)]

# Create initial population
def create_population():
    return [create_individual() for _ in range(POP_SIZE)]

# Selection (tournament)
def selection(population):
    selected = []
    for _ in range(POP_SIZE):
        i1, i2 = random.sample(population, 2)
        selected.append(i1 if fitness(i1) > fitness(i2) else i2)
    return selected

# Crossover
def crossover(parent1, parent2):
    point = random.randint(1, GENES_LENGTH - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutation
def mutate(individual):
    for i in range(GENES_LENGTH):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]
    return individual

# Genetic Algorithm
def genetic_algorithm():
    population = create_population()
    for generation in range(GENERATIONS):
        population = sorted(population, key=fitness, reverse=True)
        best = int("".join(map(str, population[0])), 2)
        print(f"Generation {generation} Best: {best} Fitness: {fitness(population[0])}")

        selected = selection(population)
        next_generation = []
        for i in range(0, POP_SIZE, 2):
            parent1 = selected[i]
            parent2 = selected[i+1]
            child1, child2 = crossover(parent1, parent2)
            next_generation.append(mutate(child1))
            next_generation.append(mutate(child2))
        population = next_generation

    best_individual = max(population, key=fitness)
    best_value = int("".join(map(str, best_individual)), 2)
    print(f"\nBest Solution: {best_value} -> Fitness = {fitness(best_individual)}")

# Run the algorithm
genetic_algorithm()
