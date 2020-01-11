"""
Solution for 50. Pow(x, n)
https://leetcode.com/problems/powx-n/
"""

class Solution:
  """
  Runtime: 28 ms, faster than 64.49% of Python3 online submissions for Pow(x, n).
  Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Pow(x, n).
  """
  def myPow(self, x: float, n: int) -> float:
    """
    Implement pow(x, n), which calculates x raised to the power n (xn).

    Example 1:

    Input: 2.00000, 10
    Output: 1024.00000
    Example 2:

    Input: 2.10000, 3
    Output: 9.26100
    Example 3:

    Input: 2.00000, -2
    Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25
    Note:

    -100.0 < x < 100.0
    n is a 32-bit signed integer, within the range [−231, 231 − 1]

    Args:
      x:
      n:

    Returns:

    """
    if n < 0:
      x = 1 / x
      n = -n
    return self.recursive(x, n)

  def cheat(self, x: float, n: int) -> float:
    """
    A solution using power operator (cheating!)

    Args:
      x:
      n:

    Returns:

    """
    return x ** n

  def brute_force(self, x: float, n: int) -> float:
    """
    Most straight forward solution that runs in O(N) in time and O(1) in space

    Args:
      x:
      n:

    Returns:

    """
    if n < 0:
      x = 1 / x
      n = -n
    ans = 1
    for _ in range(n):
      ans *= x
    return ans

  def recursive(self, x: float, n: int) -> float:
    """
    A recursive solution that runs in O(LogN) in time and O(logN) in space

    Args:
      x:
      n:

    Returns:

    """
    if n == 0:
      return 1.0
    half = self.recursive(x, n // 2)
    if n % 2 == 0:
      return half * half
    return half * half * x
