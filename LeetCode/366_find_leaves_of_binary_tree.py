"""
Solution for 366. Find Leaves of Binary Tree
https://leetcode.com/problems/find-leaves-of-binary-tree/
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
  Runtime: 24 ms, faster than 99.36% of Python3 online submissions for Find Leaves of Binary Tree.
  Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find Leaves of Binary Tree.
  """
  def findLeaves(self, root: TreeNode) -> List[List[int]]:
    """
    Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.



    Example:

    Input: [1,2,3,4,5]

              1
             / \
            2   3
           / \
          4   5

    Output: [[4,5,3],[2],[1]]


    Explanation:

    1. Removing the leaves [4,5,3] would result in this tree:

              1
             /
            2


    2. Now removing the leaf [2] would result in this tree:

              1


    3. Now removing the leaf [1] would result in the empty tree:

              []
    Args:
      root:

    Returns:

    """
    result = []
    def dfs(node):
        if not node:
            return -1
        level = max(dfs(node.left), dfs(node.right))
        if not level < len(result):
            result.append([])
        result[level].append(node.val)
        return level + 1
    if not root:
        return []
    dfs(root)
    return result