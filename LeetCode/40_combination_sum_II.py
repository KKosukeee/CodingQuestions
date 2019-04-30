"""
Solution for 40. Combination Sum II
https://leetcode.com/problems/combination-sum-ii/
"""

class Solution:
    """
    Runtime: 548 ms, faster than 10.33% of Python3 online submissions for Combination Sum II.
    Memory Usage: 13 MB, less than 5.20% of Python3 online submissions for Combination Sum II.
    """
    def combinationSum2(self, candidates, target):
        """
        Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
        Args:
            candidates:
            target:

        Returns:

        """
        candidates.sort()
        return self.dfs(candidates, target, 0, [], [])

    def dfs(self, candidates, target, index, path, result):
        if target == 0:
            if path not in result:
                result.append(path)
        elif target < 0:
            return  # backtracking
        else:
            for i in range(index, len(candidates)):
                self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], result)

            return result
