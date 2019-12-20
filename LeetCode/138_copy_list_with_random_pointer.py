"""
Solution for 138. Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/
"""
from copy import deepcopy

# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
  """
  Runtime: 28 ms, faster than 99.66% of Python3 online submissions for Copy List with Random Pointer.
  Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Copy List with Random Pointer.
  """
  def initial_solution(self, head: 'Node') -> 'Node':
    """
    An initial solution that runs in O(N) time and space

    Args:
      head:

    Returns:

    """
    dummy = Node(0, head, None)
    node_map = {None: None}
    while head:
      if head not in node_map:
        node_map[head] = Node(head.val, None, None)
      if head.random and head.random not in node_map:
        node_map[head.random] = Node(head.random.val, None, None)
      node_map[head].random = node_map[head.random]
      if head.next and head.next not in node_map:
        node_map[head.next] = Node(head.next.val, None, None)
      node_map[head].next = node_map[head.next]
      head = head.next
    return node_map[dummy.next]

  def recursive_solution(self, head: 'Node') -> 'Node':
    """
    A simple recursive solution that runs in O(N) in time and space

    Args:
      head:

    Returns:

    """
    visited = {}

    def rec(node):
      if not node:
        return None
      if node in visited:
        return visited[node]
      visited[node] = Node(node.val, None, None)
      visited[node].next = rec(node.next)
      visited[node].random = rec(node.random)
      return visited[node]

    return rec(head)

  def cheat_solution(self, head: 'Node') -> 'Node':
    """
    A cheating solution that runs in O(N) in time and space

    Args:
      head:

    Returns:

    """
    return deepcopy(head)

  def copyRandomList(self, head: 'Node') -> 'Node':
    """
    A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

    Return a deep copy of the list.

    The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.


    Example 1:


    Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    Example 2:


    Input: head = [[1,1],[2,1]]
    Output: [[1,1],[2,1]]
    Example 3:



    Input: head = [[3,null],[3,0],[3,null]]
    Output: [[3,null],[3,0],[3,null]]
    Example 4:

    Input: head = []
    Output: []
    Explanation: Given linked list is empty (null pointer), so return null.


    Constraints:

    -10000 <= Node.val <= 10000
    Node.random is null or pointing to a node in the linked list.
    Number of Nodes will not exceed 1000.

    Args:
      head:

    Returns:

    """
    return self.initial_solution(head)
