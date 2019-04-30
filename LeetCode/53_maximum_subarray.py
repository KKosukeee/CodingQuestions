"""
Solution for 53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/
"""

class Solution:
    """
    Runtime: 44 ms, faster than 93.31% of Python3 online submissions for Maximum Subarray.
    Memory Usage: 13.7 MB, less than 5.50% of Python3 online submissions for Maximum Subarray.
    """
    def maxSubArray(self, nums):
        """
        Given an integer array nums, find the contiguous subarray (containing at least one number)
        which has the largest sum and return its sum.

        Example:

        Input: [-2,1,-3,4,-1,2,1,-5,4],
        Output: 6
        Explanation: [4,-1,2,1] has the largest sum = 6.
        Args:
            nums: list of integers to look for maximum subarray

        Returns:
            list<int>: list of integers which's sum is the maximum within the nums
        """
        local_max = nums[0]
        global_max = nums[0]

        for num in nums[1:]:
            local_max = max(num, num + local_max)
            global_max = max(global_max, local_max)

        return global_max
