"""
Solution for 1295. Find Numbers with Even Number of Digits
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
"""
from typing import List

class Solution:
  """
  Runtime: 52 ms, faster than 72.87% of Python3 online submissions for Find Numbers with Even Number of Digits.
  Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find Numbers with Even Number of Digits.
  """
  def findNumbers(self, nums: List[int]) -> int:
    """
    Given an array nums of integers, return how many of them contain an even number of digits.


    Example 1:

    Input: nums = [12,345,2,6,7896]
    Output: 2
    Explanation:
    12 contains 2 digits (even number of digits).
    345 contains 3 digits (odd number of digits).
    2 contains 1 digit (odd number of digits).
    6 contains 1 digit (odd number of digits).
    7896 contains 4 digits (even number of digits).
    Therefore only 12 and 7896 contain an even number of digits.
    Example 2:

    Input: nums = [555,901,482,1771]
    Output: 1
    Explanation:
    Only 1771 contains an even number of digits.


    Constraints:

    1 <= nums.length <= 500
    1 <= nums[i] <= 10^5

    Args:
      nums:

    Returns:

    """
    return self.sum_one_linear(nums)

  def initial_solution(self, nums: List[int]) -> int:
    """
    An initial solution that runs in O(NM) in time where N = len(nums) and M =
    max(len(str(nums[i]))) and O(1) in space

    Args:
      nums:

    Returns:

    """
    ans = 0
    for num in nums:
      ans += len(str(num)) % 2 == 0
    return ans

  def one_linear(self, nums: List[int]) -> int:
    """
    A one-linear solution same as the initial solution

    Args:
      nums:

    Returns:

    """
    return len(list(filter(lambda x: len(str(x)) % 2 == 0, nums)))

  def sum_one_linear(self, nums: List[int]) -> int:
    """
    Yet another one-linear solution

    Args:
      nums:

    Returns:

    """
    return sum(len(str(num)) % 2 == 0 for num in nums)

  def other_solution(self, nums: List[int]) -> int:
    """
    A solution that doesn't convert the nums to str

    Args:
      nums:

    Returns:

    """
    ans = 0
    for num in nums:
      digit = 0
      while num > 0:
        num //= 10
        digit += 1
      ans += digit % 2 == 0
    return ans