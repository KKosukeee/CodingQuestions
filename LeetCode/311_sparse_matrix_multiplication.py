"""
Solution for 311. Sparse Matrix Multiplication
https://leetcode.com/problems/sparse-matrix-multiplication/
"""
import numpy as np
from typing import List

class Solution:
  """
  Runtime: 140 ms, faster than 28.79% of Python3 online submissions for Sparse Matrix Multiplication.
  Memory Usage: 32.3 MB, less than 100.00% of Python3 online submissions for Sparse Matrix Multiplication.
  """
  def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """
    Given two sparse matrices A and B, return the result of AB.

    You may assume that A's column number is equal to B's row number.

    Example:

    Input:

    A = [
      [ 1, 0, 0],
      [-1, 0, 3]
    ]

    B = [
      [ 7, 0, 0 ],
      [ 0, 0, 0 ],
      [ 0, 0, 1 ]
    ]

    Output:

         |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
    AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                      | 0 0 1 |

    Args:
      A:
      B:

    Returns:

    """
    return self.smart_solution(A, B)

  def cheat_solution(self, A: List[List[int]], B: List[List[int]]) -> List[
    List[int]]:
    """
    A cheat solution using np module.

    Args:
      A:
      B:

    Returns:

    """
    return np.matmul(A, B)

  def initial_solution(self, A: List[List[int]], B: List[List[int]]) -> List[
    List[int]]:
    """
    An initial solution that runs in O(MNK) in time and O(MN) in space

    Args:
      A:
      B:

    Returns:

    """
    res = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
      for j in range(len(B[0])):
        for k in range(len(B)):
          res[i][j] += A[i][k] * B[k][j]
    return res

  def smart_solution(self, A: List[List[int]], B: List[List[int]]) -> List[
    List[int]]:
    """
    A smart solution that runs in same complexity in the worst case as the
    initial one

    Args:
      A:
      B:

    Returns:

    """
    res = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
      for k in range(len(B)):
        if A[i][k] != 0:
          for j in range(len(B[0])):
            res[i][j] += A[i][k] * B[k][j]
    return res
