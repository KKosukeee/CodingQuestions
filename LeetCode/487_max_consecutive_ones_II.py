"""
Solution for 487. Max Consecutive Ones II
https://leetcode.com/problems/max-consecutive-ones-ii/
"""
from typing import List

class Solution:
  """
  Runtime: 392 ms, faster than 90.05% of Python3 online submissions for Max Consecutive Ones II.
  Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Max Consecutive Ones II.
  """
  def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    """
    Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

    Example 1:
    Input: [1,0,1,1,0]
    Output: 4
    Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
        After flipping, the maximum number of consecutive 1s is 4.
    Note:

    The input array will only contain 0 and 1.
    The length of input array is a positive integer and will not exceed 10,000
    Follow up:
    What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?

    Args:
      nums:

    Returns:

    """
    return self.efficient_sliding_window(nums)

  def sliding_window(self, nums: List[int]) -> int:
    """
    An initial sliding window solution that runs in O(N) in time and O(1) in space

    Args:
      nums:

    Returns:

    """
    left, right = 0, 0
    res, k = 0, 1

    while right < len(nums):
      while right < len(nums) and k >= 0:
        if nums[right] == 0:
          k -= 1
        res = max(res, right - left)
        right += 1
      while left < right and k < 0:
        if nums[left] == 0:
          k += 1
        left += 1
    if k >= 0:
      return max(res, right - left)
    return res

  def cleaner_sliding_window(self, nums: List[int]) -> int:
    """
    A better sliding window solution that runs in O(N) in time and O(1) in space

    Args:
      nums:

    Returns:

    """
    left = 0
    k, res = 1, 0

    for right in range(len(nums)):
      if nums[right] == 0:
        k -= 1
      if k >= 0:
        res = max(res, right - left + 1)
      else:
        while left < right and k < 0:
          if nums[left] == 0:
            k += 1
          left += 1
    return res

  def efficient_sliding_window(self, nums: List[int]) -> int:
    """
    An efficient solution that runs in O(N) in time and O(1) in space

    Args:
      nums:

    Returns:

    """
    left, k = 0, 1
    for right in range(len(nums)):
      if nums[right] == 0:
        k -= 1
      if k < 0:
        if nums[left] == 0:
          k += 1
        left += 1
    return right - left + 1
