"""
Solution for 111. Minimum Depth of Binary Tree
https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:
  """
  Runtime: 40 ms, faster than 94.15% of Python3 online submissions for Minimum Depth of Binary Tree.
  Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Minimum Depth of Binary Tree.
  """
  def bfs(self, root: TreeNode) -> int:
    """
    A BFS solution that runs in O(N)

    Args:
      root:

    Returns:

    """
    if not root:
      return 0
    queue = deque([(root, 1)])
    while queue:
      node, level = queue.popleft()
      if not node.left and not node.right:
        return level
      if node.left:
        queue.append((node.left, level + 1))
      if node.right:
        queue.append((node.right, level + 1))
    return -1

  def dfs(self, root: TreeNode) -> int:
    """
    A DFS solution that runs in O(N) in time and space

    Args:
      root:

    Returns:

    """
    if not root:
      return 0

    def dfs(node):
      if not node:
        return float('inf')
      if not node.left and not node.right:
        return 1
      return min(dfs(node.left), dfs(node.right)) + 1

    return dfs(root)

  def minDepth(self, root: TreeNode) -> int:
    """
    Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

    Note: A leaf is a node with no children.

    Example:

    Given binary tree [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
    return its minimum depth = 2.

    Args:
      root:

    Returns:

    """
    return self.bfs(root)