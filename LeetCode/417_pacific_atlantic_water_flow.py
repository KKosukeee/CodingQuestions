"""
Solution for 417. Pacific Atlantic Water Flow
https://leetcode.com/problems/pacific-atlantic-water-flow/
"""
from collections import deque

class Solution:
    """
    Runtime: 308 ms, faster than 92.91% of Python3 online submissions for Pacific Atlantic Water Flow.
    Memory Usage: 15.2 MB, less than 10.00% of Python3 online submissions for Pacific Atlantic Water Flow.
    """
    def pacificAtlantic(self, matrix):
        """
        Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

        Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

        Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

        Note:

        The order of returned grid coordinates does not matter.
        Both m and n are less than 150.


        Example:

        Given the following 5x5 matrix:

          Pacific ~   ~   ~   ~   ~
               ~  1   2   2   3  (5) *
               ~  3   2   3  (4) (4) *
               ~  2   4  (5)  3   1  *
               ~ (6) (7)  1   4   5  *
               ~ (5)  1   1   2   4  *
                  *   *   *   *   * Atlantic

        Return:

        [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
        Args:
            matrix(list[list[int]]):

        Returns:
            list[list[int]]:
        """
        if not matrix:
            return []

        pacific_set, pacific_queue = set(), deque([])
        atlantic_set, atlantic_queue = set(), deque([])
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            pacific_set.add((i, 0))
            pacific_queue.append((i, 0))

            atlantic_set.add((i, n - 1))
            atlantic_queue.append((i, n - 1))

        for j in range(n):
            pacific_set.add((0, j))
            pacific_queue.append((0, j))

            atlantic_set.add((m - 1, j))
            atlantic_queue.append((m - 1, j))

        while pacific_queue:
            i, j = pacific_queue.popleft()
            for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ix, jy = i + d[0], j + d[1]
                if 0 <= ix < m and 0 <= jy < n and not (ix, jy) in pacific_set and matrix[i][j] <= \
                        matrix[ix][jy]:
                    pacific_set.add((ix, jy))
                    pacific_queue.append((ix, jy))

        while atlantic_queue:
            i, j = atlantic_queue.popleft()
            for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ix, jy = i + d[0], j + d[1]
                if 0 <= ix < m and 0 <= jy < n and not (ix, jy) in atlantic_set and matrix[i][j] <= \
                        matrix[ix][jy]:
                    atlantic_set.add((ix, jy))
                    atlantic_queue.append((ix, jy))

        return pacific_set.intersection(atlantic_set)
