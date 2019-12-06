import numpy as np


class Array:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.board = self.int_board()

    def int_board(self):
        """
        Generating bombs, where 1 means bomb, 0 means safe
        """
        self.board = np.random.randint(20, size=(self.x, self.y))
        for x, row in enumerate(self.board):
            for y, col in enumerate(row):
                if col not in [0, 1]:
                    self.board[x][y] = 0
        return self.board

# if __name__ == "__main__":
#     a = Array(31, 20)
#     print(a.board)

