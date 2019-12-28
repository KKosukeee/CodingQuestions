"""
Solution for 766. Toeplitz Matrix
https://leetcode.com/problems/toeplitz-matrix/
"""
from collections import deque
from typing import List

class Solution:
  """
  Runtime: 88 ms, faster than 82.41% of Python3 online submissions for Toeplitz Matrix.
  Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Toeplitz Matrix.
  """
  def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    """
    A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

    Now given an M x N matrix, return True if and only if the matrix is Toeplitz.


    Example 1:

    Input:
    matrix = [
      [1,2,3,4],
      [5,1,2,3],
      [9,5,1,2]
    ]
    Output: True
    Explanation:
    In the above grid, the diagonals are:
    "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
    In each diagonal all elements are the same, so the answer is True.
    Example 2:

    Input:
    matrix = [
      [1,2],
      [2,2]
    ]
    Output: False
    Explanation:
    The diagonal "[1, 2]" has different elements.

    Note:

    matrix will be a 2D array of integers.
    matrix will have a number of rows and columns in range [1, 20].
    matrix[i][j] will be integers in range [0, 99].

    Follow up:

    What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
    What if the matrix is so large that you can only load up a partial row into the memory at once?

    Args:
      matrix:

    Returns:

    """
    return self.optimal_solution(matrix)

  def bfs_solution(self, matrix: List[List[int]]) -> bool:
    """
    A solution using BFS that runs in O(MN) in time and O(M) in space

    Args:
      matrix:

    Returns:

    """
    if not matrix:
      return False
    visited, q = set([(len(matrix) - 1, 0)]), deque([(len(matrix) - 1, 0)])
    while q:
      temp, v = deque(), None
      while q:
        i, j = q.popleft()
        if v == None:
          v = matrix[i][j]
        if matrix[i][j] != v:
          return False
        for y, x in self.get_neighs(i, j, matrix, visited):
          visited.add((i + y, j + x))
          temp.append((i + y, j + x))
      q = temp
    return True

  def get_neighs(self, i, j, matrix, visited):
    moves = []
    if 0 <= i + 1 < len(matrix) and (i + 1, j) not in visited:
      moves.append((1, 0))
    if 0 <= i - 1 < len(matrix) and (i - 1, j) not in visited:
      moves.append((-1, 0))
    if 0 <= j + 1 < len(matrix[0]) and (i, j + 1) not in visited:
      moves.append((0, 1))
    if 0 <= j - 1 < len(matrix[0]) and (i, j - 1) not in visited:
      moves.append((0, -1))
    return moves

  def sub_optimal_solution(self, matrix: List[List[int]]) -> bool:
    """
    A solution that runs in O(MN) in time and O(N) in space

    Args:
      matrix:

    Returns:

    """
    groups = {}
    for i, row in enumerate(matrix):
      for j, val in enumerate(row):
        if i - j not in groups:
          groups[i - j] = val
        elif groups[i - j] != val:
          return False
    return True

  def optimal_solution(self, matrix: List[List[int]]) -> bool:
    """
    An optimal solution that runs in O(MN) in time and O(1) in space

    Args:
      matrix:

    Returns:

    """
    return all(i == 0 or j == 0 or matrix[i - 1][j - 1] == val for i, row in
               enumerate(matrix) for j, val in enumerate(row))