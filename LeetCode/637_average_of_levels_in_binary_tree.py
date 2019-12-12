"""
Solution for 637. Average of Levels in Binary Tree
https://leetcode.com/problems/average-of-levels-in-binary-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
from typing import List

class Solution:
  """
  Runtime: 44 ms, faster than 95.82% of Python3 online submissions for Average of Levels in Binary Tree.
  Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Average of Levels in Binary Tree.
  """
  def bfs_solution(self, root: TreeNode) -> List[float]:
    """
    A BFS solution that runs in O(N) in time and O(N) in space

    Args:
      root:

    Returns:

    """
    result, q = [], deque([root])
    while q:
      s, t = 0, 0
      temp = deque()
      while q:
        node = q.popleft()
        if node:
          s += node.val
          t += 1
          temp.append(node.left)
          temp.append(node.right)
      if t != 0:
        result.append(s / t)
      q = temp
    return result

  def dfs_solution(self, root: TreeNode) -> List[float]:
    """
    A DFS solution that runs in O(N) in time and space

    Args:
      root:

    Returns:

    """
    levels = []

    def dfs(node, level):
      if not node:
        return
      if level == len(levels):
        levels.append([])
      levels[level].append(node.val)
      dfs(node.left, level + 1)
      dfs(node.right, level + 1)

    dfs(root, 0)
    return [sum(level) / len(level) for level in levels]

  def optimized_dfs_solution(self, root: TreeNode) -> List[float]:
    """
    An optimized DFS solution that runs in O(N) in time and spac

    Args:
      root:

    Returns:

    """
    levels = []

    def dfs(node, level):
      if not node:
        return
      if level == len(levels):
        levels.append((0, 0))
      s, t = levels[level]
      levels[level] = (s + node.val, t + 1)
      dfs(node.left, level + 1)
      dfs(node.right, level + 1)

    dfs(root, 0)
    return [s / t for s, t in levels]

  def averageOfLevels(self, root: TreeNode) -> List[float]:
    """
    Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
    Example 1:
    Input:
        3
       / \
      9  20
        /  \
       15   7
    Output: [3, 14.5, 11]
    Explanation:
    The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
    Note:
    The range of node's value is in the range of 32-bit signed integer.

    Args:
      root:

    Returns:

    """
    return self.bfs_solution(root)