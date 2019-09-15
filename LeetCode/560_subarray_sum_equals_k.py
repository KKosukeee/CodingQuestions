"""
Solution for 560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/submissions/
"""
from collections import defaultdict
from typing import List

class Solution:
    """
    Runtime: 136 ms, faster than 40.48% of Python3 online submissions for Subarray Sum Equals K.
    Memory Usage: 17.7 MB, less than 12.00% of Python3 online submissions for Subarray Sum Equals K.
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

        Example 1:
        Input:nums = [1,1,1], k = 2
        Output: 2
        Note:
        The length of the array is in range [1, 20,000].
        The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

        Args:
            nums(list[int]):
            k(int):

        Returns:
            int:

        """
        hash_map = defaultdict(int)
        hash_map[k] = 1
        count, cum_sum = 0, 0
        for num in nums:
            cum_sum += num
            count += hash_map[cum_sum]
            hash_map[cum_sum + k] += 1
        return count
    #      *
    # [1,1,1], k=2, c=1
    # {2:1,3:1,4:1}

    # [1,2,3]
    # [1,3,6]
    