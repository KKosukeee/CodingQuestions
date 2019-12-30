"""
Solution for 29. Divide Two Integers
https://leetcode.com/problems/divide-two-integers/
"""

class Solution:
  """
  Runtime: 24 ms, faster than 97.42% of Python3 online submissions for Divide Two Integers.
  Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Divide Two Integers.
  """
  def divide(self, dividend: int, divisor: int) -> int:
    """
    Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

    Return the quotient after dividing dividend by divisor.

    The integer division should truncate toward zero.

    Example 1:

    Input: dividend = 10, divisor = 3
    Output: 3
    Example 2:

    Input: dividend = 7, divisor = -3
    Output: -2
    Note:

    Both dividend and divisor will be 32-bit signed integers.
    The divisor will never be 0.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

    Args:
      dividend:
      divisor:

    Returns:

    """
    return self.bit_manipulation(dividend, divisor)

  def brute_force(self, dividend: int, divisor: int) -> int:
    """
    A brute force solution that runs in TLE. The runtime is O(D/S) in time and
    space is O(1)

    Args:
      dividend:
      divisor:

    Returns:

    """
    is_neg = (dividend < 0) ^ (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    how_many = 0
    while dividend - divisor >= 0:
      dividend -= divisor
      how_many += 1
    return how_many if not is_neg else -how_many

  def bit_manipulation(self, dividend: int, divisor: int) -> int:
    """
    A bit manipulation solution that runs in O(logD) in time and O(1) in space

    Args:
      dividend:
      divisor:

    Returns:

    """
    is_neg = (dividend < 0) ^ (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    ans = 0

    while dividend >= divisor:
      temp, m = divisor, 1
      while temp << 1 <= dividend:
        temp <<= 1
        m <<= 1
      dividend -= temp
      ans += m
    if is_neg:
      ans = -ans
    return max(-2147483648, min(2147483647, ans))