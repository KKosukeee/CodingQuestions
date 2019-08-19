"""
Solution for 350. Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""
from collections import Counter
class Solution:
    """
    Runtime: 56 ms, faster than 72.05% of Python3 online submissions for Intersection of Two Arrays II.
    Memory Usage: 14 MB, less than 5.72% of Python3 online submissions for Intersection of Two Arrays II.
    """
    def intersect(self, nums1, nums2):
        """
        Given two arrays, write a function to compute their intersection.

        Example 1:

        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2,2]
        Example 2:

        Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        Output: [4,9]
        Note:

        Each element in the result should appear as many times as it shows in both arrays.
        The result can be in any order.
        Follow up:

        What if the given array is already sorted? How would you optimize your algorithm?
        What if nums1's size is small compared to nums2's size? Which algorithm is better?
        What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
        Args:
            nums1(list[int]):
            nums2(list[int]):

        Returns:
            list[int]:
        """
        return (Counter(nums1) & Counter(nums2)).elements()
