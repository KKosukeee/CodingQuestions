"""
Solution for 128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/
"""
from collections import Counter

class Solution(object):
    """
    Runtime: 44 ms, faster than 51.28% of Python online submissions for Longest Consecutive Sequence.
    Memory Usage: 13.5 MB, less than 5.00% of Python online submissions for Longest Consecutive Sequence.
    """
    def recursive_dfs(self, nums):
        """
        A simple dfs solution that runs in O(N) in time and space

        Args:
            nums(list[int]):

        Returns:
            int

        """
        hash_table = set(nums)

        def dfs(num):
            if num not in hash_table:
                return 0
            return dfs(num + 1) + 1

        max_len = 0
        for num in nums:
            if num - 1 not in hash_table:
                max_len = max(max_len, dfs(num))
        return max_len

    def iterative_dfs(self, nums):
        """
        A simple dfs in iterative manner

        Args:
            nums(list[int]):

        Returns:
            int:

        """
        max_len = 0
        hash_table = set(nums)
        for num in nums:
            if num - 1 not in hash_table:
                stack, count = [num], 0
                while stack:
                    node = stack.pop()
                    if node + 1 in hash_table:
                        stack.append(node + 1)
                    count += 1
                max_len = max(max_len, count)
        return max_len

    def union_find(self, nums):
        """
        A simple union-find solution that runs in O(N) in space and time

        Args:
            nums(list[int]):

        Returns:
            int:

        """
        if not nums:
            return 0
        nums = set(nums)
        parents = [i for i in range(len(nums))]
        ranks = [0 for _ in range(len(nums))]

        def find(p):
            if p != parents[p]:
                parents[p] = find(parents[p])
            return parents[p]

        def union(p, q):
            p1, p2 = find(p), find(q)
            if ranks[p1] > ranks[p2]:
                parents[p2] = p1
            elif ranks[p1] < ranks[p2]:
                parents[p1] = p2
            else:
                parents[p1] = p2
                ranks[p2] += 1

        hash_table = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            if num - 1 in hash_table:
                union(i, hash_table[num - 1])
            if num + 1 in hash_table:
                union(i, hash_table[num + 1])
        counter = Counter([find(parent) for parent in parents])
        return max(value for value in counter.values())

    def longestConsecutive(self, nums):
        """
        Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

        Your algorithm should run in O(n) complexity.

        Example:

        Input: [100, 4, 200, 1, 3, 2]
        Output: 4
        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

        :type nums: List[int]
        :rtype: int
        """
        return self.recursive_dfs(nums)
