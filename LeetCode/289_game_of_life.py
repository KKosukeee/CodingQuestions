"""
Solution for 289. Game of Life
https://leetcode.com/problems/game-of-life/
"""
import collections
from copy import deepcopy
from typing import List

class Solution:
    """
    Runtime: 40 ms, faster than 66.29% of Python3 online submissions for Game of Life.
    Memory Usage: 13.8 MB, less than 10.00% of Python3 online submissions for Game of Life.
    """
    def simple_solution(self, board: List[List[int]]) -> None:
        """
        A simple solution that runs in O(mn) in space and time

        Args:
            board(List[List[int]]):

        Returns:
            None:

        """
        """
        Do not return anything, modify board in-place instead.
        """
        copied = deepcopy(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                zeros, ones = 0, 0
                # Upper-left
                if 0 <= i - 1 and 0 <= j - 1:
                    zeros = zeros + 1 if copied[i - 1][j - 1] == 0 else zeros
                    ones = ones + 1 if copied[i - 1][j - 1] == 1 else ones
                # Upper
                if 0 <= i - 1:
                    zeros = zeros + 1 if copied[i - 1][j] == 0 else zeros
                    ones = ones + 1 if copied[i - 1][j] == 1 else ones
                # Upper-right
                if 0 <= i - 1 and j + 1 < len(copied[0]):
                    zeros = zeros + 1 if copied[i - 1][j + 1] == 0 else zeros
                    ones = ones + 1 if copied[i - 1][j + 1] == 1 else ones
                # Left
                if 0 <= j - 1:
                    zeros = zeros + 1 if copied[i][j - 1] == 0 else zeros
                    ones = ones + 1 if copied[i][j - 1] == 1 else ones
                # Right
                if j + 1 < len(copied[0]):
                    zeros = zeros + 1 if copied[i][j + 1] == 0 else zeros
                    ones = ones + 1 if copied[i][j + 1] == 1 else ones
                # Bottom-left
                if i + 1 < len(copied) and 0 <= j - 1:
                    zeros = zeros + 1 if copied[i + 1][j - 1] == 0 else zeros
                    ones = ones + 1 if copied[i + 1][j - 1] == 1 else ones
                # Bottom
                if i + 1 < len(copied):
                    zeros = zeros + 1 if copied[i + 1][j] == 0 else zeros
                    ones = ones + 1 if copied[i + 1][j] == 1 else ones
                # Bottom-right
                if i + 1 < len(copied) and j + 1 < len(copied[0]):
                    zeros = zeros + 1 if copied[i + 1][j + 1] == 0 else zeros
                    ones = ones + 1 if copied[i + 1][j + 1] == 1 else ones
                # in case of 0
                if copied[i][j] == 0 and ones == 3:
                    board[i][j] = 1
                # Under-population
                if copied[i][j] == 1 and ones <= 1:
                    board[i][j] = 0
                elif copied[i][j] == 1 and ones > 3:
                    board[i][j] = 0

    def constance_space_solution(self, board: List[List[int]]) -> None:
        """
        A constance space solution that runs in O(mn) i time and O(1) in space

        Args:
            board(List[List[int]]):

        Returns:
            None:

        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                zeros, ones = 0, 0
                # Upper-left
                if 0 <= i - 1 and 0 <= j - 1:
                    zeros = zeros + 1 if board[i - 1][j - 1] % 2 == 0 else zeros
                    ones = ones + 1 if abs(board[i - 1][j - 1]) == 1 else ones
                # Upper
                if 0 <= i - 1:
                    zeros = zeros + 1 if board[i - 1][j] % 2 == 0 else zeros
                    ones = ones + 1 if abs(board[i - 1][j]) == 1 else ones
                # Upper-right
                if 0 <= i - 1 and j + 1 < len(board[0]):
                    zeros = zeros + 1 if board[i - 1][j + 1] % 2 == 0 else zeros
                    ones = ones + 1 if abs(board[i - 1][j + 1]) == 1 else ones
                # Left
                if 0 <= j - 1:
                    zeros = zeros + 1 if board[i][j - 1] % 2 == 0 else zeros
                    ones = ones + 1 if abs(board[i][j - 1]) == 1 else ones
                # Right
                if j + 1 < len(board[0]):
                    zeros = zeros + 1 if board[i][j + 1] % 2 == 0 else zeros
                    ones = ones + 1 if abs(board[i][j + 1]) == 1 else ones
                # Bottom-left
                if i + 1 < len(board) and 0 <= j - 1:
                    zeros = zeros + 1 if board[i + 1][j - 1] % 2 == 0 else zeros
                    ones = ones + 1 if abs(board[i + 1][j - 1]) == 1 else ones
                # Bottom
                if i + 1 < len(board):
                    zeros = zeros + 1 if board[i + 1][j] % 2 == 0 else zeros
                    ones = ones + 1 if abs(board[i + 1][j]) == 1 else ones
                # Bottom-right
                if i + 1 < len(board) and j + 1 < len(board[0]):
                    zeros = zeros + 1 if board[i + 1][j + 1] % 2 == 0 else zeros
                    ones = ones + 1 if abs(board[i + 1][j + 1]) == 1 else ones
                # in case of 0
                if board[i][j] == 0 and ones == 3:
                    board[i][j] = 2
                # Under-population
                if board[i][j] == 1 and ones <= 1:
                    board[i][j] = -1
                elif board[i][j] == 1 and ones > 3:
                    board[i][j] = -1

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] >= 1:
                    board[i][j] = 1
                elif board[i][j] <= 0:
                    board[i][j] = 0

    def interesting_solution(self, board):
        """
        An interesting solution that runs in O(mn) time and space

        Args:
            board:

        Returns:

        """
        def gameOfLifeInfinite(live):
            ctr = collections.Counter((I, J)
                                      for i, j in live
                                      for I in range(i - 1, i + 2)
                                      for J in range(j - 1, j + 2)
                                      if I != i or J != j)
            return {ij
                    for ij in ctr
                    if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}

        live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
        live = gameOfLifeInfinite(live)
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i, j) in live)

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

        Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

        Any live cell with fewer than two live neighbors dies, as if caused by under-population.
        Any live cell with two or three live neighbors lives on to the next generation.
        Any live cell with more than three live neighbors dies, as if by over-population..
        Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

        Example:

        Input:
        [
          [0,1,0],
          [0,0,1],
          [1,1,1],
          [0,0,0]
        ]
        Output:
        [
          [0,0,0],
          [1,0,1],
          [0,1,1],
          [0,1,0]
        ]
        Follow up:

        Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
        In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

        Args:
            board(list[list[int]]):

        Returns:
            None:

        """
        self.interesting_solution(board)

    """
    Simple solution: T->O(mn), S->O(mn)
    1. Loop through each cell in the board
    2. Update the current cell given the condition AND COPIED BOARD

    Constance space solution
    1. Loop through each cell and update the encode the new genration state
        1.1 If current cell is zero, but now becomes 1, set the vaule to 2
        1.2 If current cell is one, but now becomes 0, set the value to -1
    2. Loop through each cell again
        2.1 If current cell is less than or equal to 0, then it's a zero
        2.2 If current cell is greater than or equal to 1, then it's a one
        
    Interesting solution
    1. Create a sparse matrix
    2. Loop through each live cell
        2.1 Count neighbours cells
        2.2 Update the cell according to the rule
    3. Create a matrix by loop through it
    """