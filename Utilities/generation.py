import random


def crossover(population, chance_to_breed):
    for mom, dad in population:
        if random.randint(1, 1 / chance_to_breed) == 1:
            cutoff = random.randint(0, len(mom))
            tmp = mom[:cutoff].copy()
            mom[:cutoff], dad[:cutoff] = dad[:cutoff], tmp
    return population
