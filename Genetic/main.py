from geneticSolver import GeneticSolver
from time import time
import matplotlib.pyplot as plt

# reading the input
input = open("../SudoKu/output.txt", "r")

sudokus = []
sudoku = []

while len(sudokus) < 3:
    line = input.readline()
    if len(line) < 2:
        if len(sudoku) > 0:
            sudokus.append(sudoku)
        sudoku = []
    if len(line) == 0:
        break
    if len(line) >= 9:
        sudoku.append([int(digit) for digit in line[:len(line) - 1]])
        if len(sudoku[-1]) == 8:
            sudoku[-1].append(int(line[-1]))

input.close()

# printing unsolved examples
# for ith_sudoku in sudokus:
#     print(); print()
#     for row in ith_sudoku:
#         s = ""
#         for digit in row:
#             s += (str(digit) + " ")
#         print(s)
# exit()


# a puzzle used in the bruteforce solution
puz = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]]

start = time()
solver = GeneticSolver(input=puz, population_size=500, number_of_generations=500, elite_size=5, mutation_rate=0.05, restart_after=20) # 500, 1000, 5, 0.05, 25
# input=sudokus[i] for testing other examples
finish = time()

solution = solver.solution

correct = True
for line_coords in [[0,0], [1,0], [2,0], [3,0], [4,0], [5,0], [6,0], [7,0], [8,0]]:
    my_list = solver.get_line(line_coords, solution)
    if len(my_list) != len(set(my_list)):
        correct = False

for file_coords in [[0,0], [1,1], [2,2], [3,3], [4,4], [5,5], [6,6], [7,7], [8,8]]:
    my_list = solver.get_file(file_coords, solution)
    if len(my_list) != len(set(my_list)):
        correct = False

for square_coords in [[0,0], [3,0], [6,0], [0,3], [3,3], [6,3], [0,6], [3,6], [6,6]]:
    my_list = solver.get_square(square_coords, solution)
    if len(my_list) != len(set(my_list)):
        correct = False

print("\nSolution is correct - " + str(correct))
s = ""
for row in solution:
    for digit in row:
        s += (str(digit) + " ")
    s = s[:len(s) - 1] + "\n"
print(s)
print("time: {0} s".format(round(finish - start, 2)))

plt.figure()
plt.plot(solver.top_fitness_over_time)
plt.plot(solver.avg_fitness_over_time)
correct_fitness = 9*9*9*8 + 1
plt.legend(labels=["fitness of the best solution over time", "average fitness of population over time"])
plt.xlabel("time [#generation]")
plt.ylabel("fitness")
plt.show()
# plt.show(block = False)