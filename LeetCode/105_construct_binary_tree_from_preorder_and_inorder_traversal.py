"""
Solution for 105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
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
  Runtime: 132 ms, faster than 64.75% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
  Memory Usage: 50.8 MB, less than 71.05% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
  """
  def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    """
    Given preorder and inorder traversal of a tree, construct the binary tree.

    Note:
    You may assume that duplicates do not exist in the tree.

    For example, given

    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    Return the following binary tree:

        3
       / \
      9  20
        /  \
       15   7

    Args:
      preorder:
      inorder:

    Returns:

    """
    if inorder:
      i = inorder.index(preorder.pop(0))
      node = TreeNode(inorder[i])
      node.left = self.buildTree(preorder, inorder[:i])
      node.right = self.buildTree(preorder, inorder[i+1:])
      return node