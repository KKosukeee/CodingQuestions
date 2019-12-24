"""
Solution for 33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
from typing import List

class Solution:
  """
  Runtime: 36 ms, faster than 98.11% of Python3 online submissions for Search in Rotated Sorted Array.
  Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Search in Rotated Sorted Array.
  """
  def brute_force(self, nums: List[int], target: int) -> int:
    """
    A brute force solution that runs in linear time and constant space

    Args:
      nums:
      target:

    Returns:

    """
    return nums.index(target) if target in nums else -1

  def one_pass_solution(self, nums: List[int], target: int) -> int:
    """
    A one-pass solution that runs in O(logN) in time and O(1) in space

    Args:
      nums:
      target:

    Returns:

    """
    left, right = 0, len(nums) - 1
    while left <= right:
      mid = (left + right) // 2
      if nums[mid] == target:
        return mid
      elif nums[left] <= nums[mid]:
        if nums[left] <= target < nums[mid]:
          right = mid - 1
        else:
          left = mid + 1
      else:
        if nums[mid] < target <= nums[right]:
          left = mid + 1
        else:
          right = mid - 1
    return -1

  def binary_search(self, nums: List[int], target: int) -> int:
    """
    A binary search solution that runs in O(logN) in time and constant in space

    Args:
      nums:
      target:

    Returns:

    """
    if not nums:
      return -1
    pivot = 0 if nums[0] < nums[-1] else self.find_pivot(nums)
    first_half = self.partial_binary_search(nums, target, 0, pivot)
    second_half = self.partial_binary_search(nums, target, pivot + 1,
                                             len(nums) - 1)
    if first_half == second_half == -1:
      return -1
    return first_half if first_half != -1 else second_half

  def find_pivot(self, nums):
    low, high = 0, len(nums) - 1
    while low <= high:
      mid = (low + high) // 2
      if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
        return mid
      elif nums[mid] < nums[0]:
        high = mid - 1
      elif nums[mid] > nums[-1]:
        low = mid + 1
      else:
        break
    return 0

  def partial_binary_search(self, nums, target, low, high):
    while low <= high:
      mid = (low + high) // 2
      if nums[mid] == target:
        return mid
      elif nums[mid] > target:
        high = mid - 1
      else:
        low = mid + 1
    return -1

  def search(self, nums: List[int], target: int) -> int:
    """
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

    You are given a target value to search. If found in the array return its index, otherwise return -1.

    You may assume no duplicate exists in the array.

    Your algorithm's runtime complexity must be in the order of O(log n).

    Example 1:

    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4
    Example 2:

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

    Args:
      nums:
      target:

    Returns:

    """
    return self.binary_search(nums, target)