import random
import numpy as np

from Utilities.cheatSheet import cheatSheet


def init_individual(problem):
    random_list = []
    for row_constraint in problem.row_constraints:
        num_array = list(map(int, str(random.sample(cheatSheet[len(row_constraint.indices) - 1][row_constraint.total], 1)[0])))
        random.shuffle(num_array)
        random_list.extend(num_array)
    return np.array(random_list)


def init_population(size, problem):
    population = []
    for i in range(size):
        population.append(init_individual(problem))
    return population
