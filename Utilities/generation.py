import random
import matplotlib.pyplot as plt
import seaborn as sns


def getBestPopulation(problem, size, next_generation):
    return sorted(next_generation, key=lambda x: problem.get_solutions_fitness_score(x), reverse=True)[:size]


def mutation(individual, mutation_chance):
    if random.random() < mutation_chance:
        individual[random.randint(1, len(individual)-1)] = random.randint(1, 10)
    return individual


def crossover(problem, population, chance_to_breed, mutation_chance):
    next_generation = []
    for i in range(len(population)):
        for j in range(i+1, len(population)):
            if random.randint(1, 1/chance_to_breed) == 1:
                for k in range(5):
                    split = random.randint(1, len(population[i]))
                    temp = []
                    temp.extend(population[i][:split])
                    temp.extend(population[j][split:])
                    next_generation.append(mutation(temp, mutation_chance))
    next_generation.extend(population)
    next_generation = getBestPopulation(problem, len(population), next_generation)
    return next_generation


def run_generations(problem, population, chance_to_breed, mutation_chance, iteration_amount):
    best_scores = []
    worst_scores = []
    divider = len(problem.row_constraints)+len(problem.col_constraints)
    for i in range(iteration_amount):
        population = crossover(problem, population, chance_to_breed, mutation_chance)
        best_scores.append(problem.get_solutions_fitness_score(population[1]))
        worst_scores.append(problem.get_solutions_fitness_score(population[len(population)-1]))

    sns.set_style("whitegrid")
    plt.plot([score/divider for score in best_scores], color='green', label="Best Fitness")
    plt.plot([score/divider for score in worst_scores], color='red', label="Worst Fitness")
    plt.xlabel('Generations')
    plt.ylabel('Fitness')
    plt.title(str(problem.serial_number) + ' - Fitness per generation. breeding/mutation = ' + str(chance_to_breed) + '/' + str(mutation_chance))
    plt.legend(loc='upper right')
    plt.show()
    plt.close()
