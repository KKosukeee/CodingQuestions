"""
Solution for 246. Strobogrammatic Number
https://leetcode.com/problems/strobogrammatic-number/
"""

class Solution:
  """
  Runtime: 24 ms, faster than 83.59% of Python3 online submissions for Strobogrammatic Number.
  Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Strobogrammatic Number.
  """
  def isStrobogrammatic(self, num: str) -> bool:
    """
    A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

    Write a function to determine if a number is strobogrammatic. The number is represented as a string.

    Example 1:

    Input:  "69"
    Output: true
    Example 2:

    Input:  "88"
    Output: true
    Example 3:

    Input:  "962"
    Output: false

    Args:
      num:

    Returns:

    """
    pairs = set([('0', '0'), ('1', '1'), ('8', '8'), ('6', '9'), ('9', '6')])
    i, j = 0, len(num) - 1
    while i <= j:
      if (num[i], num[j]) not in pairs:
        return False
      i, j = i + 1, j - 1
    return True
