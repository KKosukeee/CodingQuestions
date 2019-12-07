"""
Solution for 260. Single Number III
https://leetcode.com/problems/single-number-iii/
"""
from collections import Counter
from typing import List

class Solution:
  """
  Runtime: 48 ms, faster than 99.92% of Python3 online submissions for Single Number III.
  Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Single Number III.
  """
  def counter(self, nums: List[int]) -> List[int]:
    """
    A cheating solution that runs O(N) in time and space

    Args:
      nums:

    Returns:

    """
    counter = Counter(nums)
    return filter(lambda k: counter[k] == 1, counter.keys())

  def bit_mask(self, nums: List[int]) -> List[int]:
    """
    A bitmask solution that runs in O(N) in time and O(1) in space

    Args:
      nums:

    Returns:

    """
    bitmask = 0

    for num in nums:
      bitmask ^= num

    diff = bitmask & (-bitmask)
    x = 0

    for num in nums:
      if diff & num:
        x ^= num
    return [x, x ^ bitmask]

  def singleNumber(self, nums: List[int]) -> List[int]:
    """
    Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

    Example:

    Input:  [1,2,1,3,2,5]
    Output: [3,5]
    Note:

    The order of the result is not important. So in the above example, [5, 3] is also correct.
    Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

    Args:
      nums:

    Returns:

    """
    return self.bit_mask(nums)
