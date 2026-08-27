class TicTacToe:

    def __init__(self, n: int):
        """
        时间复杂度: O(n)。
        空间复杂度: O(n)。

        Initialize your data structure here.
        """
        self.n = n

        self.rows = [0] * n
        self.cols = [0] * n

        # 记录两条对角线的和
        self.diag = 0
        self.anti_diag = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        时间复杂度: O(1)。
        空间复杂度: O(1)。

        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        value = 1 if player == 1 else -1

        self.rows[row] += value
        self.cols[col] += value

        # 只有(0,0), (1,1)这种对角线才能组成三连
        if row == col:
            self.diag += value
        # 以及(0,2), (1,1)这种反对角线才能组成三连
        if row + col == self.n - 1:
            self.anti_diag += value

        # 正负有一方满足条件,即可返回当前player
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diag) == self.n or abs(self.anti_diag) == self.n:
            return player

        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)