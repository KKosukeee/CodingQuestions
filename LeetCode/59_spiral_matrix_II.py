"""
Solution for 59. Spiral Matrix II
https://leetcode.com/problems/spiral-matrix-ii/
"""
from typing import List

class Solution:
  """
  Runtime: 24 ms, faster than 98.53% of Python3 online submissions for Spiral Matrix II.
  Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Spiral Matrix II.
  """
  def generateMatrix(self, n: int) -> List[List[int]]:
    """
    Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

    Example:

    Input: 3
    Output:
    [
     [ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]
    ]

    Args:
      n:

    Returns:

    """
    i, j, curr = 0, 0, 1
    direction = (0, 0)
    visited = set()
    matrix = [[1] * n for _ in range(n)]

    while len(visited) < n ** 2:
      y, x = i + direction[0], j + direction[1]
      if 0 <= y < n and 0 <= x < n and (y, x) not in visited:
        matrix[y][x] = curr
        visited.add((y, x))
        i, j = y, x
        curr += 1
      else:
        if direction == (0, 1):
          direction = (1, 0)
        elif direction == (1, 0):
          direction = (0, -1)
        elif direction == (0, -1):
          direction = (-1, 0)
        else:
          direction = (0, 1)

      if direction == (0, 0):
        direction = (0, 1)
    return matrix

  """
  1:[0,0]
  2:[0,1]
  3:[0,2]
  4:[1,2]
  5:[2,2]
  6:[2,1]
  7:[0,2]
  8:[1,0]
  9:[1,1]

  1. Initialize square matrix
  2. Initialize a direction

  """