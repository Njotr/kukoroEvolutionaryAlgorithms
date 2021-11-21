import copy

import numpy
import deap
from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from datetime import time, datetime
from functools import partial
import matplotlib.pyplot as plt

from Utilities.initiation import init_individual
from Utilities.problems import kakuro_622655


demo = init_individual(kakuro_622655)
print(demo)

