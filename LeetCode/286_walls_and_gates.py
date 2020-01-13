"""
Solution for 286. Walls and Gates
https://leetcode.com/problems/walls-and-gates/
"""
from collections import deque
from typing import List

class Solution:
  """
  Runtime: 308 ms, faster than 58.99% of Python3 online submissions for Walls and Gates.
  Memory Usage: 20.6 MB, less than 60.00% of Python3 online submissions for Walls and Gates.
  """
  def wallsAndGates(self, rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.

    You are given a m x n 2D grid initialized with these three possible values.

    -1 - A wall or an obstacle.
    0 - A gate.
    INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
    Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

    Example:

    Given the 2D grid:

    INF  -1  0  INF
    INF INF INF  -1
    INF  -1 INF  -1
      0  -1 INF INF
    After running your function, the 2D grid should be:

      3  -1   0   1
      2   2   1  -1
      1  -1   2  -1
      0  -1   3   4
    """

    def get_neighs(i, j):
      neighs = []
      if 0 <= i - 1 < len(rooms) and (i - 1, j) in infs and (
      i - 1, j) not in seen:
        neighs.append((i - 1, j))
      if 0 <= i + 1 < len(rooms) and (i + 1, j) in infs and (
      i + 1, j) not in seen:
        neighs.append((i + 1, j))
      if 0 <= j - 1 < len(rooms[0]) and (i, j - 1) in infs and (
      i, j - 1) not in seen:
        neighs.append((i, j - 1))
      if 0 <= j + 1 < len(rooms[0]) and (i, j + 1) in infs and (
      i, j + 1) not in seen:
        neighs.append((i, j + 1))
      return neighs

    q, infs, seen = deque(), set(), set()
    for i in range(len(rooms)):
      for j in range(len(rooms[i])):
        if rooms[i][j] == 0:
          q.append((i, j, 0))
          seen.add((i, j))

        if rooms[i][j] == 2147483647:
          infs.add((i, j))

    while q:
      i, j, cost = q.popleft()

      for k, l in get_neighs(i, j):
        rooms[k][l] = cost + 1
        q.append((k, l, cost + 1))
        seen.add((k, l))
