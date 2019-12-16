"""
Solution for 1293. Shortest Path in a Grid with Obstacles Elimination
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
"""
from collections import deque
from typing import List

class Solution:
  """
  Runtime: 920 ms, faster than 22.22% of Python3 online submissions for Shortest Path in a Grid with Obstacles Elimination.
  Memory Usage: 20.6 MB, less than 100.00% of Python3 online submissions for Shortest Path in a Grid with Obstacles Elimination.
  """
  def initial_solution(self, grid: List[List[int]], k: int) -> int:
    """
    An initial solution that runs in O(MNK) in time and O(MNK) in space

    Args:
      grid:
      k:

    Returns:

    """
    if len(grid) == 1 and len(grid[0]) == 1:
      return 0
    q, visited = deque([(0, k, 0, 0)]), set([(0, 0, k)])
    while q:
      s, r, i, j = q.popleft()
      for y, x in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
        if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
          if grid[y][x] == 1 and r > 0:
            if (y, x, r - 1) not in visited:
              visited.add((y, x, r - 1))
              q.append((s + 1, r - 1, y, x))
          if grid[y][x] == 0 and (y, x, r) not in visited:
            if y == len(grid) - 1 and x == len(grid[0]) - 1:
              return s + 1
            visited.add((y, x, r))
            q.append((s + 1, r, y, x))

    return -1

  def shortestPath(self, grid: List[List[int]], k: int) -> int:
    """
    Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In one step, you can move up, down, left or right from and to an empty cell.

    Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m-1, n-1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.



    Example 1:

    Input:
    grid =
    [[0,0,0],
     [1,1,0],
     [0,0,0],
     [0,1,1],
     [0,0,0]],
    k = 1
    Output: 6
    Explanation:
    The shortest path without eliminating any obstacle is 10.
    The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).


    Example 2:

    Input:
    grid =
    [[0,1,1],
     [1,1,1],
     [1,0,0]],
    k = 1
    Output: -1
    Explanation:
    We need to eliminate at least two obstacles to find such a walk.


    Constraints:

    grid.length == m
    grid[0].length == n
    1 <= m, n <= 40
    1 <= k <= m*n
    grid[i][j] == 0 or 1
    grid[0][0] == grid[m-1][n-1] == 0

    Args:
      grid:
      k:

    Returns:

    """
    return self.initial_solution(grid, k)