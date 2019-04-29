"""
Solution for 35. Search Insert Position
https://leetcode.com/problems/search-insert-position/
"""

class Solution:
    """
    Runtime: 36 ms, faster than 93.68% of Python3 online submissions for Search Insert Position.
    Memory Usage: 13.7 MB, less than 5.11% of Python3 online submissions for Search Insert Position.
    """
    # Time: O(logn), Space: O(1)
    def searchInsert(self, nums, target):
        """
        Given a sorted array and a target value, return the index if the target is found. If not,
        return the index where it would be if it were inserted in order.

        You may assume no duplicates in the array.

        Example 1:

        Input: [1,3,5,6], 5
        Output: 2
        Example 2:

        Input: [1,3,5,6], 2
        Output: 1
        Example 3:

        Input: [1,3,5,6], 7
        Output: 4
        Example 4:

        Input: [1,3,5,6], 0
        Output: 0
        Args:
            nums: list of integers to insert target number to
            target: integer value to insert into num array

        Returns:
            int: position for inserting into nums array
        """
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # Look right
                if not mid + 1 < len(nums):
                    return len(nums)

                if target <= nums[mid + 1]:
                    return mid + 1

                low = mid + 1
            else:
                # Look left
                if not mid - 1 >= 0:
                    return 0

                if nums[mid - 1] == target:
                    return mid - 1
                elif nums[mid - 1] < target:
                    return mid

                high = mid - 1
