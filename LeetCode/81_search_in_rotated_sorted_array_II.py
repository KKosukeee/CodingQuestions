"""
Solution for 81. Search in Rotated Sorted Array II
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
"""
from typing import List

class Solution:
  """
  Runtime: 48 ms, faster than 96.66% of Python3 online submissions for Search in Rotated Sorted Array II.
  Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Search in Rotated Sorted Array II.
  """
  def search(self, nums: List[int], target: int) -> bool:
    """
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

    You are given a target value to search. If found in the array return true, otherwise return false.

    Example 1:

    Input: nums = [2,5,6,0,0,1,2], target = 0
    Output: true
    Example 2:

    Input: nums = [2,5,6,0,0,1,2], target = 3
    Output: false
    Follow up:

    This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
    Would this affect the run-time complexity? How and why?

    Args:
      nums:
      target:

    Returns:

    """
    return self.logn_solution(nums, target)

  def linear_solution(self, nums: List[int], target: int) -> bool:
    """
    A linear solution that runs in O(N) in time and O(1) in space

    Args:
      nums:
      target:

    Returns:

    """
    return target in nums

  def logn_solution(self, nums: List[int], target: int) -> bool:
    """
    A logn solution that runs in O(logN) in time and O(1) in space

    Args:
      nums:
      target:

    Returns:

    """
    left, right = 0, len(nums) - 1
    while left <= right:
      mid = (left + right) // 2
      if nums[mid] == target:
        return True
      elif nums[left] == nums[mid] == nums[right]:
        left, right = left + 1, right - 1
      elif nums[mid] >= nums[left]:
        if nums[left] <= target <= nums[mid]:
          right = mid - 1
        else:
          left = mid + 1
      else:
        if nums[mid] <= target <= nums[right]:
          left = mid + 1
        else:
          right = mid - 1
    return False