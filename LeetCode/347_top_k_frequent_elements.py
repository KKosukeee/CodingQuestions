"""
Solution for 347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/
"""
import heapq
from collections import Counter

class Solution:
    """
    Runtime: 60 ms, faster than 31.63% of Python3 online submissions for Top K Frequent
        Elements.
    Memory Usage: 15.7 MB, less than 8.41% of Python3 online submissions for Top K Frequent
        Elements.
    """
    def topKFrequent(self, nums, k):
        """
        Given a non-empty array of integers, return the k most frequent elements.

        Example 1:

        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]
        Example 2:

        Input: nums = [1], k = 1
        Output: [1]
        Args:
            nums: an array containing integers to find kth most frequent elements from
            k: an integer to return kth most frequent elements from nums array

        Returns:

        """
        # Create a hash map: num -> count
        count = Counter(nums)

        # Create a heap with count, and return kth most common num
        return heapq.nlargest(k, count.keys(), key=count.get)
