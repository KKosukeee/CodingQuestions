"""
Solution for 1162. As Far from Land as Possible
https://leetcode.com/problems/as-far-from-land-as-possible/
"""
from collections import deque
class Solution:
    """
    Runtime: 668 ms, faster than 54.31% of Python3 online submissions for As Far from Land as Possible.
    Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for As Far from Land as Possible.
    """
    def maxDistance(self, grid):
        """
        Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

        The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

        If no land or water exists in the grid, return -1.



        Example 1:



        Input: [[1,0,1],[0,0,0],[1,0,1]]
        Output: 2
        Explanation:
        The cell (1, 1) is as far as possible from all the land with distance 2.
        Example 2:



        Input: [[1,0,0],[0,0,0],[0,0,0]]
        Output: 4
        Explanation:
        The cell (2, 2) is as far as possible from all the land with distance 4.


        Note:

        1 <= grid.length == grid[0].length <= 100
        grid[i][j] is 0 or 1
        Args:
            grid(list[list[int]]):

        Returns:
            int:
        """
        queue = deque([(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1])
        if len(queue) == len(grid) * len(grid[0]):
            return -1
        level = 0
        while queue:
            temp = deque([])
            while queue:
                i, j = queue.popleft()
                for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ix, jy = i+x, j+y
                    if 0 <= ix < len(grid) and 0 <= jy < len(grid[0]) and grid[ix][jy] == 0:
                        temp.append((ix, jy))
                        grid[ix][jy] = 1
            level += 1
            queue = temp
        return level - 1
