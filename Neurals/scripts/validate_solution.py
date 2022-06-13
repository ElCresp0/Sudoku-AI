def correct_sudoku(board):
    for i in range(len(board)):
        row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        col = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(len(board)):
            if board[i][j] in row:
                row.remove(board[i][j])
            else:
                return False
            if board[j][i] in col:
                col.remove(board[j][i])
            else:
                return False

    b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    f = []
    for i in range(9):
        f.append(b.copy())
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] in f[int(i / 3) * 3 + int(j / 3)]:
                f[int(i / 3) * 3 + int(j / 3)].remove(board[i][j])
            else:
                return False
    return True


def mistakes_made_sudoku(board):
    mistakes = 0
    for i in range(len(board)):
        row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        col = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(len(board)):
            if board[i][j] in row:
                row.remove(board[i][j])
            else:
                mistakes += 1
            if board[j][i] in col:
                col.remove(board[j][i])
            else:
                mistakes += 1

    b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    f = []
    for i in range(9):
        f.append(b.copy())
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] in f[int(i / 3) * 3 + int(j / 3)]:
                f[int(i / 3) * 3 + int(j / 3)].remove(board[i][j])
            else:
                mistakes += 1
    return mistakes

# print(correct_sudoku([
#          [4,8,9,5,3,2,7,6,1],
#          [7,1,3,4,8,6,5,9,2],
#          [5,6,2,9,1,7,8,3,4],
#          [2,5,8,3,4,1,9,7,6],
#          [6,3,1,7,5,9,2,4,8],
#          [9,4,7,2,6,8,1,5,3],
#          [1,2,5,6,7,3,4,8,9],
#          [8,7,6,1,9,4,3,2,5],
#          [3,9,4,8,2,5,6,1,7]]))
