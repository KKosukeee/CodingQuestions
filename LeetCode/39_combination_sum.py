"""
Solution for 39. Combination Sum
https://leetcode.com/problems/combination-sum/
"""

class Solution:
    """
    Runtime: 96 ms, faster than 52.91% of Python3 online submissions for Combination Sum.
    Memory Usage: 13.1 MB, less than 5.14% of Python3 online submissions for Combination Sum.
    """
    def combinationSum(self, candidates, target):
        """
        Given a set of candidate numbers (candidates) (without duplicates) and a target number
        (target), find all unique combinations in candidates where the candidate numbers sums
        to target.

        The same repeated number may be chosen from candidates unlimited number of times.

        Note:

        All numbers (including target) will be positive integers.
        The solution set must not contain duplicate combinations.
        Example 1:

        Input: candidates = [2,3,6,7], target = 7,
        A solution set is:
        [
          [7],
          [2,2,3]
        ]
        Example 2:

        Input: candidates = [2,3,5], target = 8,
        A solution set is:
        [
          [2,2,2,2],
          [2,3,3],
          [3,5]
        ]
        Args:
            candidates: list of integers to look for any combinations which add up to the target
            target: integer value which you look for combinations from candidates array

        Returns:
            list<list<int>>: 2D arrays where for each array in the second dimension sums up to
                the target
        """
        res = []
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        """
        Backtracking function
        Args:
            nums: list of integers from candidates array
            target: integers which you look for the sum
            index: integer value indicating where you should search from
            path: list of integers containing numbers which has been used
            res: list of list of integers where each array in the second dimension add up to the
                target value

        Returns:

        """
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)
