import random
import string


class GeneticAlgorithm:
    def __init__(self, target, population_size=100, mutation_rate=0.01):
        self.target = target
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = self.create_initial_population()

    def create_initial_population(self):
        # Create random strings of the same length as the target
        return [''.join(random.choice(string.ascii_letters + ' ')
                        for _ in range(len(self.target)))
                for _ in range(self.population_size)]

    def fitness(self, individual):
        # Calculate how close the individual is to the target
        return sum(1 for expected, actual in zip(self.target, individual)
                   if expected == actual)

    def mutate(self, individual):
        # Randomly change characters based on mutation rate
        individual = list(individual)
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                individual[i] = random.choice(string.ascii_letters + ' ')
        return ''.join(individual)

    def crossover(self, parent1, parent2):
        # Create a new individual by combining two parents
        split = random.randint(0, len(self.target))
        return parent1[:split] + parent2[split:]

    def evolve(self):
        # Sort population by fitness
        rated = [(self.fitness(individual), individual)
                 for individual in self.population]
        rated.sort(reverse=True)

        # Select top performers
        self.population = [individual for (score, individual) in rated[:self.population_size // 2]]

        # Create new generation
        while len(self.population) < self.population_size:
            parent1 = random.choice(self.population)
            parent2 = random.choice(self.population)
            child = self.crossover(parent1, parent2)
            child = self.mutate(child)
            self.population.append(child)

        return rated[0][1]  # Return best individual


def main():
    # Set the target string
    target = "Hello World"
    ga = GeneticAlgorithm(target)

    generation = 0
    best_solution = ''

    while best_solution != target:
        best_solution = ga.evolve()
        generation += 1

        if generation % 10 == 0:  # Print every 10 generations
            print(f"Generation {generation}: {best_solution}")

    print(f"\nTarget reached in generation {generation}!")
    print(f"Final solution: {best_solution}")


if __name__ == "__main__":
    main()
