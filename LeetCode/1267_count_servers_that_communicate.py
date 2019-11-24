"""
Solution for 1267. Count Servers that Communicate
https://leetcode.com/problems/count-servers-that-communicate/
"""
from typing import List

class Solution:
  """
  Runtime: 528 ms, faster than 100.00% of Python3 online submissions for Count Servers that Communicate.
  Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Count Servers that Communicate.
  """
  def initial_solution(self, grid: List[List[int]]) -> int:
    """
    An initial solution that runs in O(MN) in time and O(MN) in space

    Args:
      grid:

    Returns:

    """
    used = set()
    for i in range(len(grid)):
      temp = set()
      for j in range(len(grid[0])):
        if grid[i][j] == 1:
          temp.add((i, j))
      if len(temp) >= 2:
        used = used.union(temp)
    for j in range(len(grid[0])):
      temp = set()
      for i in range(len(grid)):
        if grid[i][j] == 1:
          temp.add((i, j))
      if len(temp) >= 2:
        used = used.union(temp)
    return len(used)

  def better_solution(self, grid: List[List[int]]) -> int:
    """
    A better solution that runs in O(MN) in time and O(M+N) in space

    Args:
      grid:

    Returns:

    """
    row = [0] * len(grid)
    col = [0] * len(grid[0])
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == 1:
          row[i] += 1
          col[j] += 1
    total = 0
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == 1:
          total += 1 if row[i] > 1 or col[j] > 1 else 0
    return total

  def countServers(self, grid: List[List[int]]) -> int:
    """
    You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

    Return the number of servers that communicate with any other server.



    Example 1:



    Input: grid = [[1,0],[0,1]]
    Output: 0
    Explanation: No servers can communicate with others.
    Example 2:



    Input: grid = [[1,0],[1,1]]
    Output: 3
    Explanation: All three servers can communicate with at least one other server.
    Example 3:



    Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
    Output: 4
    Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.


    Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m <= 250
    1 <= n <= 250
    grid[i][j] == 0 or 1

    Args:
      grid:

    Returns:

    """
    return self.better_solution(grid)