"""
Solution for 31. Next Permutation
https://leetcode.com/problems/next-permutation/
"""
from typing import List

class Solution:
  """
  Runtime: 36 ms, faster than 96.01% of Python3 online submissions for Next Permutation.
  Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Next Permutation.
  """
  def nextPermutation(self, nums: List[int]) -> None:
    """
    Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

    If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

    The replacement must be in-place and use only constant extra memory.

    Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
    """
    if len(nums) <= 1:
      return nums
    i = len(nums)-2
    while i >= 0 and nums[i+1] <= nums[i]:
      i -= 1
    if not i >= 0:
      nums.reverse()
      return
    j = len(nums)-1
    while j >= 0 and nums[j] <= nums[i]:
      j -= 1
    nums[i], nums[j] = nums[j], nums[i]
    nums[i+1:] = reversed(nums[i+1:])