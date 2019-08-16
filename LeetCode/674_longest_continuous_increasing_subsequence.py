"""
Solution for 674. Longest Continuous Increasing Subsequence
https://leetcode.com/problems/longest-continuous-increasing-subsequence/
"""
class Solution:
    """
    Runtime: 76 ms, faster than 99.56% of Python3 online submissions for Longest Continuous Increasing Subsequence.
    Memory Usage: 15 MB, less than 8.70% of Python3 online submissions for Longest Continuous Increasing Subsequence.
    """
    def findLengthOfLCIS(self, nums):
        """
        Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

        Example 1:
        Input: [1,3,5,4,7]
        Output: 3
        Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
        Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
        Example 2:
        Input: [2,2,2,2,2]
        Output: 1
        Explanation: The longest continuous increasing subsequence is [2], its length is 1.
        Note: Length of the array will not exceed 10,000.
        Args:
            nums(list[int]):

        Returns:
            int:
        """
        if not nums:
            return 0
        local_max = 0
        global_max = 0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                local_max += 1
            else:
                local_max = 0
            global_max = max(global_max, local_max)
        return global_max + 1
    