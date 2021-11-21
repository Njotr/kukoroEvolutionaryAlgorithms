import random
import numpy as np


def init_individual(problem):
    random_list = np.array()
    for row_constraint in problem.row_constraints:
        random_list.extend(random.sample(range(1, 10), len(row_constraint.indices)))
    return random_list


def init_population(size, problem):
    population = np.array()
    for i in range(size):
        population.append(init_individual(problem))
    return population
