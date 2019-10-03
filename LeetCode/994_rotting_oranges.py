"""
Solution for 994. Rotting Oranges
https://leetcode.com/problems/rotting-oranges/
"""
from collections import deque

class Solution(object):
    """
    Runtime: 40 ms, faster than 54.13% of Python online submissions for Rotting Oranges.
    Memory Usage: 11.8 MB, less than 62.50% of Python online submissions for Rotting Oranges.
    """
    def bfs(self, grid):
        """
        A BFS solution that runs in O(MN) in space and time

        :type grid: List[List[int]]
        :rtype: int
        """
        rottens = deque(
            [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 2])
        minutes = 0

        while rottens:
            temp = deque([])
            while rottens:
                i, j = rottens.popleft()
                for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]) and grid[i + x][
                        j + y] == 1:
                        temp.append((i + x, j + y))
                        grid[i + x][j + y] = 2
            rottens = temp
            if rottens:
                minutes += 1

        return minutes if not any(
            grid[i][j] == 1 for i in range(len(grid)) for j in range(len(grid[0]))) else -1

    def orangesRotting(self, grid):
        """
        In a given grid, each cell can have one of three values:

        the value 0 representing an empty cell;
        the value 1 representing a fresh orange;
        the value 2 representing a rotten orange.
        Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

        Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.



        Example 1:



        Input: [[2,1,1],[1,1,0],[0,1,1]]
        Output: 4
        Example 2:

        Input: [[2,1,1],[0,1,1],[1,0,1]]
        Output: -1
        Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
        Example 3:

        Input: [[0,2]]
        Output: 0
        Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


        Note:

        1 <= grid.length <= 10
        1 <= grid[0].length <= 10
        grid[i][j] is only 0, 1, or 2.

        :type grid: List[List[int]]
        :rtype: int
        """
        return self.bfs(grid)

    """
    BFS
    1. Loop through each cell. If the orange in rotten, start the BFS
    2. Cache the visited oranges, so that it won't be visited again
    3. Count how many oranges has become rotten
    4. Compare the total number of oranges and rotten oranges.

    Union Find
    1. Union every adjacent oranges.
    2. Loop through each cell and find number of parents.
    3. If the number of the parents is 1, then return the count it took
    4. Else, return -1
    """