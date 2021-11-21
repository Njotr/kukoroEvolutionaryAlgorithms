import deap
from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from datetime import time, datetime
from functools import partial
import matplotlib.pyplot as plt

from Utilities.generation import run_generations
from Utilities.initiation import init_population
from Utilities.problems import kakuro_622655, kakuro_357465

# pop = init_population(500, kakuro_622655)
# run_generations(kakuro_622655, pop, 0.5, 0.05, 100)

pop = init_population(500, kakuro_357465)
run_generations(kakuro_357465, pop, 0.5, 0.05, 100)
