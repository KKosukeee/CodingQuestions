"""
Solution for 75. Sort Colors
https://leetcode.com/problems/sort-colors/
"""
from typing import List

class Solution:
  """
  Runtime: 28 ms, faster than 97.14% of Python3 online submissions for Sort Colors.
  Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Sort Colors.
  """
  def violated_solution(self, nums: List[int]) -> None:
    """
    A solution that violates the problem constraint
    It run in O(Nlog(N)) in time, and O(1) in space.

    Args:
      nums:

    Returns:

    """
    nums.sort()

  def count_sort(self, nums: List[int]) -> None:
    """
    A solution that runs in O(N), in time and space

    Args:
      nums:

    Returns:

    """
    counts = [0, 0, 0]
    for num in nums:
      counts[num] += 1
    for i in range(1, len(counts)):
      counts[i] += counts[i - 1]

    for num in nums[:]:
      nums[counts[num] - 1] = num
      counts[num] -= 1

  def follow_up(self, nums: List[int]) -> None:
    """
    A solution that runs in O(N) in time and O(1) in space

    Args:
      nums:

    Returns:

    """
    p1, p2 = 0, len(nums) - 1
    curr = 0
    while curr <= p2:
      if nums[curr] == 2:
        nums[curr], nums[p2] = nums[p2], nums[curr]
        p2 -= 1
      elif nums[curr] == 0:
        nums[curr], nums[p1] = nums[p1], nums[curr]
        curr, p1 = curr + 1, p1 + 1
      else:
        curr += 1

  def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.

    Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

    Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

    Note: You are not suppose to use the library's sort function for this problem.

    Example:

    Input: [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
    Follow up:

    A rather straight forward solution is a two-pass algorithm using counting sort.
    First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
    Could you come up with a one-pass algorithm using only constant space?
    """
    self.follow_up(nums)

  """
  Count sort algorithm
  1. Count frequency of all values
  2. Take the cumulative sum on the buckets
  3. Loop through the input nums
    3.1. Get the index of the current val by looking up the index
    3.2. Decrement the index number by one
    3.3. Swap the 
  """