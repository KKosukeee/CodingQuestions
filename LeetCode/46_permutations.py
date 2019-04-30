"""
Solution for 46. Permutations
https://leetcode.com/problems/permutations/
"""
class Solution:
    """
    Runtime: 52 ms, faster than 72.70% of Python3 online submissions for Permutations.
    Memory Usage: 13.3 MB, less than 5.23% of Python3 online submissions for Permutations.
    """
    def permute(self, nums):
        """
        Given a collection of distinct integers, return all possible permutations.

        Example:

        Input: [1,2,3]
        Output:
        [
          [1,2,3],
          [1,3,2],
          [2,1,3],
          [2,3,1],
          [3,1,2],
          [3,2,1]
        ]
        Args:
            nums: list of integers to look all permutations from

        Returns:
            list<list<int>>: 2D arrays containing all permutations from nums
        """
        return self.backtrack(nums, [], [])

    def backtrack(self, nums, combination, result):
        """
        Backtrack function to get all permutations with
        Args:
            nums: same input as permute function
            combination: list of integers to store permutation
            result: list of list of integers to store all permutations

        Returns:

        """
        if not nums:
            result.append(combination) # backtracking
        else:
            for i in range(len(nums)):
                self.backtrack(nums[:i] + nums[i+1:], combination+[nums[i]], result)

            return result
