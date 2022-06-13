# SOURCE: https://betterprogramming.pub/sudoku-solver-a-brute-force-approach-using-python-ee180b071346

from brute_force import brute_force
from time import time


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

def change_format(l:list) -> str:
    return ''.join(map(str, [''.join(map(str, i)) for i in l]))

input = open("../SudoKu/output.txt", "r")

sudokus = []
sudoku = []

puzzleToSolve = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                 [6, 0, 0, 1, 9, 5, 0, 0, 0],
                 [0, 9, 8, 0, 0, 0, 0, 6, 0],
                 [8, 0, 0, 0, 6, 0, 0, 0, 3],
                 [4, 0, 0, 8, 0, 3, 0, 0, 1],
                 [7, 0, 0, 0, 2, 0, 0, 0, 6],
                 [0, 6, 0, 0, 0, 0, 2, 8, 0],
                 [0, 0, 0, 4, 1, 9, 0, 0, 5],
                 [0, 0, 0, 0, 8, 0, 0, 7, 9]]

sudokus.append(change_format(puzzleToSolve))

sudokus.append("907106030010032078250070041800461523502700104046300090790004052005987410461050709") #,987146235614532978253879641879461523532798164146325897798614352325987416461253789
sudokus.append("954802000000594283380007450023760005540280170071050308005028017200100590716045830") #,954832761167594283382617459823761945549283176671459328495328617238176594716945832
sudokus.append("031700002087502310200034876009041687708020400103067200800050143952010700010608500") #,431786952687592314295134876529341687768925431143867295876259143952413768314678529
sudokus.append("500021736142736005073900421307098142859000070210070508020300850006059204980214007") #,598421736142736985673985421367598142859142673214673598421367859736859214985214367
sudokus.append("080524106502617380671038205830052617420760030016803524004100893167380402308205061") #,983524176542617389671938245839452617425761938716893524254176893167389452398245761
sudokus.append("783205614290640038041083250378029000009104087004370502410007905902416800037902460") #,783295614295641738641783259378529146529164387164378592416837925952416873837952461
sudokus.append("700390004064715309389000750093624500507830640042500093406057030100083420038402175") #,751398264264715389389246751893624517517839642642571893426157938175983426938462175
sudokus.append("837602001410807029600410873020054387054370002008020140001783200083009514260001038") #,837692451415837629692415873926154387154378962378926145541783296783269514269541738
sudokus.append("472000059506027080010069007047310000000695720650070138024103590060700803138056400") #,472831659596427381813569247247318965381695724659274138724183596965742813138956472
sudokus.append("800940100160308704009260035601035009038700612497000083216083940974610308380409261") #,853947126162358794749261835621835479538794612497126583216583947974612358385479261




# while len(sudokus) < 9:
#     line = input.readline()
#     if len(line) < 2:
#         if len(sudoku) > 0:
#             sudokus.append(sudoku)
#         sudoku = []
#     if len(line) == 0:
#         break
#     if len(line) >= 9:
#         sudoku.append([int(digit) for digit in line[:len(line) - 1]])
#         if len(sudoku[-1]) == 8:
#             sudoku[-1].append(int(line[-1]))

# input.close()


for ith_sudoku in sudokus:
    # s = change_format(ith_sudoku)
    solver = brute_force(ith_sudoku)
    # draw(ith_sudoku)
    print(ith_sudoku)

    start = time()
    solver.sudoku_brute_force()
    finish = time()

    print()
    draw(solver.result)
    print("time: {0}".format(round(finish - start, 2)))
    print(); print()
exit()

s = change_format(puzzleToSolve)

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
