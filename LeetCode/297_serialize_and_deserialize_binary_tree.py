"""
Solution for 297. Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Codec:
  """
  Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

  Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
  """
  def serialize(self, root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    return self.dfs_preorder_serialize(root)

  def dfs_preorder_serialize(self, root):
    """
    A solution that runs in O(N) in time and space

    Args:
      root:

    Returns:

    """
    def rec(node):
      if not node:
        return 'None,'
      s = '{},'.format(node.val)
      s += rec(node.left)
      s += rec(node.right)
      return s

    return rec(root)

  def bfs_tle_serialize(self, root):
    """
    A solution that runs in O(2^D) where D is the depth of the tree in time and
    space

    Args:
      root:

    Returns:

    """
    q, res = deque([root]), []
    while True:
      all_none = True
      temp = deque()
      while q:
        node = q.popleft()
        if node:
          temp.extend([node.left, node.right])
          if all_none and (node.left or node.right):
            all_none = False
        else:
          temp.extend([None, None])
        res.append(str(node.val) if node else 'None')
      if all_none:
        break
      q = temp
    return ','.join(res)

  def deserialize(self, data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    return self.dfs_preorder_deserialize(data)

  def dfs_preorder_deserialize(self, root):
    """
    A solution that runs in O(N) in time and space

    Args:
      root:

    Returns:

    """
    q = deque(root.split(','))

    def rec():
      if q[0] == 'None':
        _ = q.popleft()
        return None
      root = TreeNode(q[0])
      _ = q.popleft()
      root.left = rec()
      root.right = rec()
      return root

    root = rec()
    return root

  def bfs_tle_deserialize(self, data):
    """
    A solution that runs in O(2^D) where D is the depth of the tree in time and
    space

    Args:
      data:

    Returns:

    """
    nodes = data.split(',')

    def rec(i):
      if not i < len(nodes):
        return None
      if nodes[i] == 'None':
        return None
      node = TreeNode(nodes[i])
      node.left = rec(i + (i + 1))
      node.right = rec(i + (i + 2))
      return node

    return rec(0)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))