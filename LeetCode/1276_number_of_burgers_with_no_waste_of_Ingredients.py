"""
Solution for 1276. Number of Burgers with No Waste of Ingredients
https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/
"""
import numpy as np
from typing import List

class Solution:
  """
  Runtime: 108 ms, faster than 7.93% of Python3 online submissions for Number of Burgers with No Waste of Ingredients.
  Memory Usage: 32.4 MB, less than 100.00% of Python3 online submissions for Number of Burgers with No Waste of Ingredients.
  """
  def first_solution(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
    """
    A first solution that runs in TLE

    Args:
      tomatoSlices:
      cheeseSlices:

    Returns:

    """
    if tomatoSlices == cheeseSlices == 0:
      return [0, 0]
    if tomatoSlices % 2 != 0:
      return []
    if cheeseSlices > tomatoSlices / 2:
      return []
    if tomatoSlices > cheeseSlices * 4:
      return []
    num_jumbo, num_small = 0, 0
    while tomatoSlices > 0 and cheeseSlices > 0:
      if tomatoSlices == cheeseSlices * 4:
        return [num_jumbo + tomatoSlices // 4, num_small]
      if tomatoSlices == cheeseSlices * 2:
        return [num_jumbo, num_small + tomatoSlices // 2]
      if tomatoSlices > cheeseSlices * 2:
        tomatoSlices, cheeseSlices = tomatoSlices - 4, cheeseSlices - 1
        num_jumbo += 1
      else:
        tomatoSlices, cheeseSlices = tomatoSlices - 2, cheeseSlices - 1
        num_small += 1

  def second_solution(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
    """
    Second solution that runs in O(1) in space and memory

    Args:
      tomatoSlices:
      cheeseSlices:

    Returns:

    """
    if tomatoSlices == cheeseSlices == 0:
      return [0, 0]
    if tomatoSlices % 2 != 0:
      return []
    if cheeseSlices > tomatoSlices / 2:
      return []
    if tomatoSlices > cheeseSlices * 4:
      return []
    a = np.array([[4, 2], [1, 1]])
    b = np.array([tomatoSlices, cheeseSlices])
    return np.linalg.solve(a, b).astype(int)

  def third_solution(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
    """
    The third solution that runs in O(1) in time and space

    Args:
      tomatoSlices:
      cheeseSlices:

    Returns:

    """
    two_x = tomatoSlices - 2 * cheeseSlices
    x = two_x // 2
    y = cheeseSlices - x
    return [x, y] if two_x >= 0 and not two_x % 2 and y >= 0 else []

  def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
    """
    Given two integers tomatoSlices and cheeseSlices. The ingredients of different burgers are as follows:

    Jumbo Burger: 4 tomato slices and 1 cheese slice.
    Small Burger: 2 Tomato slices and 1 cheese slice.
    Return [total_jumbo, total_small] so that the number of remaining tomatoSlices equal to 0 and the number of remaining cheeseSlices equal to 0. If it is not possible to make the remaining tomatoSlices and cheeseSlices equal to 0 return [].



    Example 1:

    Input: tomatoSlices = 16, cheeseSlices = 7
    Output: [1,6]
    Explantion: To make one jumbo burger and 6 small burgers we need 4*1 + 2*6 = 16 tomato and 1 + 6 = 7 cheese. There will be no remaining ingredients.
    Example 2:

    Input: tomatoSlices = 17, cheeseSlices = 4
    Output: []
    Explantion: There will be no way to use all ingredients to make small and jumbo burgers.
    Example 3:

    Input: tomatoSlices = 4, cheeseSlices = 17
    Output: []
    Explantion: Making 1 jumbo burger there will be 16 cheese remaining and making 2 small burgers there will be 15 cheese remaining.
    Example 4:

    Input: tomatoSlices = 0, cheeseSlices = 0
    Output: [0,0]
    Example 5:

    Input: tomatoSlices = 2, cheeseSlices = 1
    Output: [0,1]


    Constraints:

    0 <= tomatoSlices <= 10^7
    0 <= cheeseSlices <= 10^7

    Args:
      tomatoSlices:
      cheeseSlices:

    Returns:

    """
    return self.third_solution(tomatoSlices, cheeseSlices)

  """
  Return [], iff the following conditions meet
  - # of cheeseSlices > tomatoSlices / 2
  - tomatoSlices % 2 != 0

  Greedy approaach
  1. Loop while tomatoSlices and cheeseSlices > 0
    1.1 If tomatoSlices == cheeseSlices * 4, then return it
    1.2 If tomatoSlices == cheeseSlices * 2, then return it
    1.3 
  """