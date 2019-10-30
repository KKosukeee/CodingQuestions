"""
Solution for 797. All Paths From Source to Target
https://leetcode.com/problems/all-paths-from-source-to-target/
"""
from typing import List
class Solution:
    """
    Runtime: 116 ms, faster than 90.89% of Python3 online submissions for All Paths From Source to Target.
    Memory Usage: 15.1 MB, less than 30.00% of Python3 online submissions for All Paths From Source to Target.
    """
    def backtrack(self, graph: List[List[int]]) -> List[List[int]]:
        """
        A backtrack solution that run in O(N^M) where M = max(connected nodes at i), and O(N) in space due to the recursion stack

        Args:
            graph:

        Returns:

        """
        paths = []

        def rec(i, path):
            if i == len(graph) - 1:
                paths.append(path)
                return
            for node in graph[i]:
                rec(node, path + [node])

        rec(0, [0])
        return paths

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

        The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

        Example:
        Input: [[1,2], [3], [3], []]
        Output: [[0,1,3],[0,2,3]]
        Explanation: The graph looks like this:
        0--->1
        |    |
        v    v
        2--->3
        There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
        Note:

        The number of nodes in the graph will be in the range [2, 15].
        You can print different paths in any order, but you should keep the order of nodes inside one path.

        Args:
            graph:

        Returns:

        """
        return self.backtrack(graph)

    """
    Backtracking
    T: O(N^N), S: O(N)
    1. Given the first node loop through connected node
    2. Call backtrack function with the connected node
    3. Append whenever the current node is the goal node
    """