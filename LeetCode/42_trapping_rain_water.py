"""
Solution for 42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/
"""
from typing import List

class Solution:
  """
  Runtime: 44 ms, faster than 98.34% of Python3 online submissions for Trapping Rain Water.
  Memory Usage: 13.3 MB, less than 97.67% of Python3 online submissions for Trapping Rain Water.
  """
  def initial_solution(self, height: List[int]) -> int:
    """
    An initial solution that runs in O(N) in time and O(N) in space

    Args:
      height:

    Returns:

    """
    return self.calculate_water(height) + self.calculate_water(height[::-1],
                                                               True)

  def calculate_water(self, height, exclusive=False):
    if not height:
      return 0
    total, stack = 0, [(0, height[0])]
    for i in range(1, len(height)):
      cond = stack[-1][-1] <= height[i] if not exclusive else stack[-1][-1] < \
                                                              height[i]
      if cond:
        prev, prev_h = stack.pop()
        for j in range(prev + 1, i):
          total += min(prev_h, height[i]) - height[j]
        stack.append((i, height[i]))

    return total

  def dp_solution(self, height: List[int]) -> int:
    """
    A dp solution that runs in O(N) in time and space

    Args:
      height:

    Returns:

    """
    if not height:
      return 0
    total, n = 0, len(height)
    left, right = [0] * n, [0] * n

    left[0] = height[0]
    for i in range(1, len(height)):
      left[i] = max(left[i - 1], height[i])

    right[-1] = height[-1]
    for i in range(len(height) - 2, -1, -1):
      right[i] = max(right[i + 1], height[i])

    for i in range(len(height)):
      total += min(left[i], right[i]) - height[i]

    return total

  def two_pointers(self, height: List[int]) -> int:
    """
    A two pointers solution that runs in O(N) in tine and O(1) in space

    Args:
      height:

    Returns:

    """
    i, j = 0, len(height) - 1
    left, right, total = 0, 0, 0

    while i < j:
      if height[i] < height[j]:
        left = max(left, height[i])
        total += left - height[i]
        i += 1
      else:
        right = max(right, height[j])
        total += right - height[j]
        j -= 1
    return total

  def trap(self, height: List[int]) -> int:
    """
    Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


    The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

    Example:

    Input: [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6

    Args:
      height:

    Returns:

    """
    return self.two_pointers(height)
  