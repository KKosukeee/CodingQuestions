"""
Solution for 547. Friend Circles
https://leetcode.com/problems/friend-circles/
"""
from collections import deque
from typing import List

class Solution:
    """
    Runtime: 224 ms, faster than 61.39% of Python3 online submissions for Friend Circles.
    Memory Usage: 14.1 MB, less than 5.88% of Python3 online submissions for Friend Circles.
    """
    def union_find(self, M: List[List[int]]) -> int:
        """
        Union-find algorithm that runs in O(N^2)

        Args:
            M(list[list[int]]):

        Returns:
            int:

        """
        parents = [i for i in range(len(M))]
        rank = [0 for _ in range(len(M))]

        def find(p):
            """
            Find operation

            Args:
                p(int):

            Returns:
                int:

            """
            if parents[p] != p:
                parents[p] = find(parents[p])
            return parents[p]

        def union(p, q):
            """
            Union operation

            Args:
                p(int):
                q(int):

            Returns:
                None:

            """
            p1, p2 = find(p), find(q)
            if p1 == p2:
                return
            if rank[p1] > rank[p2]:
                parents[p2] = p1
            elif rank[p1] < rank[p2]:
                parents[p1] = p2
            else:
                parents[p1] = p2
                rank[p2] += 1

        for i in range(len(M)):
            for j in range(i + 1, len(M[0])):
                if M[i][j] == 1:
                    union(i, j)

        return len(set(find(p) for p in range(len(M))))

    def dfs(self, M):
        """
        DFS that runs in O(N^2)

        Args:
            M(list[list[int]]):

        Returns:
            int:

        """
        visited = set()
        count = 0

        for i in range(len(M)):
            if i not in visited:
                stack = [i]
                while stack:
                    node = stack.pop()
                    for j in range(len(M)):
                        if M[node][j] == 1 and j not in visited and node != j:
                            stack.append(j)
                    visited.add(node)
                count += 1
        return count

    def bfs(self, M):
        """
        BFS that runs in O(N^2)

        Args:
            M(list[list[int]]):

        Returns:
            int:

        """
        visited = set()
        count = 0
        for i in range(len(M)):
            if i not in visited:
                queue = deque([i])
                while queue:
                    node = queue.popleft()
                    for j in range(len(M)):
                        if node != j and j not in visited and M[node][j] == 1:
                            queue.append(j)
                    visited.add(node)
                count += 1
        return count

    def findCircleNum(self, M: List[List[int]]) -> int:
        """
        There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

        Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

        Example 1:
        Input:
        [[1,1,0],
         [1,1,0],
         [0,0,1]]
        Output: 2
        Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
        The 2nd student himself is in a friend circle. So return 2.
        Example 2:
        Input:
        [[1,1,0],
         [1,1,1],
         [0,1,1]]
        Output: 1
        Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
        so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
        Note:
        N is in range [1,200].
        M[i][i] = 1 for all students.
        If M[i][j] = 1, then M[j][i] = 1.

        Args:
            M(list[list[int]]):

        Returns:
            int:

        """
        return self.union_find(M)

    # 110
    # 110
    # 001
    #
    # [1,1,2]
    # [0,1,0]
    # -> union(0, 1)

    # 110
    # 111
    # 011
    #

