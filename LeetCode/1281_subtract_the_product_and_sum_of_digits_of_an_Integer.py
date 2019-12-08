"""
Solution for 1281. Subtract the Product and Sum of Digits of an Integer
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
"""

class Solution:
  """
  Runtime: 28 ms, faster than 100.00% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
  Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
  """
  def initial_solution(self, n: int) -> int:
    """
    An initial solution that runs in O(LogN) in time and O(1) where the base for
    the log operation is 10

    Args:
      n:

    Returns:

    """
    p, s = 1, 0
    for d in str(n):
      p *= int(d)
      s += int(d)
    return p - s

  def yet_another_solution(self, n: int) -> int:
    """
    The other solution that runs in same as the initial_solution

    Args:
      n:

    Returns:

    """
    p, s = 1, 0
    while n > 0:
      s += n % 10
      p *= n % 10
      n = n // 10
    return p - s

  def subtractProductAndSum(self, n: int) -> int:
    """
    Given an integer number n, return the difference between the product of its digits and the sum of its digits.


    Example 1:

    Input: n = 234
    Output: 15
    Explanation:
    Product of digits = 2 * 3 * 4 = 24
    Sum of digits = 2 + 3 + 4 = 9
    Result = 24 - 9 = 15
    Example 2:

    Input: n = 4421
    Output: 21
    Explanation:
    Product of digits = 4 * 4 * 2 * 1 = 32
    Sum of digits = 4 + 4 + 2 + 1 = 11
    Result = 32 - 11 = 21


    Constraints:

    1 <= n <= 10^5

    Args:
      n:

    Returns:

    """
    return self.yet_another_solution(n)