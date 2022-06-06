class brute_force():
    # s = ''
    # puzzleSolution = []
    def __init__(self,input_l):
        self.s = input_l
        self.result = None

    def str_to_puzzle(self, s):
        # print(self.s)
        puzzleSolution = []
        for i in range(len(s)):
            if i % 9 == 0:
                temp = []
                for j in s[i:i + 9]:
                    temp.append(int(j))
                puzzleSolution.append(temp)
        return puzzleSolution

    def same_row(self, i, j):
        if i // 9 == j // 9:
            return True
        return False

    def same_col(self,i, j):
        if i % 9 == j % 9:
            return True
        return False

    def same_block(self, i, j):
        if ((i // 9) // 3 == (j // 9) // 3) & ((i % 9) // 3 == (j % 9) // 3):
            return True
        return False

    def sudoku_brute_force(self, s = -1):
        if s == -1:
            s = self.s
        # 1
        # print(self.s+"new iter")
        i = s.find('0')

        # 2
        cannotuse = {s[j] for j in range(len(s)) if self.same_row(i, j) | self.same_col(i, j) | self.same_block(i, j)}
        every_possible_values = {str(i) for i in range(10)} - cannotuse
        # print(self.s)
        # 3
        for val in every_possible_values:
            s = s[0:i] + val + s[i + 1:]
            self.sudoku_brute_force(s)
            if s.find('0') == -1:
                #draw(str_to_puzzle(s))
                # self.str_to_puzzle()
                #return self.puzzleSolution
                self.result = self.str_to_puzzle(s)
