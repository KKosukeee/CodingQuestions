"""
Solution for 261. Graph Valid Tree
https://leetcode.com/problems/graph-valid-tree/
"""
from typing import List

class Solution:
    """
    Runtime: 108 ms, faster than 77.15% of Python3 online submissions for Graph Valid Tree.
    Memory Usage: 14.9 MB, less than 22.22% of Python3 online submissions for Graph Valid Tree.
    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

        Example 1:

        Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
        Output: true
        Example 2:

        Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
        Output: false
        Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.

        Args:
            n(int):
            edges(list[list[int]]):

        Returns:
            bool:

        """
        parents = [i for i in range(n)]
        rank = [0 for i in range(n)]

        def find(p):
            """
            Find the parent

            Args:
                p(int):

            Returns:
                int:

            """
            if parents[p] != p:
                parents[p] = find(parents[p])
            return parents[p]

        def union(edge):
            """
            Union the subsets

            Args:
                edge(list[int]):

            Returns:
                bool:

            """
            p, q = edge
            p1, p2 = find(p), find(q)
            if p1 == p2:
                return False
            if rank[p1] < rank[p2]:
                parents[p1] = p2
            elif rank[p1] > rank[p2]:
                parents[p2] = p1
            else:
                parents[p1] = p2
                rank[p2] += 1
            return True

        return len(edges) == n - 1 and all(map(union, edges))

    # [0,1,2,3,4]
    # [1,1,1,1,1]
    # [0,1,0,0,0]
    # [3,2,3,3,4]
    # [1,2,3,4,4]
    # [1,2,3,4,4]

    # [0,1,2,3,4]
    # [1,1,1,1,1]
    # [0,1,0,0,0]

    # [0,1,2]
    # [1,2,2]