"""
Solution for 53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/
"""
from typing import List

class Solution:
    """
    Runtime: 44 ms, faster than 93.31% of Python3 online submissions for Maximum Subarray.
    Memory Usage: 13.7 MB, less than 5.50% of Python3 online submissions for Maximum Subarray.
    """

    def top_down(self, nums: List[int]) -> int:
        """
        Top-down DP solution which runs in O(N)

        Args:
            nums(list[int]):

        Returns:
            int:

        """
        self.max_sum = float('-inf')
        def recursion(i):
            if not i < len(nums):
                return 0
            local_max = max(recursion(i + 1) + nums[i], nums[i])
            self.max_sum = max(self.max_sum, local_max)
            return local_max

        recursion(0)
        return self.max_sum

    def bottom_up(self, nums: List[int]) -> int:
        """
        Bottom-up DP solution which runs in O(N)

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

    def maxSubArray(self, nums: List[int]) -> int:
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
        return self.bottom_up(nums)
