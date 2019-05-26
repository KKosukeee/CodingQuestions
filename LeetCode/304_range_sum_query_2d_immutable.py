"""
Solution for 304. Range Sum Query 2D - Immutable
https://leetcode.com/problems/range-sum-query-2d-immutable/
"""

class NumMatrix:
    """
    Runtime: 56 ms, faster than 93.76% of Python3 online submissions for Range Sum Query 2D -
        Immutable.
    Memory Usage: 15.9 MB, less than 35.37% of Python3 online submissions for Range Sum Query 2D -
        Immutable.
    """
    def __init__(self, matrix):
        """
        Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its
        upper left corner (row1, col1) and lower right corner (row2, col2).

        Range Sum Query 2D
        The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and
        (row2, col2) = (4, 3), which contains sum = 8.

        Example:
        Given matrix = [
          [3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]
        ]

        sumRegion(2, 1, 4, 3) -> 8
        sumRegion(1, 1, 2, 2) -> 11
        sumRegion(1, 2, 2, 4) -> 12
        Args:
            matrix: list of list of integer.
        """
        # Just initialize the matrix
        self.matrix = matrix

        # Create the sum_matrix for constant lookup
        if matrix:
            self.dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
            for r in range(len(matrix)):
                for c in range(len(matrix[0])):
                    self.dp[r + 1][c + 1] = self.dp[r + 1][c] + self.dp[r][c + 1] + matrix[r][c] - \
                                            self.dp[r][c]

    def sumRegion(self, row1, col1, row2, col2):
        """
        This returns the sum of sub-matrix specified with (row1, col1) and (row2,  col2) pair
        Args:
            row1: int value representing the top left corner of the sub-matrix
            col1: int value representing the top left corner of the sub-matrix
            row2: int value representing the bottom right corner of the sub-matrix
            col2: int value representing the bottom right corner of the sub-matrix

        Returns:
            int: representing the sum of the sub-matrix specified by the input values
        """
        return self.dp[row2 + 1][col2 + 1] - self.dp[row2 + 1][col1] - self.dp[row1][col2 + 1] + \
               self.dp[row1][col1]
