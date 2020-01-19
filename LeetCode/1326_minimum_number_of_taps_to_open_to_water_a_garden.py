"""
Solution for 1326. Minimum Number of Taps to Open to Water a Garden
https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
"""
from typing import List

class Solution:
  """
  Runtime: 132 ms, faster than 100.00% of Python3 online submissions for Minimum Number of Taps to Open to Water a Garden.
  Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Minimum Number of Taps to Open to Water a Garden.
  """
  def minTaps(self, n: int, ranges: List[int]) -> int:
    """
    There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

    There are n + 1 taps located at points [0, 1, ..., n] in the garden.

    Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

    Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.



    Example 1:


    Input: n = 5, ranges = [3,4,1,1,0,0]
    Output: 1
    Explanation: The tap at point 0 can cover the interval [-3,3]
    The tap at point 1 can cover the interval [-3,5]
    The tap at point 2 can cover the interval [1,3]
    The tap at point 3 can cover the interval [2,4]
    The tap at point 4 can cover the interval [4,4]
    The tap at point 5 can cover the interval [5,5]
    Opening Only the second tap will water the whole garden [0,5]
    Example 2:

    Input: n = 3, ranges = [0,0,0,0]
    Output: -1
    Explanation: Even if you activate all the four taps you cannot water the whole garden.
    Example 3:

    Input: n = 7, ranges = [1,2,1,0,2,1,0,1]
    Output: 3
    Example 4:

    Input: n = 8, ranges = [4,0,0,0,0,0,0,0,4]
    Output: 2
    Example 5:

    Input: n = 8, ranges = [4,0,0,0,4,0,0,0,4]
    Output: 1


    Constraints:

    1 <= n <= 10^4
    ranges.length == n + 1
    0 <= ranges[i] <= 100

    Args:
      n:
      ranges:

    Returns:

    """
    return self.jump_game(n, ranges)

  def jump_game(self, n: int, ranges: List[int]) -> int:
    """
    A solution similar to the jump game that runs in O(N) in time and O(1) in
    space

    Args:
      n:
      ranges:

    Returns:

    """
    for i in range(len(ranges)):
      l = max(0, i - ranges[i])
      ranges[l] = max(ranges[i], i + ranges[i])
    low, high, res = 0, 0, 0
    while high < n:
      low, high = high, max(ranges[low:high + 1])
      if low == high:
        return -1
      res += 1
    return res
