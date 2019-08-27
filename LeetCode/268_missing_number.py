"""
Solution for 268. Missing Number
https://leetcode.com/problems/missing-number/
"""
class Solution:
    """
    Runtime: 140 ms, faster than 99.55% of Python3 online submissions for Missing Number.
    Memory Usage: 15.1 MB, less than 6.45% of Python3 online submissions for Missing Number.
    """
    def missingNumber(self, nums):
        """
        Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

        Example 1:

        Input: [3,0,1]
        Output: 2
        Example 2:

        Input: [9,6,4,2,3,5,7,0,1]
        Output: 8
        Note:
        Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
        Args:
            nums(list[int]):

        Returns:
            int:

        """
        return int(len(nums) * (len(nums) + 1) / 2 - sum(nums))
