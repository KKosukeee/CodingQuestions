"""
Solution for 572. Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  """
  Runtime: 248 ms, faster than 65.00% of Python3 online submissions for Subtree of Another Tree.
  Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Subtree of Another Tree.
  """
  def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    """
    Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

    Example 1:
    Given tree s:

         3
        / \
       4   5
      / \
     1   2
    Given tree t:
       4
      / \
     1   2
    Return true, because t has the same structure and node values with a subtree of s.
    Example 2:
    Given tree s:

         3
        / \
       4   5
      / \
     1   2
        /
       0
    Given tree t:
       4
      / \
     1   2
    Return false.

    Args:
      s:
      t:

    Returns:

    """
    return self.dfs(s, t)

  def dfs(self, s, t):
    """
    A DFS solution that runs in O(ST) in time and O(S+T) in space

    Args:
      s:
      t:

    Returns:

    """
    def rec(node):
      if not node:
        return False
      if node.val == t.val:
        return self.identical(node, t) or rec(node.left) or rec(node.right)
      else:
        return rec(node.left) or rec(node.right)

    return rec(s)

  def identical(self, s, t):
    if not s and not t:
      return True
    if not s or not t:
      return False
    return s.val == t.val and self.identical(s.left, t.left) and self.identical(
      s.right, t.right)