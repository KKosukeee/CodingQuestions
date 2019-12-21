"""
Solution for 449. Serialize and Deserialize BST
https://leetcode.com/problems/serialize-and-deserialize-bst/
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
  """
  Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

  Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

  The encoded string should be as compact as possible.

  Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

  Submission:
  Runtime: 64 ms, faster than 87.69% of Python3 online submissions for Serialize and Deserialize BST.
  Memory Usage: 17.5 MB, less than 100.00% of Python3 online submissions for Serialize and Deserialize BST.
  """
  def serialize(self, root: TreeNode) -> str:
    """Encodes a tree to a single string.
    """
    return self.postorder_serialize(root)

  def preorder_serialize(self, root: TreeNode) -> str:
    """
    A pre-order serialization that runs in O(N) in time and O(N) in space

    Args:
      root:

    Returns:

    """
    inorder, preorder = [], []

    def rec(node):
      if not node:
        return
      preorder.append(str(node.val))
      rec(node.left)
      inorder.append(str(node.val))
      rec(node.right)

    rec(root)
    return ','.join(inorder) + ':' + ','.join(preorder)

  def postorder_serialize(self, root: TreeNode) -> str:
    """
    A postorder serialization solution that runs in O(N) in time and space

    Args:
      root:

    Returns:

    """
    postorder = []

    def rec(node):
      if not node:
        return
      rec(node.left)
      rec(node.right)
      postorder.append(str(node.val))

    rec(root)
    return ','.join(postorder)

  def deserialize(self, data: str) -> TreeNode:
    """Decodes your encoded data to tree.
    """
    return self.postorder_deserialize(data)

  def preorder_deserialize(self, data: str) -> TreeNode:
    """
    A pre-order deserialization method that runs in O(N^2) in time and O(N) in
    space

    Args:
      data:

    Returns:

    """
    inorder, preorder = data.split(':')
    if not inorder or not preorder:
      return None

    inorder = [int(v) for v in inorder.split(',')]
    preorder = deque([int(v) for v in preorder.split(',')])

    def rec(nums):
      if not nums:
        return None
      val = preorder.popleft()
      pivot = nums.index(val)
      node = TreeNode(val)
      node.left = rec(nums[:pivot])
      node.right = rec(nums[pivot + 1:])
      return node

    return rec(inorder)

  def postorder_deserialize(self, data: str) -> TreeNode:
    """
    A post-order deserialization method that runs in O(N) in time and space

    Args:
      data:

    Returns:

    """
    if not data:
      return None
    stack = [int(v) for v in data.split(',')]

    def rec(lower, upper):
      if not stack or stack[-1] < lower or stack[-1] > upper:
        return None
      val = stack.pop()
      node = TreeNode(val)
      node.right = rec(val, upper)
      node.left = rec(lower, val)
      return node

    return rec(float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))