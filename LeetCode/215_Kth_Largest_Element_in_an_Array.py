"""
Solution for 215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/
"""

import heapq

class Solution:
    """
    Runtime: 48 ms, faster than 48.58% of Python3 online submissions for Kth Largest Element
        in an Array.
    Memory Usage: 13.6 MB, less than 10.53% of Python3 online submissions for Kth Largest Element
        in an Array.
    """
    # O(k+(n-k)log(k)) time, min-heap
    def findKthLargest(self, nums, k):
        """
        Find the kth largest element in an unsorted array. Note that it is the kth largest element
        in the sorted order, not the kth distinct element.

        Example 1:

        Input: [3,2,1,5,6,4] and k = 2
        Output: 5
        Example 2:

        Input: [3,2,3,1,2,4,5,5,6] and k = 4
        Output: 4

        Args:
            nums: an unsorted array which you get kth largest number from
            k: an integer to take kth largest number from the array

        Returns:
            int: kth largest number from nums array
        """
        # Initialize heap array
        heap = []

        # Loop through nums to push into the heap
        for num in nums:
            heapq.heappush(heap, num)

        # Pop an element len(nums) - k times from the heap
        for _ in range(len(nums) - k):
            heapq.heappop(heap)

        # Return the popped value
        return heapq.heappop(heap)
