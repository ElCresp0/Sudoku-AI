from random import random, randrange
from copy import copy, deepcopy


class GeneticSolver:

    # input: two-dimension list, empty squares should be set to 0
    def __init__(self, input, population_size = 250, number_of_generations = 500, elite_size = 25, mutation_rate = 0.05, restart_after = 20):

        self.input = input
        self.number_of_generations = number_of_generations
        self.elite_size = elite_size
        self.mutation_rate = mutation_rate
        self.population_size = population_size
        self.restart_after = restart_after

        self.no_no_square = []
        self.top_fitness_over_time = []
        self.avg_fitness_over_time = []

        self.available_numbers = {}
        for number in range(1, 10):
            self.available_numbers[number] = 9
        
        for row in range(len(input)):
            for col in range(len(input[0])):
                if input[row][col] != 0:
                    self.no_no_square.append([row, col])
                    self.available_numbers[input[row][col]] -= 1
        self.lez_go(self.generate_population())


    # this returns an array of numbers sorted from the most to the least optimal
    # (according to the used evaluation method)
    def get_optimal_numbers(self, solution, coords):
        numbers = [i for i in range(1, 10)]
        ret = []
        while len(numbers) > 0:
            ret.append(numbers.pop(randrange(len(numbers))))
        functions = [self.get_file, self.get_line, self.get_square]
        my_list = []
        for function in functions:
            my_list.append(function(coords, solution))
        numbers = [[i, my_list.count(i)] for i in range(1, 10)]
        numbers = sorted(numbers, key = lambda v: v[1])
        numbers = [n for [n, _] in numbers]
        return numbers

    def generate_solution(self):
        ret = deepcopy(self.input)
        tmp_available_numbers = copy(self.available_numbers)
        to_fill = [] # creating a list of coordinates to be filled randomly
        for row in range(len(ret)):
            for col in range(len(ret[0])):
                if ret[row][col] == 0:
                    to_fill.append([row, col])

        while len(to_fill) > 0:
            [row, col] = to_fill.pop(randrange(len(to_fill)))
            numbers = self.get_optimal_numbers(ret, [row, col])
            i = 0
            while tmp_available_numbers[numbers[i]] == 0:
                i += 1
            tmp_available_numbers[numbers[i]] -= 1
            ret[row][col] = numbers[i]
        return ret

    def generate_population(self):
        return [self.generate_solution() for _ in range(self.population_size)]

    # in the following functions: coords: [row, col]
    def get_square(self, coords, solution):
        row, col = coords[0] // 3, coords[1] // 3
        return solution[row][3*col : (3*col + 3)] \
        + solution[row + 1][3*col : (3*col + 3)] \
        + solution[row + 2][3*col : (3*col + 3)]
            
    def get_line(self, coords, solution):
        return solution[coords[0]]

    def get_file(self, coords, solution):
        return [row[coords[1]] for row in solution]

    # coords: [row, col]
    # def evaluate_gene(self, coords, solution):
    #     ret = 3 * 8
    #     functions = [self.get_file, self.get_line, self.get_square]
    #     for function in functions:
    #         my_list = function(coords, solution)
    #         ret -= abs(1 - my_list.count(solution[coords[0]][coords[1]]))
    #     return ret

    # def fitness(self, solution):
    #     ret = self.fitness_of_a_correct_solution
    #     for row in range(len(solution)):
    #         for col in range(len(solution[0])):
    #             functions = [self.get_file, self.get_line, self.get_square]
    #             for function in functions:
    #                 my_list = function([row, col], solution)
    #                 ret -= abs(1 - my_list.count(solution[row][col]))
    #     return abs(self.fitness_of_a_correct_solution - ret)
        
    # def reversed_fitness(self, solution):
    #     ret = 1
    #     for row in range(len(solution)):
    #         for col in range(len(solution[0])):
    #             functions = [self.get_file, self.get_line, self.get_square]
    #             for function in functions:
    #                 my_list = function([row, col], solution)
    #                 ret += abs(1 - my_list.count(solution[row][col]))
    #     return ret

    # def reverse_fitness(self, population) -> dict:
    #     ret = []
    #     for solution in enumerate(population):
    #        ret.append([solution[0], 1 / self.fitness(solution[1])])
    #     ret = dict(sorted(ret, key = lambda x: x[1]))
    #     return ret

    # def population_fitness_f(self, population) -> dict:
    #     ret = []
    #     for solution in enumerate(population):
    #         ret.append([solution[0], 1 / self.reversed_fitness(solution[1])])
    #     return dict(sorted(ret, key = lambda v: -v[1]))



    # reversed because the return value gets bigger for worse solutions
    def reversed_fitness(self, solution):
        ret = 1
        for row in range(len(solution)):
            for col in range(len(solution[0])):
                functions = [self.get_file, self.get_line, self.get_square]
                for function in functions:
                    my_list = function([row, col], solution)
                    ret += abs(1 - my_list.count(solution[row][col]))
        return ret

    def population_fitness_f(self, population) -> dict:
        ret = []
        for solution in enumerate(population):
            ret.append([solution[0], -self.reversed_fitness(solution[1])])
        return dict(sorted(ret, key = lambda v: -v[1]))




    def select(self, population):

        population_fitness = self.population_fitness_f(population) # dict{index, fitness (descending)}
        ret = []

        # elite
        for i in range(self.elite_size):
            ret.append(population[list(population_fitness.keys())[i]])

        # lottery
        sum_fitness = sum(population_fitness.values())
        if len(self.avg_fitness_over_time) == len(self.top_fitness_over_time):
            self.avg_fitness_over_time.append(sum_fitness / self.population_size)
        sum_so_far = 0
        odds = dict()
        for solution in population_fitness.keys():
            odds[solution] = sum_so_far + (population_fitness[solution] / sum_fitness)
            sum_so_far += odds[solution]

        while len(ret) < self.population_size:        
            r = random()
            for solution in population_fitness.keys():
                if odds[solution] >= r:
                    ret.append(population[solution])
                    break
        
        return ret

    def cross_population(self, population):
        ret = []
        ret.append(population[0]) # preserving the best solution (not the whole elite in this case)

        while len(ret) < self.population_size:
            parent1 = population[randrange(len(population))]
            parent2 = population[randrange(len(population))]

            child = deepcopy(self.input)
            tmp_available_numbers = copy(self.available_numbers)
            for row in range(len(parent1)):
                for col in range(len(parent1[0])):
                    # no_no_square contains coordinates of the original input values - not to be changed, hence the name
                    if not [row, col] in self.no_no_square:
                        gene = parent1[row][col] if randrange(2) == 0 else parent2[row][col]
                        numbers = [gene] + self.get_optimal_numbers(child, [row, col])
                        while tmp_available_numbers[numbers[0]] == 0:
                            # at this point if the list was empty, it would mean a mistake has been made somewhere else in the code
                            gene = numbers.pop(0)
                        tmp_available_numbers[gene] -= 1
                        child[row][col] = gene
            ret.append(child)
        return ret

    def mutate(self, population):
        def mutate_solution(solution):
            # swap two numbers
            for _ in range(1):
                row_col_1 = [randrange(len(solution)), randrange(len(solution[0]))]
                row_col_2 = [randrange(len(solution)), randrange(len(solution[0]))]
                for row_col_i in [row_col_1, row_col_2]:
                    while row_col_i in self.no_no_square:
                        row_or_col = randrange(2) # 0 if random() < 0.5 else 1 #
                        row_col_i[row_or_col] = (row_col_i[row_or_col] + 1) % len(solution)
                solution[row_col_1[0]][row_col_1[1]], solution[row_col_2[0]][row_col_2[1]] = solution[row_col_2[0]][row_col_2[1]], solution[row_col_1[0]][row_col_1[1]]

        # protect elite from mutation
        ret = self.select(population)[:self.elite_size]
        for solution in population[self.elite_size:]:        
            if random() <= self.mutation_rate:
                mutate_solution(solution)
            ret.append(solution)
        return ret

    def lez_go(self, population):
        prev_top_fitness = 0
        stuck_counter = 0
        for generation in range(self.number_of_generations):

            # DRAWING PROGRESSBAR:
            # hash_signs = int(generation / self.number_of_generations * 50)
            # underlines = 50 - hash_signs
            # progress_bar = "progress: ["
            # for _ in range(hash_signs):
            #     progress_bar += "#"
            # for _ in range(underlines):
            #     progress_bar += "_"
            # progress_bar += "]"
            # print("\r" + progress_bar, end = "")

            population = self.select(population)

            current_top_fitness = self.reversed_fitness(population[0])
            if prev_top_fitness == current_top_fitness:
                stuck_counter += 1
            else:
                prev_top_fitness = current_top_fitness
                stuck_counter = 0

            self.top_fitness_over_time.append(-current_top_fitness)

            print("\r{0} / {1} -> {2}".format(generation, self.number_of_generations, current_top_fitness), end = "")

            population = self.cross_population(population)
            population = self.mutate(population)

            # restarting the population (preserving the elite) when it's unlikely to further evolve
            # the newly generated populations do sometimes improve the solution
            # idea of restarting the population is taken from here:
            # http://micsymposium.org/mics_2009_proceedings/mics2009_submission_66.pdf
            if stuck_counter == self.restart_after:
                population = self.select(population)[:self.elite_size] + self.generate_population()[self.elite_size:]
                self.restart_after += 5
                stuck_counter = 0

        print()
        self.solution = self.select(population)[0]