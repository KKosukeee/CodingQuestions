"""
Solution for 303. Range Sum Query - Immutable
https://leetcode.com/problems/range-sum-query-immutable/
"""
from typing import List

class NumArray:
  """
  Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

  Example:
  Given nums = [-2, 0, 3, -5, 2, -1]

  sumRange(0, 2) -> 1
  sumRange(2, 5) -> -1
  sumRange(0, 5) -> -3
  Note:
  You may assume that the array does not change.
  There are many calls to sumRange function.
  """
  def __init__(self, nums: List[int]):
    self.cum_sum = [0]
    for num in nums:
      self.cum_sum.append(self.cum_sum[-1] + num)

  def sumRange(self, i: int, j: int) -> int:
    return self.cum_sum[j + 1] - self.cum_sum[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)