"""
Solution for 285. Inorder Successor in BST
https://leetcode.com/problems/inorder-successor-in-bst/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import bisect

class Solution:
  """
  Runtime: 68 ms, faster than 94.97% of Python3 online submissions for Inorder Successor in BST.
  Memory Usage: 16.7 MB, less than 100.00% of Python3 online submissions for Inorder Successor in BST.
  """
  def initial_solution(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
    """
    An initial solution that runs in O(N) in time and O(N) in space

    Args:
      root:
      p:

    Returns:

    """
    if not root:
      return None
    nodes, vals, stack = [], [], [root]
    v = p.val

    def dfs(node):
      if not node:
        return None
      dfs(node.left)
      nodes.append(node)
      vals.append(node.val)
      dfs(node.right)

    dfs(root)
    i = bisect.bisect_right(vals, v)
    return nodes[i] if i < len(nodes) else None

  def better_solution(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
    """
    The better solution that runs in O(N) in time and O(1) in space

    Args:
      root:
      p:

    Returns:

    """
    cand = None
    while root:
      if p.val < root.val:
        cand = root
        root = root.left
      elif p.val >= root.val:
        root = root.right
    return cand

  def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
    """
    Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

    The successor of a node p is the node with the smallest key greater than p.val.



    Example 1:


    Input: root = [2,1,3], p = 1
    Output: 2
    Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
    Example 2:


    Input: root = [5,3,6,2,4,null,null,1], p = 6
    Output: null
    Explanation: There is no in-order successor of the current node, so the answer is null.


    Note:

    If the given node has no in-order successor in the tree, return null.
    It's guaranteed that the values of the tree are unique.

    Args:
      root:
      p:

    Returns:

    """
    return self.better_solution(root, p)