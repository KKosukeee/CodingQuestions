"""
Solution for 426. Convert Binary Search Tree to Sorted Doubly Linked List
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
  """
  Runtime: 28 ms, faster than 98.68% of Python3 online submissions for Convert Binary Search Tree to Sorted Doubly Linked List.
  Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Convert Binary Search Tree to Sorted Doubly Linked List.
  """
  def linear_solution(self, root: 'Node') -> 'Node':
    """
    A linear solution that runs in O(N) in time and O(N) in space

    Args:
      root:

    Returns:

    """
    if not root:
      return None
    nodes = []

    def rec(node):
      if node:
        rec(node.left)
        nodes.append(node)
        rec(node.right)

    rec(root)
    for i in range(len(nodes) - 1):
      nodes[i].right = nodes[i + 1]
    for i in range(len(nodes) - 1, 0, -1):
      nodes[i].left = nodes[i - 1]
    nodes[0].left = nodes[-1]
    nodes[-1].right = nodes[0]
    return nodes[0]

  def one_pass_solution(self, root: 'Node') -> 'Node':
    """
    A one pass solution that runs in O(N) in time and space

    Args:
      root:

    Returns:

    """
    first, last = None, None

    def rec(node):
      nonlocal first, last
      if node:
        rec(node.left)
        if last:
          last.right = node
          node.left = last
        else:
          first = node
        last = node
        rec(node.right)

    if not root:
      return None
    rec(root)
    last.right = first
    first.left = last
    return first

  def treeToDoublyList(self, root: 'Node') -> 'Node':
    """
    Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

    You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

    We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.



    Example 1:



    Input: root = [4,2,5,1,3]


    Output: [1,2,3,4,5]

    Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

    Example 2:

    Input: root = [2,1,3]
    Output: [1,2,3]
    Example 3:

    Input: root = []
    Output: []
    Explanation: Input is an empty tree. Output is also an empty Linked List.
    Example 4:

    Input: root = [1]
    Output: [1]


    Constraints:

    -1000 <= Node.val <= 1000
    Node.left.val < Node.val < Node.right.val
    All values of Node.val are unique.
    0 <= Number of Nodes <= 2000

    Args:
      root:

    Returns:

    """
    return self.one_pass_solution(root)