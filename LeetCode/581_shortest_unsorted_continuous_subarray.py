"""
Solution for 581. Shortest Unsorted Continuous Subarray
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
"""

class Solution:
    """
    Runtime: 236 ms, faster than 83.62% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
    Memory Usage: 15.1 MB, less than 5.48% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
    """
    def findUnsortedSubarray(self, nums):
        """
        Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

        You need to find the shortest such subarray and output its length.

        Example 1:
        Input: [2, 6, 4, 8, 10, 9, 15]
        Output: 5
        Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
        Note:
        Then length of the input array is in range [1, 10,000].
        The input array may contain duplicates, so ascending order here means <=.
        Args:
            nums: list<int>

        Returns:
            int:
        """
        sorted_array = sorted(nums)
        i, j = 0, len(nums) - 1
        is_sorted = True

        while i < len(nums) and j >= 0 and i <= j and (
                nums[i] == sorted_array[i] or nums[j] == sorted_array[j]):
            if nums[i] != sorted_array[i]:
                is_sorted = False
            else:
                i += 1

            if nums[j] != sorted_array[j]:
                is_sorted = False
            else:
                j -= 1

        if not i <= j:
            return len(nums) if not is_sorted else 0

        return j - i + 1

    """
    Runtime: 276 ms, faster than 26.72% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
    Memory Usage: 15.2 MB, less than 5.48% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
    """
    def findUnsortedSubarray(self, nums):
        """
        Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

        You need to find the shortest such subarray and output its length.

        Example 1:
        Input: [2, 6, 4, 8, 10, 9, 15]
        Output: 5
        Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
        Note:
        Then length of the input array is in range [1, 10,000].
        The input array may contain duplicates, so ascending order here means <=.
        Args:
            nums: list<int>

        Returns:
            int:
        """
        unsorted_array_started = False
        min_value, max_value = float('inf'), float('-inf')
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                unsorted_array_started = True

            if unsorted_array_started:
                min_value = min(min_value, nums[i])

        unsorted_array_started = False
        for i in range(len(nums) - 2, -1, -1):
            if nums[i + 1] < nums[i]:
                unsorted_array_started = True

            if unsorted_array_started:
                max_value = max(max_value, nums[i])

        i, j = 0, len(nums) - 1
        while i < len(nums) and nums[i] <= min_value:
            i += 1

        while j >= 0 and nums[j] >= max_value:
            j -= 1

        if not i <= j:
            return 0

        return j - i + 1
