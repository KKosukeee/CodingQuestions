"""
Solution for 1273. Delete Tree Nodes
https://leetcode.com/problems/delete-tree-nodes/
"""
from collections import defaultdict
from typing import List

class Solution:
  """
  Runtime: 244 ms, faster than 83.40% of Python3 online submissions for Delete Tree Nodes.
  Memory Usage: 27.3 MB, less than 100.00% of Python3 online submissions for Delete Tree Nodes.
  """
  def count_up(self, nodes: int, parent: List[int], value: List[int]) -> int:
    """
    A solution that runs in O(N) in time and O(N) in space

    Args:
      nodes:
      parent:
      value:

    Returns:

    """
    outgoing = defaultdict(list)
    for i in range(len(parent)):
      outgoing[parent[i]].append(i)

    def dfs(node):
      total, count = value[node], 1
      for i in outgoing[node]:
        t, c = dfs(i)
        total += t
        count += c
      return total, count if total else 0

    return dfs(0)[1]

  def count_down(self, nodes: int, parent: List[int], value: List[int]) -> int:
    """
    A solution that runs in O(N) in time and O(N) in space

    Args:
      nodes:
      parent:
      value:

    Returns:

    """
    outgoing = defaultdict(list)
    for i in range(len(parent)):
      outgoing[parent[i]].append(i)
    result = [nodes]

    def dfs(node):
      total, count = value[node], 1
      for i in outgoing[node]:
        t, c = dfs(i)
        total += t
        count += c
      if total == 0:
        result[-1] -= count
        return total, 0
      else:
        return total, count

    dfs(0)
    return result[-1]

  def deleteTreeNodes(self, nodes: int, parent: List[int],
                      value: List[int]) -> int:
    """
    A tree rooted at node 0 is given as follows:

    The number of nodes is nodes;
    The value of the i-th node is value[i];
    The parent of the i-th node is parent[i].
    Remove every subtree whose sum of values of nodes is zero.

    After doing so, return the number of nodes remaining in the tree.



    Example 1:



    Input: nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]
    Output: 2


    Constraints:

    1 <= nodes <= 10^4
    -10^5 <= value[i] <= 10^5
    parent.length == nodes
    parent[0] == -1 which indicates that 0 is the root.

    Args:
      nodes:
      parent:
      value:

    Returns:

    """
    return self.count_up(nodes, parent, value)

    """
    DFS
    T: O(N), S: O(N)
    1. Create a graph by looping through the parent
    2. Traverse the graph, until it reaches to the leaf
      2.1 If the value is zero, then remove the key from the dict
    3. If the current node isn't the leaf, add all values in the children, and update the val in value
    4. Return the length of the dict
    """