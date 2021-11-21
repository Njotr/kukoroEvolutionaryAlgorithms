from Utilities.generation import run_generations
from Utilities.initiation import init_population
from Utilities.problems import kakuro_622655, kakuro_357465, kakuro_383659

problems = [kakuro_622655, kakuro_357465, kakuro_383659]


def experiment_1():
    for problem in problems:
        pop = init_population(500, problem)
        run_generations(problem, pop, 0.5, 0.05, 30)


def experiment_2():
    for problem in problems:
        pop = init_population(500, problem)
        run_generations(problem, pop, 1, 0.05, 30)


def experiment_3():
    for problem in problems:
        pop = init_population(500, problem)
        run_generations(problem, pop, 1, 0.2, 30)


experiment_1()
experiment_2()
experiment_3()
