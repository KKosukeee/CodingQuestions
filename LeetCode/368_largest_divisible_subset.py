"""
Solution for 368. Largest Divisible Subset
"""

class Solution:
    """
    Runtime: 412 ms, faster than 33.91% of Python3 online submissions for Largest Divisible Subset.
    Memory Usage: 13.2 MB, less than 77.84% of Python3 online submissions for Largest Divisible
        Subset.
    """
    def largestDivisibleSubset(self, nums):
        """
        Given a set of distinct positive integers, find the largest subset such that every pair
        (Si, Sj) of elements in this subset satisfies:

        Si % Sj = 0 or Sj % Si = 0.

        If there are multiple solutions, return any subset is fine.

        Example 1:

        Input: [1,2,3]
        Output: [1,2] (of course, [1,3] will also be ok)
        Example 2:

        Input: [1,2,4,8]
        Output: [1,2,4,8]
        Args:
            nums: list<int> to find the largest divisible subset from

        Returns:
            list<int>: list of integers from nums array.
        """
        nums.sort()
        if len(nums) == 0: return []
        result = [nums[0]]
        dp = [[nums[i]] for i in range(len(nums))]
        for i in range(1, len(dp)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [nums[i]]
            if len(dp[i]) > len(result):
                result = dp[i]

        return result
