"""
Solution for 47. Permutations II
https://leetcode.com/problems/permutations-ii/
"""

class Solution:
    """
    Runtime: 996 ms, faster than 10.17% of Python3 online submissions for Permutations II.
    Memory Usage: 13.2 MB, less than 6.22% of Python3 online submissions for Permutations II.
    """
    def permuteUnique(self, nums):
        """
        Given a collection of numbers that might contain duplicates, return all possible unique
        permutations.

        Example:

        Input: [1,1,2]
        Output:
        [
          [1,1,2],
          [1,2,1],
          [2,1,1]
        ]
        Args:
            nums: list of integers to look for permutations from

        Returns:
            list<list<int>>: containing all permutations from nums array
        """
        return self.backtrack(nums, [], [])

    def backtrack(self, nums, combination, result):
        """
        Backtrack function
        Args:
            nums: list of integers same as the permute function
            combination: list of integers containing permutation given nums
            result: list of all integers which needs to be returned at the end

        Returns:

        """
        if not nums:
            if combination not in result:
                result.append(combination)  # backtracking
        else:
            for i in range(len(nums)):
                self.backtrack(nums[:i] + nums[i + 1:], combination + [nums[i]], result)

            return result
