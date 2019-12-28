"""
Solution for 670. Maximum Swap
https://leetcode.com/problems/maximum-swap/
"""
from functools import reduce

class Solution:
  """
  Runtime: 20 ms, faster than 98.26% of Python3 online submissions for Maximum Swap.
  Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Maximum Swap.
  """
  def maximumSwap(self, num: int) -> int:
    """
    Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

    Example 1:
    Input: 2736
    Output: 7236
    Explanation: Swap the number 2 and the number 7.
    Example 2:
    Input: 9973
    Output: 9973
    Explanation: No swap.
    Note:
    The given number is in the range [0, 108]

    Args:
      num:

    Returns:

    """
    nums = [int(v) for v in str(num)]
    index_map = {x: i for i, x in enumerate(nums)}
    for i, x in enumerate(nums):
      for d in range(9, x, -1):
        if d in index_map and index_map[d] > i:
          nums[i], nums[index_map[d]] = nums[index_map[d]], nums[i]
          return reduce(lambda a, b: a*10+b, nums)
    return num