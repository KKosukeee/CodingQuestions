"""
Solution for 1302. Deepest Leaves Sum
https://leetcode.com/problems/deepest-leaves-sum/
"""
from collections import defaultdict
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  """
  Runtime: 84 ms, faster than 94.52% of Python3 online submissions for Deepest Leaves Sum.
  Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Deepest Leaves Sum.
  """
  def deepestLeavesSum(self, root: TreeNode) -> int:
    """
    Given a binary tree, return the sum of values of its deepest leaves.


    Example 1:



    Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
    Output: 15


    Constraints:

    The number of nodes in the tree is between 1 and 10^4.
    The value of nodes is between 1 and 100.

    Args:
      root:

    Returns:

    """
    return self.bfs(root)

  def dfs(self, root: TreeNode) -> int:
    """
    A DFS solution that runs in O(N) in time and O(N) in space

    Args:
      root:

    Returns:

    """
    sum_map = defaultdict(int)

    def dfs(node, level):
      if node:
        dfs(node.left, level + 1)
        sum_map[level] += node.val
        dfs(node.right, level + 1)

    dfs(root, 0)
    return sum_map[max(sum_map.keys())]

  def bfs(self, root: TreeNode) -> int:
    """
    A BFS solution that runs in O(N) in time and O(N) in space

    Args:
      root:

    Returns:

    """
    if not root:
      return 0
    q = deque([root])
    while q:
      res, temp = 0, deque()
      while q:
        node = q.popleft()
        res += node.val
        if node.left:
          temp.append(node.left)
        if node.right:
          temp.append(node.right)
      q = temp
    return res