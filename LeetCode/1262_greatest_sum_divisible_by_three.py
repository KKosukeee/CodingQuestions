"""
Solution for 1262. Greatest Sum Divisible by Three
https://leetcode.com/problems/greatest-sum-divisible-by-three/
"""
from typing import List

class Solution:
  """
  Runtime: 264 ms, faster than 92.05% of Python3 online submissions for Greatest Sum Divisible by Three.
  Memory Usage: 17.5 MB, less than 100.00% of Python3 online submissions for Greatest Sum Divisible by Three.
  """
  def initial_solution(self, nums: List[int]) -> int:
    """
    An initial solution that runs in TLE i.e. O(N^N) in time and O(N) in space

    Args:
      nums:

    Returns:

    """
    other = [num for num in nums if num % 3 != 0]
    total = sum(nums) - sum(other)

    def backtrack(curr, used):
      max_formed = 0
      for i in range(len(other)):
        if i in used:
          continue
        used.add(i)
        max_formed = max(max_formed, backtrack(curr + other[i], used))
        used.remove(i)
      curr = curr if curr % 3 == 0 else 0
      return max(curr, max_formed)

    max_other = 0
    for i in range(len(other)):
      max_other = max(max_other, backtrack(other[i], set([i])))
    return max_other + total

  def second_solution(self, nums: List[int]) -> int:
    """
    The second solution that runs in O(Nlog(N)) in time and O(N) in space

    Args:
      nums:

    Returns:

    """
    mod1, mod2, res = [], [], 0
    for num in nums:
      if num % 3 == 0:
        res += num
      elif num % 3 == 1:
        mod1.append(num)
      elif num % 3 == 2:
        mod2.append(num)
    mod1.sort(reverse=True)
    mod2.sort(reverse=True)
    sum1, sum2, removed = sum(mod1), sum(mod2), float('inf')
    if (sum1 + sum2) % 3 == 0:
      return res + sum1 + sum2
    elif (sum1 + sum2) % 3 == 1:
      if len(mod1) > 0:
        removed = min(removed, mod1[-1])
      if len(mod2) > 1:
        removed = min(removed, mod2[-1] + mod2[-2])
      return res + sum1 + sum2 - removed
    elif (sum1 + sum2) % 3 == 2:
      if len(mod2) > 0:
        removed = min(removed, mod2[-1])
      if len(mod1) > 1:
        removed = min(removed, mod1[-1] + mod1[-2])
      return res + sum1 + sum2 - removed

  def maxSumDivThree(self, nums: List[int]) -> int:
    """
    Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.



    Example 1:

    Input: nums = [3,6,5,1,8]
    Output: 18
    Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
    Example 2:

    Input: nums = [4]
    Output: 0
    Explanation: Since 4 is not divisible by 3, do not pick any number.
    Example 3:

    Input: nums = [1,2,3,4,4]
    Output: 12
    Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).


    Constraints:

    1 <= nums.length <= 4 * 10^4
    1 <= nums[i] <= 10^4

    Args:
      nums:

    Returns:

    """
    return self.second_solution(nums)

