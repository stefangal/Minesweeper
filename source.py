import numpy as np


class Array:
    def __init__(self, x, y, bombs):
        self.x = x
        self.y = y
        self.board = self.int_board(bombs)


    def int_board(self, bmb_qty):
        """
        Generating bombs, where 1 means bomb, 0 means safe
        """
        self.tmp = np.array(list(-1 for _ in range(bmb_qty)))
        self.new = np.array([0])
        size = self.x*self.y
        while len(self.tmp) < size:
            self.tmp = np.append(self.tmp, self.new, axis=0)
        self.board = np.ravel(self.tmp)
        np.random.shuffle(self.board)
        self.board = self.board.reshape((self.x, self.y))
        self.touching()
        return self.board

    # def test_board(self):
    #     self.bd =

    def touching(self):
        for row_idx, row in enumerate(self.board, start=0):
            for nr_idx, nr in enumerate(row, start=0):
                if nr == -1:
                    try:
                        #1 before
                        if nr_idx > 0 and self.board[row_idx][nr_idx-1] != -1:
                            self.board[row_idx][nr_idx-1] += 1
                    except:
                        pass
                    try:
                        #1 after
                        if nr_idx < self.y and self.board[row_idx][nr_idx+1] != -1:
                            self.board[row_idx][nr_idx+1] += 1
                    except:
                        pass
                    try:
                        #above 1 before
                        if row_idx > 0 and nr_idx > 0 and self.board[row_idx-1][nr_idx-1] != -1:
                            self.board[row_idx-1][nr_idx-1] += 1
                    except:
                        pass
                    try:
                        #above
                        if row_idx > 0 and self.board[row_idx-1][nr_idx] != -1:
                            self.board[row_idx-1][nr_idx] += 1
                    except:
                        pass
                    try:
                        #above 1 after
                        if  row_idx > 0 and nr_idx < self.y and self.board[row_idx-1][nr_idx+1] != -1:
                            self.board[row_idx-1][nr_idx+1] += 1
                    except:
                        pass
                    try:
                        #below 1 before
                        if row_idx <= self.x and nr_idx > 0 and self.board[row_idx+1][nr_idx-1] != -1:
                            self.board[row_idx+1][nr_idx-1] += 1
                    except:
                        pass
                    try:
                        #below
                        if row_idx <= self.x and self.board[row_idx+1][nr_idx] != -1:
                            self.board[row_idx+1][nr_idx] += 1
                    except:
                        pass
                    try:
                        #below 1 after
                        if row_idx <= self.x and nr_idx < self.y and self.board[row_idx+1][nr_idx+1] != -1:
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

# if __name__ == "__main__":
#     a = Array(31, 20, 50)
#     print(a.board)

