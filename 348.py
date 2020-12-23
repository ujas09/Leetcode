class TicTacToe:
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.r = [0] * n
        self.c = [0] * n
        self.size = n
        self.d = [0, 0]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        sign = 1
        if player == 2:
            sign = -1

        self.r[row] += sign
        self.c[col] += sign

        if row == col:
            self.d[0] += sign
        if row + col == self.size - 1:
            self.d[1] += sign

        for i in range(self.size):
            if self.r[i] == self.size:
                return 1
            elif self.r[i] == -1 * self.size:
                return 2

            if self.c[i] == self.size:
                return 1
            elif self.c[i] == -1 * self.size:
                return 2

        if self.d[0] == self.size:
            return 1
        elif self.d[0] == -1 * self.size:
            return 2
        if self.d[1] == self.size:
            return 1
        elif self.d[1] == -1 * self.size:
            return 2
        return 0



        # Your TicTacToe object will be instantiated and called as such:
        # obj = TicTacToe(n)
        # param_1 = obj.move(row,col,player)