"""
Solution for 162. Find Peak Element
https://leetcode.com/problems/find-peak-element/
"""
from typing import List

class Solution:
  """
  Runtime: 44 ms, faster than 71.44% of Python3 online submissions for Find Peak Element.
  Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find Peak Element.
  """
  def findPeakElement(self, nums: List[int]) -> int:
    """
    A peak element is an element that is greater than its neighbors.

    Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

    The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

    You may imagine that nums[-1] = nums[n] = -∞.

    Example 1:

    Input: nums = [1,2,3,1]
    Output: 2
    Explanation: 3 is a peak element and your function should return the index number 2.
    Example 2:

    Input: nums = [1,2,1,3,5,6,4]
    Output: 1 or 5
    Explanation: Your function can return either index number 1 where the peak element is 2,
                 or index number 5 where the peak element is 6.
    Note:

    Your solution should be in logarithmic complexity.

    Args:
      nums:

    Returns:

    """
    return self.log_solution(nums)

  def linear_solution(self, nums: List[int]) -> int:
    """
    A linear solution that runs in O(N) in time and O(1) in space

    Args:
      nums:

    Returns:

    """
    n = len(nums)
    nums = [-float('inf')] + nums + [-float('inf')]
    for i in range(1, n + 1):
      if nums[i - 1] < nums[i] > nums[i + 1]:
        return i - 1
    return -1

  def log_solution(self, nums: List[int]) -> int:
    """
    A logN solution that runs in O(log(N)) in time and O(1) in space¥

    Args:
      nums:

    Returns:

    """
    left, right = 0, len(nums) - 1
    while left < right:
      mid = (left + right) // 2
      if nums[mid] < nums[mid + 1]:
        left = mid + 1
      else:
        right = mid
    return left