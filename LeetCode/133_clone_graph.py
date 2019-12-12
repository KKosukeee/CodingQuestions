"""
Solution for 133. Clone Graph
https://leetcode.com/problems/clone-graph/
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

from copy import deepcopy
from collections import deque

class Solution:
  """
  Runtime: 36 ms, faster than 89.98% of Python3 online submissions for Clone Graph.
  Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Clone Graph.
  """
  def dfs_copy_solution(self, node: 'Node') -> 'Node':
    """
    A DFS solution that runs in O(N) in time and O(N) in space

    Args:
      node:

    Returns:

    """
    visited = {}

    def rec(node):
      if not node:
        return node

      if node in visited:
        return visited[node]

      visited[node] = Node(node.val, [])
      if node.neighbors:
        visited[node].neighbors = [rec(neigh) for neigh in node.neighbors]

      return visited[node]

    return rec(node)

  def bfs_copy_solution(self, node: 'Node') -> 'Node':
    """
    A BFS solution that runs in O(N) in time and space

    Args:
      node:

    Returns:

    """
    if not node:
      return node
    q = deque([node])
    visited = {node: Node(node.val, [])}

    while q:
      n = q.popleft()
      for neigh in n.neighbors:
        if neigh not in visited:
          visited[neigh] = Node(neigh.val, [])
          q.append(neigh)
        visited[n].neighbors.append(visited[neigh])
    return visited[node]

  def hack_solution(self, node: 'Node') -> 'Node':
    """
    A cheat solution that runs in O(N) in time and space

    Args:
      node:

    Returns:

    """
    return deepcopy(node)

  def cloneGraph(self, node: 'Node') -> 'Node':
    """
    Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.



    Example:



    Input:
    {"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

    Explanation:
    Node 1's value is 1, and it has two neighbors: Node 2 and 4.
    Node 2's value is 2, and it has two neighbors: Node 1 and 3.
    Node 3's value is 3, and it has two neighbors: Node 2 and 4.
    Node 4's value is 4, and it has two neighbors: Node 1 and 3.


    Note:

    The number of nodes will be between 1 and 100.
    The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
    Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
    You must return the copy of the given node as a reference to the cloned graph.

    Args:
      node:

    Returns:

    """
    return self.hack_solution(node)