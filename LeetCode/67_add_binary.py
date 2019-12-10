"""
Solution for 67. Add Binary
https://leetcode.com/problems/add-binary/
"""
from collections import deque

class Solution:
  """
  Runtime: 28 ms, faster than 94.33% of Python3 online submissions for Add Binary.
  Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Add Binary.
  """
  def initial_solution(self, a: str, b: str) -> str:
    """
    An initial solution that runs in O(N+M) in time and O(max(N, M)) in space

    Args:
      a:
      b:

    Returns:

    """
    return bin(int(a, base=2) + int(b, base=2))[2:]

  def loop_solution(self, a: str, b: str) -> str:
    """
    Another solution which runs in O(max(N, M)) in time and O(max(N, M)) in space

    Args:
      a:
      b:

    Returns:

    """
    res, carry, n = deque(), 0, max(len(a), len(b))
    for i in range(n):
      j1 = len(a) - i - 1
      j2 = len(b) - i - 1

      b1, b2 = 0, 0
      if 0 <= j1 < len(a):
        b1 = int(a[j1])
      if 0 <= j2 < len(b):
        b2 = int(b[j2])

      b3 = b1 + b2 + carry
      res.appendleft(str(b3 % 2))
      if b3 > 1:
        carry = 1
      else:
        carry = 0

    if carry:
      res.appendleft('1')
    return ''.join(res)

  def bit_manipulation(self, a: str, b: str) -> str:
    """
    Another solution that runs in O(max(N, M)) in time and O(N+M) in space

    Args:
      a:
      b:

    Returns:

    """
    x, y = int(a, 2), int(b, 2)
    while y:
      answer = x ^ y
      carry = (x & y) << 1
      x, y = answer, carry
    return bin(x)[2:]

  def addBinary(self, a: str, b: str) -> str:
    """
    Given two binary strings, return their sum (also a binary string).

    The input strings are both non-empty and contains only characters 1 or 0.

    Example 1:

    Input: a = "11", b = "1"
    Output: "100"
    Example 2:

    Input: a = "1010", b = "1011"
    Output: "10101"

    Args:
      a:
      b:

    Returns:

    """
    return self.bit_manipulation(a, b)