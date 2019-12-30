"""
Solution for 307. Range Sum Query - Mutable
https://leetcode.com/problems/range-sum-query-mutable/
"""
from typing import List

class SegNode:
  def __init__(self, start, end):
    self.start = start
    self.end = end
    self.left = None
    self.right = None
    self.sum = 0


class NumArray:
  """
  Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

  The update(i, val) function modifies nums by updating the element at index i to val.

  Example:

  Given nums = [1, 3, 5]

  sumRange(0, 2) -> 9
  update(1, 2)
  sumRange(0, 2) -> 8
  Note:

  The array is only modifiable by the update function.
  You may assume the number of calls to update and sumRange function is distributed evenly.
  """
  def __init__(self, nums: List[int]):
    self.build_segtree(nums)

  def build_segtree(self, nums):
    def rec(start, end):
      if start > end:
        return None

      node = SegNode(start, end)
      if start == end:
        node.sum = nums[start]
      else:
        mid = (start + end) // 2
        node.left = rec(start, mid)
        node.right = rec(mid + 1, end)
        node.sum = node.left.sum + node.right.sum

      return node

    self.root = rec(0, len(nums) - 1)

  def update(self, i: int, val: int) -> None:
    def bin_search(node):
      if node.start == node.end:
        node.sum = val
      else:
        mid = (node.start + node.end) // 2
        if i <= mid:
          bin_search(node.left)
        else:
          bin_search(node.right)
        node.sum = node.left.sum + node.right.sum

    bin_search(self.root)

  def sumRange(self, i: int, j: int) -> int:
    def rec(node, start, end):
      if node.start == start and node.end == end:
        return node.sum
      mid = (node.start + node.end) // 2
      if end <= mid:
        return rec(node.left, start, end)
      elif start >= mid + 1:
        return rec(node.right, start, end)
      else:
        return rec(node.left, start, mid) + rec(node.right, mid + 1, end)

    return rec(self.root, i, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)