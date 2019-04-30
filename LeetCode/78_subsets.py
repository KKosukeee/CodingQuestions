"""
Solution for 78. Subsets
https://leetcode.com/problems/subsets/
"""

class Solution:
    """
    Runtime: 40 ms, faster than 86.21% of Python3 online submissions for Subsets.
    Memory Usage: 13.5 MB, less than 5.00% of Python3 online submissions for Subsets.
    """
    # DFS recursively
    def recursive_approach(self, nums):
        """
        Recursive approach for this question
        Args:
            nums: list of integers to look for all subsets

        Returns:
            list: 2D dense array containing integers
        """
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        """
        Recursive helper function
        Args:
            nums: list of integers to look for all subsets
            index: integer indicating where to search the subset from
            path: integer indicating currently seen nums
            res: output array containing integers

        Returns:

        """
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)

    def iterative_approach(self, nums):
        """
        Iterative approach for the question
        Args:
            nums: list of integers to look for all subsets

        Returns:
            list: 2D dense array containing integers
        """
        result = [[]]
        N = len(nums)

        def backtrack(combo, start):
            for i in range(start, N):
                new_combo = combo + [nums[i]]
                result.append(new_combo)
                backtrack(new_combo, i + 1)

        backtrack([], 0)
        return result

    def subsets(self, nums):
        """
        Given a set of distinct integers, nums, return all possible subsets (the power set).

        Note: The solution set must not contain duplicate subsets.

        Example:

        Input: nums = [1,2,3]
        Output:
        [
          [3],
          [1],
          [2],
          [1,2,3],
          [1,3],
          [2,3],
          [1,2],
          []
        ]
        Args:
            nums: list of integers to look for all subsets

        Returns:
            list: 2D dense array containing integers
        """
        return self.recursive_approach(nums)
