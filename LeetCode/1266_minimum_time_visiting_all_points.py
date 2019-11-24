"""
Solution for 1266. Minimum Time Visiting All Points
https://leetcode.com/problems/minimum-time-visiting-all-points/
"""
from typing import List

class Solution:
  """
  Runtime: 52 ms, faster than 100.00% of Python3 online submissions for Minimum Time Visiting All Points.
  Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Minimum Time Visiting All Points.
  """
  def brute_force(self, points: List[List[int]]) -> int:
    """
    A brute force solution that runs in O(N) in time and O(1) in space

    Args:
      points:

    Returns:

    """
    steps = 0
    for i in range(1, len(points)):
      x, y = points[i - 1]
      if points[i][0] > x and points[i][1] > y:
        while points[i][0] > x and points[i][1] > y:
          y, x = y + 1, x + 1
          steps += 1
      if points[i][0] < x and points[i][1] < y:
        while points[i][0] < x and points[i][1] < y:
          y, x = y - 1, x - 1
          steps += 1
      if points[i][0] > x and points[i][1] < y:
        while points[i][0] > x and points[i][1] < y:
          y, x = y - 1, x + 1
          steps += 1
      if points[i][0] < x and points[i][1] > y:
        while points[i][0] < x and points[i][1] > y:
          y, x = y + 1, x - 1
          steps += 1
      if x == points[i][0]:
        steps += abs(points[i][1] - y)
      elif y == points[i][1]:
        steps += abs(points[i][0] - x)
    return steps

  def better_solution(self, points: List[List[int]]) -> int:
    """
    A better solution that runs in same as the brute force

    Args:
      points:

    Returns:

    """
    steps = 0
    for i in range(1, len(points)):
      x, y = points[i - 1]
      xx, yy = points[i]
      d1, d2 = abs(xx - x), abs(yy - y)
      steps += min(d1, d2) + abs(d1 - d2)
    return steps

  def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
    """
    On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

    You can move according to the next rules:

    In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
    You have to visit the points in the same order as they appear in the array.


    Example 1:


    Input: points = [[1,1],[3,4],[-1,0]]
    Output: 7
    Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]
    Time from [1,1] to [3,4] = 3 seconds
    Time from [3,4] to [-1,0] = 4 seconds
    Total time = 7 seconds
    Example 2:

    Input: points = [[3,2],[-2,2]]
    Output: 5


    Constraints:

    points.length == n
    1 <= n <= 100
    points[i].length == 2
    -1000 <= points[i][0], points[i][1] <= 1000

    Args:
      points:

    Returns:

    """
    return self.better_solution(points)
