"""
Solution for 136. Single Number
https://leetcode.com/problems/single-number/
"""
from functools import reduce
class Solution:
    """
    Runtime: 104 ms, faster than 41.17% of Python3 online submissions for Single Number.
    Memory Usage: 16.2 MB, less than 6.56% of Python3 online submissions for Single Number.
    """
    def singleNumber(self, nums):
        """
        Given a non-empty array of integers, every element appears twice except for one. Find that single one.

        Note:

        Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

        Example 1:

        Input: [2,2,1]
        Output: 1
        Example 2:

        Input: [4,1,2,1,2]
        Output: 4
        Args:
            nums(list[int]):

        Returns:
            int:
        """
        return reduce(lambda a, b: a ^ b, nums)
