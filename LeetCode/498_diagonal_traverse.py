"""
Solution for 498. Diagonal Traverse
https://leetcode.com/problems/diagonal-traverse/
"""
from collections import deque
from collections import defaultdict
from typing import List

class Solution:
  """
  Runtime: 200 ms, faster than 92.51% of Python3 online submissions for Diagonal Traverse.
  Memory Usage: 15.8 MB, less than 16.67% of Python3 online submissions for Diagonal Traverse.
  """
  def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
    """
    Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.



    Example:

    Input:
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]

    Output:  [1,2,4,7,5,3,6,8,9]

    Explanation:



    Note:

    The total number of elements of the given matrix will not exceed 10,000.

    Args:
      matrix:

    Returns:

    """
    return self.sort_odd_solution(matrix)

  def bfs_solution(self, matrix: List[List[int]]) -> List[int]:
    """
    A solution using BFS that runs in O(MND) where M = len(matrix), N = len(matrix[0])
    and D = max(all diag in matrix) in time and O(MN) in space

    Args:
      matrix:

    Returns:

    """
    if not any(matrix):
      return []

    t, q = 0, deque([(0, 0)])
    visited, res = set([(0, 0)]), []

    while q:
      temp = deque()
      res.extend(map(lambda x: matrix[x[0]][x[1]], q) if t % 2 == 0 else map(
        lambda x: matrix[x[0]][x[1]], reversed(q)))
      while q:
        i, j = q.popleft()
        for y, x in self.get_neighs(i, j, matrix):
          if (i + y, j + x) not in visited:
            visited.add((i + y, j + x))
            temp.append((i + y, j + x))
      q = temp
      t += 1
    return res

  def get_neighs(self, i, j, matrix):
    neighs = []
    if 0 <= i + 1 < len(matrix) and 0 <= j < len(matrix[0]):
      neighs.append((1, 0))
    if 0 <= i < len(matrix) and 0 <= j + 1 < len(matrix[0]):
      neighs.append((0, 1))
    return neighs

  def sort_odd_solution(self, matrix: List[List[int]]) -> List[int]:
    """
    A solution that runs in O(MN) in time and O(MN) in space

    Args:
      matrix:

    Returns:

    """
    diagonal_map = defaultdict(list)
    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        diagonal_map[i + j].append(matrix[i][j])
    res = []
    for k in sorted(diagonal_map.keys()):
      if k % 2 == 0:
        diagonal_map[k].reverse()
      res += diagonal_map[k]
    return res