"""
Solution for 238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
"""
class Solution:
    """
    Runtime: 124 ms, faster than 99.56% of Python3 online submissions for Product of Array Except Self.
    Memory Usage: 20.4 MB, less than 82.00% of Python3 online submissions for Product of Array Except Self.
    """
    def productExceptSelf(self, nums):
        """
        Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

        Example:

        Input:  [1,2,3,4]
        Output: [24,12,8,6]
        Note: Please solve it without division and in O(n).

        Follow up:
        Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
        Args:
            nums(list[int]):

        Returns:
            list[int]:
        """
        cl, cr = 1, 1
        result = [1] * len(nums)
        for i in range(len(nums)):
            j = len(nums)-i-1
            result[i] *= cl
            result[j] *= cr
            cl, cr = cl*nums[i], cr*nums[j]
        return result
