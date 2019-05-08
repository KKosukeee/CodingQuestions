"""
Solution for 209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/
"""

class Solution:
    """
    Runtime: 44 ms, faster than 99.06% of Python3 online submissions for Minimum Size Subarray
        Sum.
    Memory Usage: 14.5 MB, less than 12.78% of Python3 online submissions for Minimum Size Subarray
        Sum
    """
    def minSubArrayLen(self, s, nums):
        """
        Given an array of n positive integers and a positive integer s, find the minimal length of
        a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

        Example:

        Input: s = 7, nums = [2,3,1,2,4,3]
        Output: 2
        Explanation: the subarray [4,3] has the minimal length under the problem constraint.
        Args:
            s: int value to look minimum sub-array from nums that satisifies sum(sub) >= s
            nums: list<int> to look for a minimum sub-array from

        Returns:
            int: representing the the size of the array that add up to >= s
        """
        left = 0
        summed = 0
        answer = float('inf')

        for right in range(len(nums)):
            summed += nums[right]

            while left <= right and summed >= s:
                answer = min(answer, right - left + 1)
                summed -= nums[left]
                left += 1

        return answer if answer != float('inf') else 0
