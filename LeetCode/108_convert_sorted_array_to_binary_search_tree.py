"""
Solution for 108. Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  """
  Runtime: 64 ms, faster than 84.97% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
  Memory Usage: 15.2 MB, less than 100.00% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
  """
  def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    """
    Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

    For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

    Example:

    Given the sorted array: [-10,-3,0,5,9],

    One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

          0
         / \
       -3   9
       /   /
     -10  5

    Args:
      nums:

    Returns:

    """
    def rec(left, right):
      if not left <= right:
        return None
      mid = (left + right) // 2
      node = TreeNode(nums[mid])
      node.left = rec(left, mid-1)
      node.right = rec(mid+1, right)
      return node
    return rec(0, len(nums)-1)