"""
Solution for 236. Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  """
  Runtime: 68 ms, faster than 95.01% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
  Memory Usage: 25.8 MB, less than 38.89% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
  """
  def initial_solution(self, root: 'TreeNode', p: 'TreeNode',
                       q: 'TreeNode') -> 'TreeNode':
    """
    An initial solution using nonlocal variable, which runs in O(N) in time and
    space

    Args:
      root:
      p:
      q:

    Returns:

    """
    lca = None

    def rec(node):
      if not node:
        return 0
      nonlocal lca
      t = rec(node.left) + rec(node.right) + int(node == p) + int(node == q)
      if t == 2 and not lca:
        lca = node
      return t

    rec(root)
    return lca

  def without_nonlocal_solution(self, root: 'TreeNode', p: 'TreeNode',
                                q: 'TreeNode') -> 'TreeNode':
    """
    A solution that doesn't use nonlocal variable that runs same as the initial
    solution

    Args:
      root:
      p:
      q:

    Returns:

    """
    def rec(node):
      if not node:
        return None, 0
      ln, lv = rec(node.left)
      rn, rv = rec(node.right)
      if lv + rv + int(node == p) + int(node == q) == 2:
        if not ln and not rn:
          return node, 2
        return ln or rn, 2
      return None, lv + rv + int(node == p) + int(node == q)

    return rec(root)[0]

  def bool_solution(self, root: 'TreeNode', p: 'TreeNode',
                    q: 'TreeNode') -> 'TreeNode':
    """
    A boolean solution that runs in O(N) in time and space using boolean

    Args:
      root:
      p:
      q:

    Returns:

    """
    self.lca = None

    def rec(node):
      if not node:
        return False
      curr = node == p or node == q
      left = rec(node.left)
      right = rec(node.right)

      if curr + left + right >= 2:
        self.lca = node
      return curr or left or right

    rec(root)
    return self.lca

  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                           q: 'TreeNode') -> 'TreeNode':
    """
    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

    Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]




    Example 1:

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.
    Example 2:

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


    Note:

    All of the nodes' values will be unique.
    p and q are different and both values will exist in the binary tree.

    Args:
      root:
      p:
      q:

    Returns:

    """
    return self.bool_solution(root, p, q)
