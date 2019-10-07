"""
Solution for 794. Valid Tic-Tac-Toe State
https://leetcode.com/problems/valid-tic-tac-toe-state/
"""
from collections import Counter

class Solution(object):
    """
    Runtime: 16 ms, faster than 74.42% of Python online submissions for Valid Tic-Tac-Toe State.
    Memory Usage: 11.7 MB, less than 50.00% of Python online submissions for Valid Tic-Tac-Toe State.
    """
    def simple_solution(self, board):
        """
        A simple solution that runs in O(1) in time and space

        :type board: List[str]
        :rtype: bool
        """
        counter = Counter(board[0] + board[1] + board[2])
        if counter['O'] > counter['X'] or counter['X'] - counter['O'] > 1:
            return False
        if any((Counter(r)['X'] == 3 and not counter['X'] - counter['O'] == 1) or (
                Counter(r)['O'] == 3 and not counter['O'] == counter['X']) for r in board):
            return False
        if any((Counter(c)['X'] == 3 and not counter['X'] - counter['O'] == 1) or (
                Counter(c)['O'] == 3 and not counter['O'] == counter['X']) for c in zip(*board)):
            return False
        d1, d2 = [], []
        for i in range(len(board)):
            d1.append(board[i][i])
            d2.append(board[i][len(board) - i - 1])
        d1, d2 = Counter(d1), Counter(d2)
        if ((d1['X'] == 3 or d2['X'] == 3) and not counter['X'] - counter['O'] == 1) or (
                (d1['O'] == 3 or d2['O'] == 3) and not counter['O'] == counter['X']):
            return False
        return True

    def better_solution(self, board):
        """
        A cleaner solution that runs in O(1) in time and space

        :type board: List[str]
        :rtype: bool
        """

        def win(board, player):
            for i in range(len(board)):
                if all(board[i][j] == player for j in range(len(board))):
                    return True
                if all(board[j][i] == player for j in range(len(board))):
                    return True
            return ((player == board[0][0] == board[1][1] == board[2][2]) or
                    (player == board[0][2] == board[1][1] == board[2][0]))

        counter = Counter(board[0] + board[1] + board[2])
        if counter['O'] > counter['X'] or counter['X'] - counter['O'] > 1:
            return False
        if win(board, 'X') and not counter['X'] - counter['O'] == 1:
            return False
        if win(board, 'O') and not counter['X'] == counter['O']:
            return False
        return True

    def validTicTacToe(self, board):
        """
        A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

        The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

        Here are the rules of Tic-Tac-Toe:

        Players take turns placing characters into empty squares (" ").
        The first player always places "X" characters, while the second player always places "O" characters.
        "X" and "O" characters are always placed into empty squares, never filled ones.
        The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
        The game also ends if all squares are non-empty.
        No more moves can be played if the game is over.
        Example 1:
        Input: board = ["O  ", "   ", "   "]
        Output: false
        Explanation: The first player always plays "X".

        Example 2:
        Input: board = ["XOX", " X ", "   "]
        Output: false
        Explanation: Players take turns making moves.

        Example 3:
        Input: board = ["XXX", "   ", "OOO"]
        Output: false

        Example 4:
        Input: board = ["XOX", "O O", "XOX"]
        Output: true
        Note:

        board is a length-3 array of strings, where each string board[i] has length 3.
        Each board[i][j] is a character in the set {" ", "X", "O"}.

        :type board: List[str]
        :rtype: bool
        """
        return self.better_solution(board)

    """
    Simple solution
    T: O(1), S: O(N)
    1. Count # of 'X' and 'O'
    2. If not #ofX - #ofO <= 1, then return False
    3. If there is  any row, col and diag with same chars, then False
    4. Return True at the end of the function

    OXX
    XOX
    OXO

    OX
    XOX
    OXO
    """