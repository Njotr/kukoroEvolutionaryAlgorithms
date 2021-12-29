import random
import time
import numpy as np
from deap import tools, algorithms

from TreeStuff.envirment import setup_environment
from TreeStuff.testing import test
from Utilities import csp
from Utilities.importProblems import ecl_to_array, array_to_problem, ecl_to_array2
from Utilities.kakuro import Kakuro
from Utilities.plotLogs import plot

random.seed(42)
path = "./Data/problems.ecl"
problems = array_to_problem(ecl_to_array(path))
random.shuffle(problems)
train_problems = problems[:int((len(problems) + 1) * .70)]
test_problems = problems[int((len(problems) + 1) * .70):]
problems = ecl_to_array2(path)


############### Forward Checking Example ###############
def fw_solve(puzzle):
    problem = Kakuro(puzzle)
    start = time.time()
    FC_results = csp.backtracking_search(problem, inference=csp.forward_checking)
    end = time.time()
    problem.display(FC_results)
    print("FC time: " + str(end - start) + " assigns: " + str(problem.nassigns) + "\n\n")
############### Forward Checking Example ###############


for puzzle in problems:
    fw_solve(puzzle)

# def experiment_1():
    # pop = init_population(50, problem)
    # run_generations(problem, pop, 1, 0.2, 50)
    # solver = []
    # pset, toolbox = setup_environment(solver, train_problems)
    # population = toolbox.population(n=10)
    # hof = tools.HallOfFame(1)
    # stats = tools.Statistics(lambda ind: ind.fitness.values)
    # stats.register("avg", np.mean)
    # stats.register("std", np.std)
    # stats.register("min", np.min)
    # stats.register("max", np.max)
    # _, logs = algorithms.eaSimple(population, toolbox, 0.5, 0.5, 10, stats, halloffame=hof)
    # bestIndividual = hof.items[0]
    # print(f'{bestIndividual}')
    # # test(pset, solver, bestIndividual, test_problems)
    # plot(logs, "experiment_1")


# def experiment_2():
    # solver = []
    # pset, toolbox = setup_environment(solver, train_problems)
    # population = toolbox.population(n=10)
    # hof = tools.HallOfFame(1)
    # stats = tools.Statistics(lambda ind: ind.fitness.values)
    # stats.register("avg", np.mean)
    # stats.register("std", np.std)
    # stats.register("min", np.min)
    # stats.register("max", np.max)
    # _, logs = algorithms.eaSimple(population, toolbox, 0.5, 0.5, 10, stats, halloffame=hof)
    # bestIndividual = hof.items[0]
    # print(f'{bestIndividual}')
    # # test(pset, solver, bestIndividual, test_problems)
    # plot(logs, "experiment_1")


# def experiment_3():
    # solver = []
    # pset, toolbox = setup_environment(solver, train_problems)
    # population = toolbox.population(n=10)
    # hof = tools.HallOfFame(1)
    # stats = tools.Statistics(lambda ind: ind.fitness.values)
    # stats.register("avg", np.mean)
    # stats.register("std", np.std)
    # stats.register("min", np.min)
    # stats.register("max", np.max)
    # _, logs = algorithms.eaSimple(population, toolbox, 0.5, 0.5, 10, stats, halloffame=hof)
    # bestIndividual = hof.items[0]
    # print(f'{bestIndividual}')
    # # test(pset, solver, bestIndividual, test_problems)
    # plot(logs, "experiment_1")

# experiment_1()
# experiment_2()
# experiment_3()
