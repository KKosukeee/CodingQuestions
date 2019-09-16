"""
Solution for 323. Number of Connected Components in an Undirected Graph
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
"""
from collections import deque
from collections import defaultdict
from typing import List

class Solution:
    """
    Runtime: 124 ms, faster than 49.07% of Python3 online submissions for Number of Connected Components in an Undirected Graph.
    Memory Usage: 15.2 MB, less than 100.00% of Python3 online submissions for Number of Connected Components in an Undirected Graph.
    """
    def union_find(self, n, edges):
        """
        Solves the problem using Union-Find that runs in O(N + Mlog(N)) where N = n, M = len(edges))

        Args:
            n(int):
            edges(list[list[int]]):

        Returns:
            int:

        """

        parents = [i for i in range(n)]
        rank = [0 for _ in range(n)]

        def find(p):
            if parents[p] != p:
                parents[p] = find(parents[p])
            return parents[p]

        def union(p, q):
            p1, p2 = find(p), find(q)
            if rank[p1] == rank[p2]:
                parents[p1] = p2
                rank[p2] += 1
            elif rank[p1] > rank[p2]:
                parents[p2] = p1
            else:
                parents[p1] = p2

        for p, q in edges:
            union(p, q)
        return len(set(find(p) for p in range(n)))

    def dfs(self, n, edges):
        """

        Args:
            n(int):
            edges(list[list[int]]):

        Returns:
            int:

        """

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for child in graph[node]:
                dfs(child)

        visited = set()
        graph = defaultdict(list)
        for p, q in edges:
            graph[p].append(q)
            graph[q].append(p)
        result = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                result += 1
        return result

    def bfs(self, n, edges):
        """

        Args:
            n(int):
            edges(list[list[int]]):

        Returns:
            int:

        """
        if n <= 0:
            return 0

        graph = defaultdict(list)
        for p, q in edges:
            graph[p].append(q)
            graph[q].append(p)

        visited = set()

        def bfs(node):
            queue = deque([node])
            while queue:
                node = queue.popleft()
                visited.add(node)
                queue.extend(filter(lambda x: x not in visited, graph[node]))

        result = 0
        for node in range(n):
            if node not in visited:
                bfs(node)
                result += 1

        return result

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

        Example 1:

        Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

             0          3
             |          |
             1 --- 2    4

        Output: 2
        Example 2:

        Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

             0           4
             |           |
             1 --- 2 --- 3

        Output:  1
        Note:
        You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

        Args:
            n(int):
            edges(list[list[int]]):

        Returns:
            int:

        """
        return self.union_find(n, edges)

    # [0,1,2,3,4]
    # [1,1,1,4,4]
    # [0,1,0,0,1]