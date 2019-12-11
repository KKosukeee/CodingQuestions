"""
Solution for 314. Binary Tree Vertical Order Traversal
https://leetcode.com/problems/binary-tree-vertical-order-traversal/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
from collections import defaultdict
from typing import List

class Solution:
  """
  Runtime: 20 ms, faster than 99.72% of Python3 online submissions for Binary Tree Vertical Order Traversal.
  Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Tree Vertical Order Traversal.
  """
  def initial_solution(self, root: TreeNode) -> List[List[int]]:
    """
    An initial solution that runs in O(NLogN) in time and O(N) in space

    Args:
      root:

    Returns:

    """
    queue, col_map = deque([(root, 0)]), defaultdict(list)
    while queue:
      node, col = queue.popleft()
      if node:
        col_map[col].append(node.val)
        queue.append((node.left, col - 1))
        queue.append((node.right, col + 1))

    return [col_map[key] for key in sorted(col_map.keys())]

  def verticalOrder(self, root: TreeNode) -> List[List[int]]:
    """
    Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

    If two nodes are in the same row and column, the order should be from left to right.

    Examples 1:

    Input: [3,9,20,null,null,15,7]

       3
      /\
     /  \
     9  20
        /\
       /  \
      15   7

    Output:

    [
      [9],
      [3,15],
      [20],
      [7]
    ]
    Examples 2:

    Input: [3,9,8,4,0,1,7]

         3
        /\
       /  \
       9   8
      /\  /\
     /  \/  \
     4  01   7

    Output:

    [
      [4],
      [9],
      [3,0,1],
      [8],
      [7]
    ]
    Examples 3:

    Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

         3
        /\
       /  \
       9   8
      /\  /\
     /  \/  \
     4  01   7
        /\
       /  \
       5   2

    Output:

    [
      [4],
      [9,5],
      [3,0,1],
      [8,2],
      [7]
    ]

    Args:
      root:

    Returns:

    """
    return self.initial_solution(root)
