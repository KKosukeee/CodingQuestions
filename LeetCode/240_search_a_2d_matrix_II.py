"""
Solution for 240. Search a 2D Matrix II
https://leetcode.com/problems/search-a-2d-matrix-ii/
"""
import bisect

class Solution:
  """
  Runtime: 32 ms, faster than 93.14% of Python3 online submissions for Search a 2D Matrix II.
  Memory Usage: 17.4 MB, less than 92.59% of Python3 online submissions for Search a 2D Matrix II.
  """
  def sub_optimal_solution(self, matrix, target):
    """
    A sub-optimal solution that runs in O(Mlog(K)) in time and O(1) in time

    Args:
      matrix:
      target:

    Returns:

    """
    if not any(matrix):
      return False
    for i in range(len(matrix)):
      if matrix[i][0] <= target <= matrix[i][-1]:
        index = bisect.bisect(matrix[i], target)
        if 0 <= index - 1 < len(matrix[i]) and matrix[i][index - 1] == target:
          return True
    return False

  def optimal_solution(self, matrix, target):
    """
    An optimal solution that runs in O(M+N) in time and O(1) in space

    Args:
      matrix:
      target:

    Returns:

    """
    if not any(matrix):
      return False
    row = len(matrix)
    col = 0

    while col < len(matrix[0]) and row >= 0:
      if matrix[row][col] > target:
        row -= 1
      elif matrix[row][col] < target:
        col += 1
      elif matrix[row][col] == target:
        return True
    return False

  def searchMatrix(self, matrix, target):
    """
    Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.
    Example:

    Consider the following matrix:

    [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    Given target = 5, return true.

    Given target = 20, return false.

    Args:
      matrix:
      target:

    Returns:

    """
    return self.sub_optimal_solution(matrix, target)
