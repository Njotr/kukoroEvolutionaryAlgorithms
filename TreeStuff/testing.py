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
        solvedPercant.append((len(problem), numOfSolvedEqs(puzzle)))
    solvedPercantStr = [f'{pair[1]}/{pair[0]}' for pair in solvedPercant if pair[0] != pair[1]]
    print(f'Evaluations mean={np.mean(evaluations)}, solved {solved} out of {len(evaluations)}')
    print(f'(Num of solved equations)/(Num of all equations) in puzzle: {", ".join(solvedPercantStr)}')


def numOfSolvedEqs(problem):
    count = 0
    for eq in problem:
        if eq.isSolved():
            count += 1
    return count
