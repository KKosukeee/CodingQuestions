"""
Solution for 325. Maximum Size Subarray Sum Equals k
https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
"""
from typing import List

class Solution:
  """
  Runtime: 116 ms, faster than 95.36% of Python3 online submissions for Maximum Size Subarray Sum Equals k.
  Memory Usage: 15.8 MB, less than 100.00% of Python3 online submissions for Maximum Size Subarray Sum Equals k.
  """
  def maxSubArrayLen(self, nums: List[int], k: int) -> int:
    """
    Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

    Note:
    The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

    Example 1:

    Input: nums = [1, -1, 5, -2, 3], k = 3
    Output: 4
    Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
    Example 2:

    Input: nums = [-2, -1, 2, 1], k = 1
    Output: 2
    Explanation: The subarray [-1, 2] sums to 1 and is the longest.
    Follow Up:
    Can you do it in O(n) time?

    Args:
      nums:
      k:

    Returns:

    """
    max_len, cum_sum, hash_map = 0, 0, {k: -1}
    for i in range(len(nums)):
      cum_sum += nums[i]
      hash_map.setdefault(cum_sum+k, i)
      if cum_sum in hash_map:
        max_len = max(max_len, i-hash_map[cum_sum])
    return max_len
  