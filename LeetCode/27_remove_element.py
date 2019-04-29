"""
Solution for 27. Remove Element
https://leetcode.com/problems/remove-element/
"""

class Solution:
    """
    Runtime: 36 ms, faster than 99.37% of Python3 online submissions for Remove Element.
    Memory Usage: 12.9 MB, less than 5.09% of Python3 online submissions for Remove Element.
    """
    def optimal_approach(self, nums, val):
        """
        Optimal approach for the question
        Args:
            nums: list of integers to remove a val from
            val: integer value to remove from nums array

        Returns:
            int: length of newly created array where val is removed from nums
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1

        return len(nums)

    def clean_approach(self, nums, val):
        """
        Clean approach for the question
        Args:
            nums: list of integers to remove a val from
            val: integer value to remove from nums array

        Returns:
            int: length of newly created array where val is removed from nums
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i

    def removeElement(self, nums, val):
        """
        Given an array nums and a value val, remove all instances of that value in-place and return
        the new length.

        Do not allocate extra space for another array, you must do this by modifying the input
        array in-place with O(1) extra memory.

        The order of elements can be changed. It doesn't matter what you leave beyond the new
        length.

        Example 1:

        Given nums = [3,2,2,3], val = 3,

        Your function should return length = 2, with the first two elements of nums being 2.

        It doesn't matter what you leave beyond the returned length.
        Example 2:

        Given nums = [0,1,2,2,3,0,4,2], val = 2,

        Your function should return length = 5, with the first five elements of nums containing
        0, 1, 3, 0, and 4.

        Note that the order of those five elements can be arbitrary.

        It doesn't matter what values are set beyond the returned length.
        Args:
            nums: list of integers to remove a val from
            val: integer value to remove from nums array

        Returns:
            int: length of newly created array where val is removed from nums
        """
        return self.clean_approach(nums, val)
