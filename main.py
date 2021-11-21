import deap
from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from datetime import time, datetime
from functools import partial
import matplotlib.pyplot as plt

from Utilities.initiation import init_individual, init_population
from Utilities.problems import kakuro_622655

pop = init_population(2, kakuro_622655)




