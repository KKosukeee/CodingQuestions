"""
Solution for 200. Number of Islands
https://leetcode.com/problems/number-of-islands/
"""
from collections import deque

class Solution:
    """
    Runtime: 96 ms, faster than 35.31% of Python3 online submissions for Number of Islands.
    Memory Usage: 13.6 MB, less than 29.67% of Python3 online submissions for Number of Islands.
    """
    def numIslands(self, grid):
        """
        Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island
        is surrounded by water and is formed by connecting adjacent lands horizontally or
        vertically. You may assume all four edges of the grid are all surrounded by water.

        Example 1:

        Input:
        11110
        11010
        11000
        00000

        Output: 1
        Example 2:

        Input:
        11000
        11000
        00100
        00011

        Output: 3
        Args:
            grid: 2D array where the each element is string. they are either '1' or '0'

        Returns:
            int: # of islands found in the grid
        """
        # initialize count as zero
        count = 0

        # write an outer loop
        for i in range(len(grid)):

            # write an inner loop
            for j in range(len(grid[i])):

                # check the grid[i][j] value
                if grid[i][j] == '1':
                    # if grid[i][j] == '1', then do BFS
                    self.bfs(grid, i, j)

                    # increment count by one
                    count += 1

        return count

    def bfs(self, grid, i, j):
        """
        Does the breadth-first search.
        Args:
            grid: input grid to the main function
            i: row index
            j: col index

        Returns:

        """
        # assign grid[i][j] value as '0'
        grid[i][j] = '0'

        # create level array
        level = [(i, j)]
        level = deque([(i, j)])

        # loop while level array contains an element
        while level:
            tmp = []

            # loop each item in level array
            while level:

                ci, cj = level.popleft()

                # get its' adjacent cells
                for ai, aj in self.get_adjacents(grid, ci, cj):
                    grid[ai][aj] = '0'

                    # put them into tmp array
                    tmp.append((ai, aj))

            # assign level array with tmp array
            level = deque(tmp)

    def get_adjacents(self, grid, i, j):
        """
        Gets the adjancent cells
        Args:
            grid: input grid to the main function
            i: row index
            j: col index

        Returns:
            list<tuple<int>>: list of indices that can be reached by the given i and j
        """
        valid_cells = []

        for _i, _j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= i + _i < len(grid) and 0 <= j + _j < len(grid[0]):
                if grid[i + _i][j + _j] == '1':
                    valid_cells.append((i + _i, j + _j))

        return valid_cells
