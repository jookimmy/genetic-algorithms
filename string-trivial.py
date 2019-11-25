import random
import numpy as np

# create global variables for problem
GENE_POOL = [chr(i) for i in range(127)]
# TARGET_SOLUTION = np.array([1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1])
TARGET_SOLUTION = "Hello my name is Joowon"

class Individual:
    #initialize a new individual based on given chromosome and fitness
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calculate_fit()

    # calculate the fitness based on the difference of target and child
    def calculate_fit(self):
        fitness = 0
        for i in range(len(TARGET_SOLUTION)):
            if self.chromosome[i] == TARGET_SOLUTION[i]:
                fitness+=1
        return fitness/len(TARGET_SOLUTION)

    # mate two parents and acquire a child mutation prob of 5 percent
    def mate(self, parent):
        chromosome = ""
        for i in range(len(self.chromosome)):
            prob = random.random()
            if prob <= 0.475:
                chromosome += self.chromosome[i]
            elif prob <= 0.95 and prob > 0.475:
                chromosome += parent.chromosome[i]
            else:
                mutation = random.choice(GENE_POOL)
                chromosome += mutation
        child = Individual(chromosome)
        return child

# generate random set of chromosomes for initialization
# def gen_chromosome():
#    chromosome = np.zeros(len(TARGET_SOLUTION))
#    rand = random.randint(0, len(TARGET_SOLUTION))
#    chromosome[0:rand] = 1
#    np.random.shuffle(chromosome)
#    return chromosome

def gen_chromosome():
    chromosome = ""
    for i in range(len(TARGET_SOLUTION)):
        gene = random.choice(GENE_POOL)
        chromosome += gene
    return chromosome

def main():
    generation = 1
    population = [Individual(gen_chromosome()) for i in range(100)]
    population_size = 100
    
    while True:
        sorted_pop = sorted(population, key = lambda x : x.fitness, reverse = True)
        if sorted_pop[0].fitness == 1.0:
            population = sorted_pop
            print("Most fit has been found!")
            break
        
        top_10 = int((population_size*10)/100)
        parents = sorted_pop[:top_10]
        new_gen = []
        for i in range(100):
            parent1 = random.choice(parents)
            parent2 = random.choice([parent for parent in parents if parent.chromosome != parent1.chromosome])
            child = parent1.mate(parent2)
            new_gen.append(child)
        
        population = new_gen
        print("Generation: %s String: %s Fitness: %s " % (generation, population[0].chromosome, population[0].fitness ))
        generation += 1
    
    print("Generation: %s String: %s Fitness: %s" % (generation, population[0].chromosome, population[0].fitness))


if __name__ == '__main__': 
    main()


