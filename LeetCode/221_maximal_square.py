"""
Solution for 221. Maximal Square
https://leetcode.com/problems/maximal-square/
"""
from typing import List

class Solution(object):
    """
    Runtime: 180 ms, faster than 40.87% of Python online submissions for Maximal Square.
    Memory Usage: 19.7 MB, less than 5.16% of Python online submissions for Maximal Square.
    """

    def top_down(self, matrix: List[List[str]]) -> int:
        """
        Top-down solution that runs in O(MN) where M = len(matrix), N = len(matrix[0])

        Args:
            matrix(list[list[str]]):

        Returns:
            int:

        """
        dp = [[-1] * len(matrix[0]) for _ in range(len(matrix))]

        def find_max(i, j):
            if not matrix:
                return 0
            if not 0 <= i < len(matrix) or not 0 <= j < len(matrix[0]):
                return 0
            if matrix[i][j] == '0':
                return 0
            if dp[i][j] >= 0:
                return dp[i][j]
            dp[i][j] = min(find_max(i + 1, j + 1),
                           find_max(i + 1, j),
                           find_max(i, j + 1)) + 1
            return dp[i][j]

        global_max = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    global_max = max(global_max, find_max(i, j))
        return global_max ** 2

    def bottom_up(self, matrix: List[List[str]]) -> int:
        """
        Bottom-up solution that runs in O(MN)

        Args:
            matrix(list[list[str]]):

        Returns:
            int

        """
        if not matrix:
            return 0
        dp = [[0 if matrix[i][j] == '0' else 1 for j in range(len(matrix[0]))] for i in
              range(len(matrix))]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return max(dp[i][j] for i in range(len(dp)) for j in range(len(dp[0]))) ** 2

    def maximalSquare(self, matrix):
        """
        Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only
        1's and return its area.

        Example:

        Input:

        1 0 1 0 0
        1 0 1 1 1
        1 1 1 1 1
        1 0 0 1 0

        Output: 4
        Args:
            matrix: 2D matrix for finding maximum square

        Returns:
            int: indicating the are of the maximum square
        """
        return self.bottom_up(matrix)
