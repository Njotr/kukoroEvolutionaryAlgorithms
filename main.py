from Utilities.generation import run_generations
from Utilities.initiation import init_population
from Utilities.problems import kakuro_622655, kakuro_357465, kakuro_383659

problems = [kakuro_622655, kakuro_357465, kakuro_383659]


def experiment_1():
    for problem in problems:
        pop = init_population(500, problem)
        run_generations(problem, pop, 0.25, 0.05, 50)


def experiment_2():
    for problem in problems:
        pop = init_population(500, problem)
        run_generations(problem, pop, 1, 0.05, 50)


def experiment_3():
    for problem in problems:
        pop = init_population(500, problem)
        run_generations(problem, pop, 1, 0.2, 50)


# experiment_1()
# experiment_2()
# experiment_3()

pop = init_population(500, kakuro_383659)
run_generations(kakuro_383659, pop, 1, 0.2, 50)
pop = init_population(500, kakuro_357465)
run_generations(kakuro_357465, pop, 1, 0.2, 50)

