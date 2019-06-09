"""
Solution for 283. Move Zeroes
https://leetcode.com/problems/move-zeroes/
"""

class Solution:
    """
    Runtime: 52 ms, faster than 52.07% of Python3 online submissions for Move Zeroes.
    Memory Usage: 14.6 MB, less than 12.19% of Python3 online submissions for Move Zeroes.
    """
    def moveZeroes(self, nums):
        """
        Given an array nums, write a function to move all 0's to the end of it while maintaining
        the relative order of the non-zero elements.

        Example:

        Input: [0,1,0,3,12]
        Output: [1,3,12,0,0]
        Args:
            nums: list of integers to move zeros from

        Returns:

        """
        zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero] = nums[i]
                zero += 1

        for i in range(zero, len(nums)):
            nums[i] = 0
