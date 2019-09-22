"""
Solution for 1202. Smallest String With Swaps
https://leetcode.com/problems/smallest-string-with-swaps/
"""
from collections import defaultdict
from collections import deque
from typing import List

class Solution:
    """
    Runtime: 736 ms, faster than 100.00% of Python3 online submissions for Smallest String With Swaps.
    Memory Usage: 50.2 MB, less than 100.00% of Python3 online submissions for Smallest String With Swaps.
    """
    def dfs(self, s: str, pairs: List[List[int]]) -> str:
        """
        DFS solution that runs in O(E + Vlog(V)) where E = len(pairs), V = len(s)

        Args:
            s(str):
            pairs(list[list[int]]):

        Returns:
            str:

        """
        graph = defaultdict(list)
        for p, q in pairs:
            graph[q].append(p)
            graph[p].append(q)

        visited = set()
        group = defaultdict(list)

        for i in range(len(s)):
            if i not in visited:
                stack = [i]
                indices = []
                while stack:
                    vertex = stack.pop()
                    if vertex not in visited:
                        visited.add(vertex)
                        stack.extend(graph[vertex])
                        indices.append(vertex)
                group[i] = indices

        return_s = list(s)
        for indices in group.values():
            part_s = ''
            for i in indices:
                part_s += s[i]
            part_s = sorted(part_s)
            for i, j in enumerate(sorted(indices)):
                return_s[j] = part_s[i]
        return ''.join(return_s)

    def bfs(self, s: str, pairs: List[List[int]]) -> str:
        """
        BFS solution that runs in O(E + Vlog(V))

        Args:
            s(str):
            pairs(list[list[int]]):

        Returns:
            str:

        """
        graph = defaultdict(list)
        for p, q in pairs:
            graph[p].append(q)
            graph[q].append(p)
        visited = set()
        groups = []
        for i in range(len(s)):
            if i not in visited:
                groups.append([])
                queue = deque([i])
                while queue:
                    node = queue.popleft()
                    if node not in visited:
                        visited.add(node)
                        queue.extend(graph[node])
                        groups[-1].append(node)
        result_s = list(s)
        for group in groups:
            group.sort()
            ss = sorted([s[i] for i in group])
            for i, char in zip(group, ss):
                result_s[i] = char
        return ''.join(result_s)

    def union_find(self, s: str, pairs: List[List[int]]) -> str:
        """
        Union-find solution that runs in O(E+Vlog(V))

        Args:
            s(str):
            pairs(list[list[int]]):

        Returns:
            str:

        """
        parents = [i for i in range(len(s))]
        ranks = [0 for _ in range(len(s))]

        def find(p):
            """
            Find parent of p

            Args:
                p(int):

            Returns:
                int:

            """
            if p != parents[p]:
                parents[p] = find(parents[p])
            return parents[p]

        def union(p, q):
            """
            Union p and q

            Args:
                p(int):
                q(int):

            Returns:
                None:

            """
            p1, p2 = find(p), find(q)
            if ranks[p1] == ranks[p2]:
                parents[p1] = p2
                ranks[p2] += 1
            elif ranks[p1] > ranks[p2]:
                parents[p2] = p1
            else:
                parents[p1] = p2

        for p, q in pairs:
            union(p, q)
        parents = [find(parent) for parent in parents]
        groups = defaultdict(list)
        for i, parent in enumerate(parents):
            groups[parent].append(i)
        result_s = list(s)
        for group in groups.values():
            group.sort()
            ss = sorted([result_s[i] for i in group])
            for i, char in zip(group, ss):
                result_s[i] = char
        return ''.join(result_s)

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        """
        You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

        You can swap the characters at any pair of indices in the given pairs any number of times.

        Return the lexicographically smallest string that s can be changed to after using the swaps.



        Example 1:

        Input: s = "dcab", pairs = [[0,3],[1,2]]
        Output: "bacd"
        Explaination:
        Swap s[0] and s[3], s = "bcad"
        Swap s[1] and s[2], s = "bacd"
        Example 2:

        Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
        Output: "abcd"
        Explaination:
        Swap s[0] and s[3], s = "bcad"
        Swap s[0] and s[2], s = "acbd"
        Swap s[1] and s[2], s = "abcd"
        Example 3:

        Input: s = "cba", pairs = [[0,1],[1,2]]
        Output: "abc"
        Explaination:
        Swap s[0] and s[1], s = "bca"
        Swap s[1] and s[2], s = "bac"
        Swap s[0] and s[1], s = "abc"



        Constraints:

        1 <= s.length <= 10^5
        0 <= pairs.length <= 10^5
        0 <= pairs[i][0], pairs[i][1] < s.length
        s only contains lower case English letters.

        Args:
            s(str):
            pairs(list[list[int]]):

        Returns:
            str:

        """
        return self.union_find(s, pairs)
    