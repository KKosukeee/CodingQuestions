"""
Solution for 247. Strobogrammatic Number II
https://leetcode.com/problems/strobogrammatic-number-ii/
"""
from typing import List

class Solution:
  """
  Runtime: 108 ms, faster than 81.01% of Python3 online submissions for Strobogrammatic Number II.
  Memory Usage: 18.7 MB, less than 100.00% of Python3 online submissions for Strobogrammatic Number II.
  """
  def findStrobogrammatic(self, n: int) -> List[str]:
    """
    A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

    Find all strobogrammatic numbers that are of length = n.

    Example:

    Input:  n = 2
    Output: ["11","69","88","96"]

    Args:
      n:

    Returns:

    """
    def rec(n, m):
      if n == 0:
        return ['']
      elif n == 1:
        return ['0', '1', '8']

      inners = rec(n - 2, m)
      res = []

      for inner in inners:
        if n != m:
          res.append('0' + inner + '0')
        res.append('1' + inner + '1')
        res.append('8' + inner + '8')
        res.append('6' + inner + '9')
        res.append('9' + inner + '6')
      return res

    return rec(n, n)