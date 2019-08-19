"""
Solution for 349. Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/
"""
class Solution:
    """
    Runtime: 52 ms, faster than 84.19% of Python3 online submissions for Intersection of Two Arrays.
    Memory Usage: 14.1 MB, less than 5.88% of Python3 online submissions for Intersection of Two Arrays.
    """
    def intersection(self, nums1, nums2):
        """
        Given two arrays, write a function to compute their intersection.

        Example 1:

        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2]
        Example 2:

        Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        Output: [9,4]
        Note:

        Each element in the result must be unique.
        The result can be in any order.
        Args:
            nums1(list[int]):
            nums2(list[int]):

        Returns:
            list[int]:
        """
        return set(nums1).intersection(set(nums2))