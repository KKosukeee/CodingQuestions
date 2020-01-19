"""
Solution for 1323. Maximum 69 Number
https://leetcode.com/problems/maximum-69-number/
"""

class Solution:
  """
  Runtime: 24 ms, faster than 100.00% of Python3 online submissions for Maximum 69 Number.
  Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Maximum 69 Number.
  """
  def maximum69Number(self, num: int) -> int:
    """
    Given a positive integer num consisting only of digits 6 and 9.

    Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).



    Example 1:

    Input: num = 9669
    Output: 9969
    Explanation:
    Changing the first digit results in 6669.
    Changing the second digit results in 9969.
    Changing the third digit results in 9699.
    Changing the fourth digit results in 9666.
    The maximum number is 9969.
    Example 2:

    Input: num = 9996
    Output: 9999
    Explanation: Changing the last digit 6 to 9 results in the maximum number.
    Example 3:

    Input: num = 9999
    Output: 9999
    Explanation: It is better not to apply any change.


    Constraints:

    1 <= num <= 10^4
    num's digits are 6 or 9.

    Args:
      num:

    Returns:

    """
    return self.one_linear(num)

  def one_linear(self, num):
    """
    A one-linear solution that runs in O(N) in time where N = len(num) and O(N)
    in space

    Args:
      num:

    Returns:

    """
    return int(str(num).replace('6', '9', 1))

  def initial_solution(self, num: int) -> int:
    res, ignore = 0, False
    for digit in str(num):
      digit = int(digit)
      if not ignore and digit == 6:
        digit = 9
        ignore = True
      res = res * 10 + digit
    return res
