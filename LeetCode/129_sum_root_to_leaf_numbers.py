"""
Solution for 129. Sum Root to Leaf Numbers
https://leetcode.com/problems/sum-root-to-leaf-numbers/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  """
  Runtime: 24 ms, faster than 95.57% of Python3 online submissions for Sum Root to Leaf Numbers.
  Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Sum Root to Leaf Numbers.
  """
  def sumNumbers(self, root: TreeNode) -> int:
    """
    Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

    An example is the root-to-leaf path 1->2->3 which represents the number 123.

    Find the total sum of all root-to-leaf numbers.

    Note: A leaf is a node with no children.

    Example:

    Input: [1,2,3]
        1
       / \
      2   3
    Output: 25
    Explanation:
    The root-to-leaf path 1->2 represents the number 12.
    The root-to-leaf path 1->3 represents the number 13.
    Therefore, sum = 12 + 13 = 25.
    Example 2:

    Input: [4,9,0,5,1]
        4
       / \
      9   0
     / \
    5   1
    Output: 1026
    Explanation:
    The root-to-leaf path 4->9->5 represents the number 495.
    The root-to-leaf path 4->9->1 represents the number 491.
    The root-to-leaf path 4->0 represents the number 40.
    Therefore, sum = 495 + 491 + 40 = 1026.

    Args:
      root:

    Returns:

    """
    return self.other_solution(root)

  def initial_solution(self, root: TreeNode) -> int:
    """
    An initial solution that runs in O(N) where N = # of nodes in the BT and
    O(N) in space

    Args:
      root:

    Returns:

    """
    nums = []

    def rec(node, curr):
      if not node:
        return
      if not node.left and not node.right:
        nums.append(curr * 10 + node.val)
        return
      rec(node.left, curr * 10 + node.val)
      rec(node.right, curr * 10 + node.val)

    rec(root, 0)
    return sum(nums)

  def one_pass(self, root: TreeNode) -> int:
    """
    A one pass solution that runs in O(N) in time and space

    Args:
      root:

    Returns:

    """
    self.res = 0

    def rec(node, curr):
      if not node:
        return
      elif not node.left and not node.right:
        self.res += curr * 10 + node.val
      elif node:
        rec(node.left, curr * 10 + node.val)
        rec(node.right, curr * 10 + node.val)

    rec(root, 0)
    return self.res

  def other_solution(self, root: TreeNode) -> int:
    """
    An other solution that rusn in O(N) in time and space

    Args:
      root:

    Returns:

    """
    def rec(node, curr):
      if not node:
        return 0
      if not node.left and not node.right:
        return curr * 10 + node.val
      return rec(node.left, curr * 10 + node.val) + rec(node.right,
                                                        curr * 10 + node.val)

    return rec(root, 0)