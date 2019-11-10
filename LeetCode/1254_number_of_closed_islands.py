"""
Solution for 1254. Number of Closed Islands
https://leetcode.com/problems/number-of-closed-islands/
"""
from collections import deque
from typing import List

class Solution:
    """
    Runtime: 132 ms, faster than 100.00% of Python3 online submissions for Number of Closed Islands.
    Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Number of Closed Islands.
    """
    def closedIsland(self, grid: List[List[int]]) -> int:
        """
        Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

        Return the number of closed islands.



        Example 1:



        Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
        Output: 2
        Explanation:
        Islands in gray are closed because they are completely surrounded by water (group of 1s).
        Example 2:



        Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
        Output: 1
        Example 3:

        Input: grid = [[1,1,1,1,1,1,1],
                       [1,0,0,0,0,0,1],
                       [1,0,1,1,1,0,1],
                       [1,0,1,0,1,0,1],
                       [1,0,1,1,1,0,1],
                       [1,0,0,0,0,0,1],
                       [1,1,1,1,1,1,1]]
        Output: 2


        Constraints:

        1 <= grid.length, grid[0].length <= 100
        0 <= grid[i][j] <=1

        Args:
            grid:

        Returns:

        """
        def bfs(i, j):
            if (i, j) in visited:
                return 0
            queue, is_closed = deque([(i, j)]), True
            while queue:
                i, j = queue.popleft()
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                if 0 <= i - 1 and grid[i - 1][j] == 0:
                    queue.append((i - 1, j))
                if i + 1 < len(grid) and grid[i + 1][j] == 0:
                    queue.append((i + 1, j))
                if 0 <= j - 1 and grid[i][j - 1] == 0:
                    queue.append((i, j - 1))
                if j + 1 < len(grid[0]) and grid[i][j + 1] == 0:
                    queue.append((i, j + 1))
                is_closed = is_closed and 0 <= i - 1 and i + 1 < len(
                    grid) and 0 <= j - 1 and j + 1 < len(grid[0])
            return 1 if is_closed else 0

        count, visited = 0, set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    count += bfs(i, j)
        return count
