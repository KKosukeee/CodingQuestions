"""
Solution for 523. Continuous Subarray Sum
https://leetcode.com/problems/continuous-subarray-sum/
"""
from typing import List

class Solution:
  """
  Runtime: 220 ms, faster than 97.31% of Python3 online submissions for Continuous Subarray Sum.
  Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Continuous Subarray Sum.
  """
  def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    """
    Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.



    Example 1:

    Input: [23, 2, 4, 6, 7],  k=6
    Output: True
    Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
    Example 2:

    Input: [23, 2, 6, 4, 7],  k=6
    Output: True
    Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.


    Note:

    The length of the array won't exceed 10,000.
    You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

    Args:
      nums:
      k:

    Returns:

    """
    if k == 0:
      return any(nums[i] == nums[i + 1] == 0 for i in range(len(nums) - 1))
    cum_sum, mod_map = 0, {0: -1}
    for i, num in enumerate(nums):
      cum_sum = (cum_sum + num) % k
      if cum_sum in mod_map and i - mod_map[cum_sum] >= 2:
        print(mod_map)
        return True
      mod_map.setdefault(cum_sum, i)
    return False
