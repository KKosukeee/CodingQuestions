"""
Solution for 493. Reverse Pairs
https://leetcode.com/problems/reverse-pairs/
"""
from typing import List
import bisect

class Solution:
    """
    Runtime: 2248 ms, faster than 29.86% of Python3 online submissions for Reverse Pairs.
    Memory Usage: 20.7 MB, less than 33.33% of Python3 online submissions for Reverse Pairs.
    """
    def reversePairs(self, nums: List[int]) -> int:
        """
        Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

        You need to return the number of important reverse pairs in the given array.

        Example1:

        Input: [1,3,2,3,1]
        Output: 2
        Example2:

        Input: [2,4,3,5,1]
        Output: 3
        Note:
        The length of the given array will not exceed 50,000.
        All the numbers in the input array are in the range of 32-bit integer.

        Args:
            nums(list[int]):

        Returns:
            int:

        """
        if not nums:
            return 0
        sorted_nums = []
        count = 0
        for i in range(1, len(nums)):
            index = bisect.bisect_left(sorted_nums, nums[i-1])
            sorted_nums.insert(index, nums[i-1])
            index = bisect.bisect_left(sorted_nums, nums[i]*2+1)
            count += len(sorted_nums) - index
        return count
