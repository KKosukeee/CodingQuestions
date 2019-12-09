"""
Solution for 258. Add Digits
https://leetcode.com/problems/add-digits/
"""

class Solution:
  """
  Runtime: 24 ms, faster than 98.03% of Python3 online submissions for Add Digits.
  Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Add Digits.
  """
  def initial_solution(self, num: int) -> int:
    """
    An initial solution that runs in O(logN) in time and O(1) in space

    Args:
      num:

    Returns:

    """
    while num >= 10:
      temp = 0
      while num > 0:
        temp += num % 10
        num //= 10
      num = temp
    return num

  def follow_up(self, num: int) -> int:
    """
    A follow up solution that runs in O(1) in time and O(1) in space

    Args:
      num:

    Returns:

    """
    if num == 0:
      return 0
    else:
      return (num - 1) % 9 + 1

  def addDigits(self, num: int) -> int:
    """
    Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

    Example:

    Input: 38
    Output: 2
    Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
                 Since 2 has only one digit, return it.
    Follow up:
    Could you do it without any loop/recursion in O(1) runtime?

    Args:
      num:

    Returns:

    """
    return self.follow_up(num)