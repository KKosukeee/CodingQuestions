"""
Solution for 645. Set Mismatch
https://leetcode.com/problems/set-mismatch/
"""
class Solution:
    """
    Runtime: 216 ms, faster than 90.27% of Python3 online submissions for Set Mismatch.
    Memory Usage: 15.7 MB, less than 11.11% of Python3 online submissions for Set Mismatch.
    """
    def findErrorNums(self, nums):
        """
        The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

        Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

        Example 1:
        Input: nums = [1,2,2,4]
        Output: [2,3]
        Note:
        The given array size will in the range [2, 10000].
        The given array's numbers won't have any order.
        Args:
            nums(list[int]):

        Returns:

        """
        return [sum(nums)-sum(set(nums)), int(len(nums)*(len(nums)+1)/2-sum(set(nums)))]
