"""
Solution for 270. Closest Binary Search Tree Value
https://leetcode.com/problems/closest-binary-search-tree-value/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  """
  Runtime: 36 ms, faster than 81.61% of Python3 online submissions for Closest Binary Search Tree Value.
  Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Closest Binary Search Tree Value.
  """
  def closestValue(self, root: TreeNode, target: float) -> int:
    """
    Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

    Note:

    Given target value is a floating point.
    You are guaranteed to have only one unique value in the BST that is closest to the target.
    Example:

    Input: root = [4,2,5,1,3], target = 3.714286

        4
       / \
      2   5
     / \
    1   3

    Output: 4

    Args:
      root:
      target:

    Returns:

    """
    return self.bin_search(root, target)

  def linear_search(self, root: TreeNode, target: float) -> int:
    """
    A linear search that runs in O(N) in time and space

    Args:
      root:
      target:

    Returns:

    """
    def inorder(node):
      if not node:
        return []
      return inorder(node.left) + [node.val] + inorder(node.right)

    return min(inorder(root), key=lambda x: abs(x - target))

  def bin_search(self, root: TreeNode, target: float) -> int:
    """
    A solution using binary search that runs in O(log(N)) where N is # of nodes
    in the binary tree and O(1) in space

    Args:
      root:
      target:

    Returns:

    """
    cloest, diff = root.val, abs(root.val - target)
    while root:
      if abs(root.val - target) < diff:
        diff = abs(root.val - target)
        cloest = root.val
      if root.val < target:
        root = root.right
      else:
        root = root.left
    return cloest
