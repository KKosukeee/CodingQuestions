"""
Solution for 34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

class Solution:
    """
    Runtime: 40 ms, faster than 85.90% of Python3 online submissions for Find First and Last
    Position of Element in Sorted Array.
    Memory Usage: 13.9 MB, less than 5.06% of Python3 online submissions for Find First and Last
    Position of Element in Sorted Array.
    """
    # Time: O(logn), Space: O(1)
    def searchRange(self, nums, target):
        """
        Given an array of integers nums sorted in ascending order, find the starting and ending
        position of a given target value.

        Your algorithm's runtime complexity must be in the order of O(log n).

        If the target is not found in the array, return [-1, -1].

        Example 1:

        Input: nums = [5,7,7,8,8,10], target = 8
        Output: [3,4]
        Example 2:

        Input: nums = [5,7,7,8,8,10], target = 6
        Output: [-1,-1]
        Args:
            nums: list of integers to search first and last position of elements from
            target: integer value to look find first and last position with

        Returns:
            list<int>: list of integers containing start and end of the target value in the nums
        """
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                # expand the window
                i, j = mid, mid

                while i - 1 >= 0 and nums[i - 1] == target:
                    i -= 1

                while j + 1 < len(nums) and nums[j + 1] == target:
                    j += 1

                return [i, j]
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return [-1, -1]
