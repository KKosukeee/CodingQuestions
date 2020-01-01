"""
Solution for 1296. Divide Array in Sets of K Consecutive Numbers
https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
"""
from collections import Counter
from typing import List

class Solution:
  """
  Runtime: 460 ms, faster than 64.18% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.
  Memory Usage: 27.3 MB, less than 100.00% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.
  """
  def isPossibleDivide(self, nums: List[int], k: int) -> bool:
    """
    Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
    Return True if its possible otherwise return False.



    Example 1:

    Input: nums = [1,2,3,3,4,4,5,6], k = 4
    Output: true
    Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
    Example 2:

    Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
    Output: true
    Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
    Example 3:

    Input: nums = [3,3,2,2,1,1], k = 3
    Output: true
    Example 4:

    Input: nums = [1,2,3,4], k = 3
    Output: false
    Explanation: Each array should be divided in subarrays of size 3.


    Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    1 <= k <= nums.length

    Args:
      nums:
      k:

    Returns:

    """
    return self.counter_solution(nums, k)

  def counter_solution(self, nums: List[int], k: int) -> bool:
    """
    A solution using a counter. This runs in O(Nlog(N)) in time and O(N) in space

    Args:
      nums:
      k:

    Returns:

    """
    counter = Counter(nums)
    for key in sorted(counter.keys()):
      while counter[key]:
        for i in range(key, key + k):
          if counter[i] == 0:
            return False
          counter[i] -= 1
    return True
