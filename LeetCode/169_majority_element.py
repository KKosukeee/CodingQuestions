"""
Solution for 169. Majority Element
https://leetcode.com/problems/majority-element/
"""
class Solution:
    """
    Runtime: 196 ms, faster than 66.55% of Python3 online submissions for Majority Element.
    Memory Usage: 14.8 MB, less than 7.14% of Python3 online submissions for Majority Element.
    """
    def majorityElement(self, nums):
        """
        Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

        You may assume that the array is non-empty and the majority element always exist in the array.

        Example 1:

        Input: [3,2,3]
        Output: 3
        Example 2:

        Input: [2,2,1,1,1,2,2]
        Output: 2Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

        You may assume that the array is non-empty and the majority element always exist in the array.

        Example 1:

        Input: [3,2,3]
        Output: 3
        Example 2:

        Input: [2,2,1,1,1,2,2]
        Output: 2

        Args:
            nums(list[int]):

        Returns:
            int:

        """
        count, candidate = 0, None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate
