"""
Solution for 221. Maximal Square
https://leetcode.com/problems/maximal-square/
"""

class Solution(object):
    """
    Runtime: 180 ms, faster than 40.87% of Python online submissions for Maximal Square.
    Memory Usage: 19.7 MB, less than 5.16% of Python online submissions for Maximal Square.
    """
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
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j] == 1:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j]) + 1
        max_area = max(max(x) for x in dp)
        return max_area ** 2
