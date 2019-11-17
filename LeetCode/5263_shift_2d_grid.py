"""
Solution for 5263. Shift 2D Grid
https://leetcode.com/problems/shift-2d-grid/
"""
from copy import deepcopy
from typing import List

class Solution:
  """
  Runtime: 804 ms, faster than 100.00% of Python3 online submissions for Shift 2D Grid.
  Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Shift 2D Grid.
  """
  def brute_force(self, grid: List[List[int]], k: int) -> List[List[int]]:
    """
    A brute force solution that copies the grid for k times and runs in
    O(NMK) in time and O(NM) in space

    Args:
      grid:
      k:

    Returns:

    """
    for _ in range(k):
      temp = deepcopy(grid)
      for i in range(len(grid)):
        for j in range(len(grid[0])):
          temp[i][(j + 1) % len(grid[0])] = grid[i][j]
      for i in range(len(temp)):
        temp[(i + 1) % len(temp)][0] = grid[i][-1]
      grid = temp
    return grid

  def optimal(self, grid: List[List[int]], k: int) -> List[List[int]]:
    """
    A slightly optimized solution that runs in O(NMK) in time and O(NM) in space

    Args:
      grid:
      k:

    Returns:

    """
    for _ in range(k):
      mat = []
      for i in range(len(grid)):
        row = []
        for j in range(len(grid[0])):
          row.append(grid[i][(j - 1) % len(grid[0])])
        mat.append(row)
      last = mat[-1][0]
      for i in range(len(grid)):
        last, mat[i][0] = mat[i][0], last
      grid = mat
    return grid

  def linear_solution(self, grid: List[List[int]], k: int) -> List[List[int]]:
    """
    A linear solution that runs in O(NM) in time and space

    Args:
      grid:
      k:

    Returns:

    """
    flattend = [grid[i][j] for i in range(len(grid)) for j in
                range(len(grid[0]))]
    shifted_array = []
    for i in range(len(flattend)):
      shifted_array.append(flattend[(i - k) % (len(grid) * len(grid[0]))])
    for i in range(len(flattend)):
      grid[i // len(grid[0])][i % len(grid[0])] = shifted_array[i]
    return grid

  def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
    """
    Given a 2D grid of size n * m and an integer k. You need to shift the grid k times.

    In one shift operation:

    Element at grid[i][j] becomes at grid[i][j + 1].
    Element at grid[i][m - 1] becomes at grid[i + 1][0].
    Element at grid[n - 1][m - 1] becomes at grid[0][0].
    Return the 2D grid after applying shift operation k times.



    Example 1:


    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
    Output: [[9,1,2],[3,4,5],[6,7,8]]
    Example 2:


    Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
    Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
    Example 3:

    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
    Output: [[1,2,3],[4,5,6],[7,8,9]]


    Constraints:

    1 <= grid.length <= 50
    1 <= grid[i].length <= 50
    -1000 <= grid[i][j] <= 1000
    0 <= k <= 100

    Args:
      grid:
      k:

    Returns:

    """
    return self.linear_solution(grid, k)