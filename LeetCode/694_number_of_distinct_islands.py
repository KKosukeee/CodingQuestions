"""
Solution for 694. Number of Distinct Islands
https://leetcode.com/problems/number-of-distinct-islands/
"""
from collections import deque
from typing import List

class Solution:
  """
  Runtime: 256 ms, faster than 31.91% of Python3 online submissions for Number of Distinct Islands.
  Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Number of Distinct Islands.
  """
  def numDistinctIslands(self, grid: List[List[int]]) -> int:
    """
    Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

    Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

    Example 1:
    11000
    11000
    00011
    00011
    Given the above grid map, return 1.
    Example 2:
    11011
    10000
    00001
    11011
    Given the above grid map, return 3.

    Notice that:
    11
    1
    and
     1
    11
    are considered different island shapes, because we do not consider reflection / rotation.
    Note: The length of each dimension in the given grid does not exceed 50.

    Args:
      grid:

    Returns:

    """
    return self.bfs(grid)

  def bfs(self, grid: List[List[int]]) -> int:
    """
    A solution using BFS that runs in O(RC) where R = len(grid) and C = len(grid[0])
    in time and O(RC) in space as well

    Args:
      grid:

    Returns:

    """
    islands, visited = set(), set()

    def _bfs(i, j):
      q, path = deque([(i, j)]), set([(0, 0)])
      visited.add((i, j))
      while q:
        y, x = q.popleft()
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
          if 0 <= dy + y < len(grid) and \
              0 <= dx + x < len(grid[0]) and \
              (dy + y, dx + x) not in visited and \
              grid[dy + y][dx + x] == 1:
            q.append((dy + y, dx + x))
            visited.add((dy + y, dx + x))
            path.add((i - (dy + y), j - (dx + x)))
      islands.add(frozenset(path))

    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == 1 and (i, j) not in visited:
          _bfs(i, j)
    return len(islands)
