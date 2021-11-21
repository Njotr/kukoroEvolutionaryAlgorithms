import random


def init_individual(problem):
    random_list = []
    for row_constraint in problem.row_constraints:
        random_list.extend(random.sample(range(1, 10), len(row_constraint.indices)))
    return random_list


def init_population(size, problem):
    population = []
    for i in range(size):
        population.append(init_individual(problem))
    return population
