from brute_force import brute_force


def draw(puzzle):
    for r in range(len(puzzle)):
        if r == 0 or r == 3 or r == 6:
            print("+-------+-------+-------+")
        for c in range(len(puzzle[r])):
            if c == 0 or c == 3 or c == 6:
                print("| ", end="")
            if puzzle[r][c] != 0:
                print(puzzle[r][c], end=" ")
            else:
                print(end="  ")
            if c == 8:
                print("|")
    print("+-------+-------+-------+")


puzzleToSolve = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                 [6, 0, 0, 1, 9, 5, 0, 0, 0],
                 [0, 9, 8, 0, 0, 0, 0, 6, 0],
                 [8, 0, 0, 0, 6, 0, 0, 0, 3],
                 [4, 0, 0, 8, 0, 3, 0, 0, 1],
                 [7, 0, 0, 0, 2, 0, 0, 0, 6],
                 [0, 6, 0, 0, 0, 0, 2, 8, 0],
                 [0, 0, 0, 4, 1, 9, 0, 0, 5],
                 [0, 0, 0, 0, 8, 0, 0, 7, 9]]

s = ''.join(map(str, [''.join(map(str, i)) for i in puzzleToSolve]))

print("Sudoku Problem")
draw(puzzleToSolve)
print(s)
# exit()
print("\nSudoku Solution")
solver1 = brute_force(s)
# print(solver1.sudoku_brute_force())
solver1.sudoku_brute_force()
# s = solver1.result
# for i in len(s):

draw(solver1.result)
 #sudoku_brute_force(s)