"""
Solution for 348. Design Tic-Tac-Toe
https://leetcode.com/problems/design-tic-tac-toe/
"""

class TicTacToe(object):
    """
    Runtime: 72 ms, faster than 89.77% of Python online submissions for Design Tic-Tac-Toe.
    Memory Usage: 13.8 MB, less than 100.00% of Python online submissions for Design Tic-Tac-Toe.
    """

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.board = [0 for _ in range(2 * n + 2)]
        self.n = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.board[row] = self.board[row] + 1 if player == 1 else self.board[row] - 1
        self.board[col + self.n] = self.board[col + self.n] + 1 if player == 1 else self.board[
                                                                                        col + self.n] - 1

        if row == col:
            self.board[-2] = self.board[-2] + 1 if player == 1 else self.board[-2] - 1

        if row == self.n - col - 1:
            self.board[-1] = self.board[-1] + 1 if player == 1 else self.board[-1] - 1

        if abs(self.board[row]) == self.n or abs(self.board[col + self.n]) == self.n or abs(
                self.board[-2]) == self.n or abs(self.board[-1]) == self.n:
            return 1 if player == 1 else 2
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)