"""
Solution for 137. Single Number II
https://leetcode.com/problems/single-number-ii/
"""
from collections import Counter
from typing import List

class Solution:
  """
  Runtime: 52 ms, faster than 97.40% of Python3 online submissions for Single Number II.
  Memory Usage: 14.5 MB, less than 66.67% of Python3 online submissions for Single Number II.
  """
  def sort_solution(self, nums: List[int]) -> int:
    """
    A sort solution that runs in O(NlogN) in time and O(1) in space

    Args:
      nums:

    Returns:

    """
    nums.sort()
    i = 0
    while i < len(nums) - 1:
      if nums[i] != nums[i + 1]:
        return nums[i]
      i += 3
    return nums[-1]

  def counter_solution(self, nums: List[int]) -> int:
    """
    A counter solution that runs in O(N) in time and O(N) in space

    Args:
      nums:

    Returns:

    """
    counter = Counter(nums)
    for num in nums:
      if counter[num] == 1:
        return num

  def bit_manipulation(self, nums: List[int]) -> int:
    """
    A bit manipulation solution that runs in O(N) in time and O(1) in space

    Args:
      nums:

    Returns:

    """
    seen_once, seen_twice = 0, 0
    for num in nums:
      seen_once = ~seen_twice & (seen_once ^ num)
      seen_twice = ~seen_once & (seen_twice ^ num)
    return seen_once

  def singleNumber(self, nums: List[int]) -> int:
    """
    Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

    Note:

    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

    Example 1:

    Input: [2,2,3,2]
    Output: 3
    Example 2:

    Input: [0,1,0,1,0,1,99]
    Output: 99

    Args:
      nums:

    Returns:

    """
    return self.bit_manipulation(nums)
