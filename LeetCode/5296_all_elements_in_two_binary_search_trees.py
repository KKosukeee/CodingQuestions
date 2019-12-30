"""
Solution for 5296. All Elements in Two Binary Search Trees
https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
"""
import bisect
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  """
  Runtime: 344 ms, faster than 100.00% of Python3 online submissions for All Elements in Two Binary Search Trees.
  Memory Usage: 15.9 MB, less than 100.00% of Python3 online submissions for All Elements in Two Binary Search Trees.
  """
  def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
    """
    Given two binary search trees root1 and root2.

    Return a list containing all the integers from both trees sorted in ascending order.



    Example 1:


    Input: root1 = [2,1,4], root2 = [1,0,3]
    Output: [0,1,1,2,3,4]
    Example 2:

    Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
    Output: [-10,0,0,1,2,5,7,10]
    Example 3:

    Input: root1 = [], root2 = [5,1,7,0,2]
    Output: [0,1,2,5,7]
    Example 4:

    Input: root1 = [0,-10,10], root2 = []
    Output: [-10,0,10]
    Example 5:


    Input: root1 = [1,null,8], root2 = [8,1]
    Output: [1,1,8,8]


    Constraints:

    Each tree has at most 5000 nodes.
    Each node's value is between [-10^5, 10^5].

    Args:
      root1:
      root2:

    Returns:

    """
    return self.optimal_solution(root1, root2)

  def initial_solution(self, root1: TreeNode, root2: TreeNode) -> List[int]:
    """
    An initial solution that runs in O(N+MLog(N+M)) in time and O(max(N, M)) in space

    Args:
      root1:
      root2:

    Returns:

    """
    res = []

    def dfs(node):
      if not node:
        return
      dfs(node.left)
      bisect.insort(res, node.val)
      dfs(node.right)

    dfs(root1)
    dfs(root2)
    return res

  def better_solution(self, root1: TreeNode, root2: TreeNode) -> List[int]:
    """
    A better solution that runs in O(N+M) in time and O(max(N,M)) in space

    Args:
      root1:
      root2:

    Returns:

    """
    def inorder(root):
      if not root:
        return []
      ls = inorder(root.left)
      ls.append(root.val)
      ls.extend(inorder(root.right))
      return ls

    bst1 = inorder(root1)
    bst2 = inorder(root2)
    i, j, res = 0, 0, []

    while i < len(bst1) and j < len(bst2):
      if bst1[i] <= bst2[j]:
        res.append(bst1[i])
        i += 1
      else:
        res.append(bst2[j])
        j += 1

    if i < len(bst1):
      while i < len(bst1):
        res.append(bst1[i])
        i += 1
    if j < len(bst2):
      while j < len(bst2):
        res.append(bst2[j])
        j += 1
    return res

  def optimal_solution(self, root1: TreeNode, root2: TreeNode) -> List[int]:
    """
    An optimal approach that runs in O(N+M) in time and O(1) in space

    Args:
      root1:
      root2:

    Returns:

    """
    iter1 = self.inorder_traversal(root1)
    iter2 = self.inorder_traversal(root2)
    v1, v2, res = next(iter1, None), next(iter2, None), []

    while v1 or v2:
      if not v2 or (v1 and v1.val <= v2.val):
        res.append(v1.val)
        v1 = next(iter1, None)
      else:
        res.append(v2.val)
        v2 = next(iter2, None)
    return res

  def inorder_traversal(self, root):
    stack = []
    while root or stack:
      while root:
        stack.append(root)
        root = root.left
      node = stack.pop()
      yield node
      root = node.right