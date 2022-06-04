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


def str_to_puzzle(s):
    puzzleSolution = []
    for i in range(len(s)):
        if i % 9 == 0:
            temp = []
            for j in s[i:i + 9]:
                temp.append(int(j))
            puzzleSolution.append(temp)
    return puzzleSolution


def same_row(i, j):
    if i // 9 == j // 9:
        return True
    return False


def same_col(i, j):
    if i % 9 == j % 9:
        return True
    return False


def same_block(i, j):
    if ((i // 9) // 3 == (j // 9) // 3) & ((i % 9) // 3 == (j % 9) // 3):
        return True
    return False


def sudoku_brute_force(s):
    # 1
    i = s.find('0')

    # 2
    cannotuse = {s[j] for j in range(len(s)) if same_row(i, j) | same_col(i, j) | same_block(i, j)}
    every_possible_values = {str(i) for i in range(10)} - cannotuse
    print(s)
    # 3
    for val in every_possible_values:
        s = s[0:i] + val + s[i + 1:]
        sudoku_brute_force(s)
        if s.find('0') == -1:
            draw(str_to_puzzle(s))


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
print("\nSudoku Solution")
sudoku_brute_force(s)