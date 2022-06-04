class brute_force():
    s = ''
    puzzleSolution = []
    def __init__(self,input_l):
        self.s = input_l

    def str_to_puzzle(self):
        print(self.s)
        for i in range(len(self.s)):
            if i % 9 == 0:
                temp = []
                for j in self.s[i:i + 9]:
                    temp.append(int(j))
                self.puzzleSolution.append(temp)
        return self.puzzleSolution

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

    def sudoku_brute_force(self):
        # 1
        print(self.s+"new iter")
        i = self.s.find('0')

        # 2
        cannotuse = {self.s[j] for j in range(len(self.s)) if self.same_row(i, j) | self.same_col(i, j) | self.same_block(i, j)}
        every_possible_values = {str(i) for i in range(10)} - cannotuse
        print(self.s)
        # 3
        for val in every_possible_values:
            self.s = self.s[0:i] + val + self.s[i + 1:]
            self.sudoku_brute_force()
            if self.s.find('0') == -1:
                #draw(str_to_puzzle(s))
                self.str_to_puzzle()
                #return self.puzzleSolution
