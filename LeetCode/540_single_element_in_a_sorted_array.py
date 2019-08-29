"""
Solution for 540. Single Element in a Sorted Array
https://leetcode.com/problems/single-element-in-a-sorted-array/https://leetcode.com/problems/single-element-in-a-sorted-array/
"""
class Solution:
    """
    Runtime: 84 ms, faster than 71.80% of Python3 online submissions for Single Element in a Sorted Array.
    Memory Usage: 15.8 MB, less than 7.69% of Python3 online submissions for Single Element in a Sorted Array.
    """
    def singleNonDuplicate(self, nums):
        """
        Given a sorted array consisting of only integers where every element appears exactly twice except for one element which appears exactly once. Find this single element that appears only once.



        Example 1:

        Input: [1,1,2,3,3,4,4,8,8]
        Output: 2
        Example 2:

        Input: [3,3,7,7,10,11,11]
        Output: 10


        Note: Your solution should run in O(log n) time and O(1) space.

        Args:
            nums(list[int]):

        Returns:
            int:

        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            is_even = (mid - low + 1) % 2 == 0
            if low == high:
                return nums[mid]
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            elif (nums[mid] == nums[mid - 1] and not is_even) or (
                    nums[mid] == nums[mid + 1] and is_even):
                high = mid - 2 if not is_even else mid - 1
            else:
                low = mid + 2 if not is_even else mid + 1
        return nums[mid]

# [1,2,2,3,3]       -> len(left) == odd     -> move left
# [1,2,2,3,3,4,4]   -> len(left) == even    -> move left

# [1,1,2,2,3]       -> len(left) == odd     -> move right
# [1,1,2,2,3,3,4]   -> len(left) == even    -> move right


# Time -> O(N) where N is len(nums)
# Space -> O(1)

# Time -> O(2N) -> O(N)
# Space -> {1: 2, 2: 2, 3: 1} O(N)
