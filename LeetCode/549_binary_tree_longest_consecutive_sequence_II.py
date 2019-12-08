"""
Solution for 549. Binary Tree Longest Consecutive Sequence II
https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  """
  Runtime: 44 ms, faster than 99.01% of Python3 online submissions for Binary Tree Longest Consecutive Sequence II.
  Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for Binary Tree Longest Consecutive Sequence II.
  """
  def longestConsecutive(self, root: TreeNode) -> int:
    """
    Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

    Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

    Example 1:

    Input:
            1
           / \
          2   3
    Output: 2
    Explanation: The longest consecutive path is [1, 2] or [2, 1].


    Example 2:

    Input:
            2
           / \
          1   3
    Output: 3
    Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].


    Note: All the values of tree nodes are in the range of [-1e7, 1e7].

    Args:
      root:

    Returns:

    """
    def rec(node):
      if not node:
        return 0, 0, 0
      inc, dec = 1, 1
      li, ld, lt = rec(node.left)

      if node.left:
        if node.left.val - node.val == 1:
          inc = li + 1
        if node.val - node.left.val == 1:
          dec = ld + 1

      ri, rd, rt = rec(node.right)
      if node.right:
        if node.right.val - node.val == 1:
          inc = max(inc, ri + 1)
        if node.val - node.right.val == 1:
          dec = max(dec, rd + 1)
      return inc, dec, max(inc + dec - 1, lt, rt)

    return max(rec(root))
