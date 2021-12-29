from typing import Tuple, List

import numpy as np
from deap import gp

def test(pset, solver, bestIndividual, test_problems):
    routine = gp.compile(bestIndividual, pset)
    solvedPercant = []
    evaluations = []
    solved = 0
    for i, problem in enumerate(test_problems):
        solver.reset(problem)
        solver.run(routine)
        evaluations.append(solver.evaluate()[0])
        if evaluations[-1] == 1.0:
            solved += 1
    return [f'{pair[1]}/{pair[0]}' for pair in solvedPercant if pair[0] != pair[1]]

