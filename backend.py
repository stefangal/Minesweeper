import numpy as np


class Array:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.board = self.int_board()
        self.board = self.touching()

    def int_board(self):
        """
        Generating bombs, where 1 means bomb, 0 means safe
        """
        self.board = np.random.randint(low=-1, high=20, size=(self.x, self.y))
        for x, row in enumerate(self.board):
            for y, col in enumerate(row):
                if col not in [0, -1]:
                    self.board[x][y] = 0
        return self.board

    def touching(self):
        for row_idx, row in enumerate(self.board, start=0):
            for nr_idx, nr in enumerate(row, start=0):
                if nr == -1:
                    try:
                        #1 before
                        if nr_idx > 0 and self.board[row_idx][nr_idx-1] != -1:
                            self.board[row_idx][nr_idx-1] += 1
                        #1 after
                        if nr_idx < 19 and self.board[row_idx][nr_idx+1] != -1:
                            self.board[row_idx][nr_idx+1] += 1
                        #above 1 before
                        if row_idx > 0 and nr_idx > 0 and self.board[row_idx-1][nr_idx-1] != -1:
                            self.board[row_idx-1][nr_idx-1] += 1
                        #above
                        if row_idx > 0 and self.board[row_idx-1][nr_idx] != -1:
                            self.board[row_idx-1][nr_idx] += 1
                        #above 1 after
                        if  row_idx > 0 and nr_idx < 19 and self.board[row_idx-1][nr_idx+1] != -1:
                            self.board[row_idx-1][nr_idx+1] += 1
                        #below 1 before
                        if row_idx < 31 and nr_idx > 0 and self.board[row_idx+1][nr_idx-1] != -1:
                            self.board[row_idx+1][nr_idx-1] += 1
                        #below
                        if row_idx < 31 and self.board[row_idx+1][nr_idx] != -1:
                            self.board[row_idx+1][nr_idx] += 1
                        #below 1 after
                        if row_idx < 31 and nr_idx < 19 and self.board[row_idx+1][nr_idx+1] != -1:
                            self.board[row_idx+1][nr_idx+1] += 1
                    except:
                        pass
        return self.board

    @property
    def bombs(self):
        bomb_qty = 0
        for row in self.board:
            for cell in row:
                if cell == -1:
                    bomb_qty += 1
        return bomb_qty

if __name__ == "__main__":
    a = Array(31, 20)
    print(a.bombs)

