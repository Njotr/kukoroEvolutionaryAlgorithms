import numpy as np
from deap import gp, creator, base, tools
from functools import partial


def progn(*args):
    for arg in args:
        arg()


def shuffle(out1, out2):
    return partial(progn, out1, out2)


def setup_environment(solver, train_problems):
    pset = gp.PrimitiveSet("main", 0)
    pset.addPrimitive(shuffle, 2)
    pset.addTerminal(solver.fw)
    pset.addTerminal(solver.down)
    pset.addTerminal(solver.bw)

    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()

    toolbox.register("expr_init", gp.genFull, pset=pset, min_=1, max_=4)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr_init)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    def evalArtificialAnt(individual):
        routine = gp.compile(individual, pset)
        evaluations = []
        for problem in train_problems:
            solver.reset(solver)
            solver.run(routine)
            evaluations.append(solver.evaluate())
        return np.mean(evaluations)

    toolbox.register("evaluate", evalArtificialAnt)
    toolbox.register("select", tools.selTournament, tournsize=5)
    toolbox.register("mate", gp.cxOnePoint)
    toolbox.register("expr_mut", gp.genFull, min_=0, max_=4)
    toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

    return pset, toolbox