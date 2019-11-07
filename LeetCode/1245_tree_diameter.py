"""
Solution for 1245. Tree Diameter
https://leetcode.com/problems/tree-diameter/
"""
from collections import defaultdict
from typing import List

class Solution:
    """
    Runtime: 188 ms, faster than 98.02% of Python3 online submissions for Tree Diameter.
    Memory Usage: 17.4 MB, less than 100.00% of Python3 online submissions for Tree Diameter.
    """
    def dfs(self, edges: List[List[int]]) -> int:
        """
        A DFS solution that runs in TLE

        Args:
            edges:

        Returns:

        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, visited):
            if node in visited:
                return -1
            max_depth = -1
            visited.add(node)
            for adjacent in graph[node]:
                max_depth = max(max_depth, dfs(adjacent, visited))
            return max_depth + 1

        max_depth = 0
        for node in range(len(edges) + 1):
            max_depth = max(max_depth, dfs(node, set()))
        return max_depth

    def optimal(self, edges: List[List[int]]) -> int:
        """
        An optimal solution that runs in O(N)

        Args:
            edges:

        Returns:

        """
        graph, self.max_depth = defaultdict(list), 0
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):
            d1, d2 = 0, 0
            for adjacent in graph[node]:
                if adjacent != parent:
                    d = dfs(adjacent, node)
                    if d > d1:
                        d1, d2 = d, d1
                    elif d > d2:
                        d2 = d
                self.max_depth = max(self.max_depth, d1 + d2)
            return d1 + 1

        dfs(0, None)
        return self.max_depth

    def treeDiameter(self, edges: List[List[int]]) -> int:
        """
        Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.

        The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.



        Example 1:



        Input: edges = [[0,1],[0,2]]
        Output: 2
        Explanation:
        A longest path of the tree is the path 1 - 0 - 2.
        Example 2:



        Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
        Output: 4
        Explanation:
        A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.


        Constraints:

        0 <= edges.length < 10^4
        edges[i][0] != edges[i][1]
        0 <= edges[i][j] <= edges.length
        The given edges form an undirected tree.

        Args:
            edges:

        Returns:

        """
        return self.optimal(edges)