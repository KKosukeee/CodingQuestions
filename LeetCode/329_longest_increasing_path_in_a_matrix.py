"""
Solution for 329. Longest Increasing Path in a Matrix
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
"""
from functools import lru_cache
from typing import List

class Solution:
    """
    Runtime: 492 ms, faster than 75.58% of Python3 online submissions for Longest Increasing Path in a Matrix.
    Memory Usage: 18.3 MB, less than 7.69% of Python3 online submissions for Longest Increasing Path in a Matrix.
    """
    def top_down(self, matrix: List[List[int]]) -> int:
        """
        A top-down solution that runs in O(MN) in time and space

        Args:
            matrix:

        Returns:

        """
        @lru_cache(maxsize=None)
        def dfs(i, j):
            return max(
                [dfs(y, x) for y, x in self.get_neighbours(i, j, matrix)],
                default=0) + 1

        return max([dfs(i, j) for i in range(len(matrix)) for j in
                    range(len(matrix[0]))], default=0)

    def get_neighbours(self, i, j, matrix):
        """
        A helper method

        Args:
            i:
            j:
            matrix:

        Returns:

        """
        neighs = []
        if i - 1 >= 0 and matrix[i][j] < matrix[i - 1][j]:
            neighs.append((i - 1, j))
        if i + 1 < len(matrix) and matrix[i][j] < matrix[i + 1][j]:
            neighs.append((i + 1, j))
        if j - 1 >= 0 and matrix[i][j] < matrix[i][j - 1]:
            neighs.append((i, j - 1))
        if j + 1 < len(matrix[0]) and matrix[i][j] < matrix[i][j + 1]:
            neighs.append((i, j + 1))
        return neighs

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        Given an integer matrix, find the length of the longest increasing path.

        From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

        Example 1:

        Input: nums =
        [
          [9,9,4],
          [6,6,8],
          [2,1,1]
        ]
        Output: 4
        Explanation: The longest increasing path is [1, 2, 6, 9].
        Example 2:

        Input: nums =
        [
          [3,4,5],
          [3,2,6],
          [2,2,1]
        ]
        Output: 4
        Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

        Args:
            matrix:

        Returns:

        """
        return self.top_down(matrix)
