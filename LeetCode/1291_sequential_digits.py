"""
Solution for 1291. Sequential Digits
https://leetcode.com/problems/sequential-digits/
"""
from typing import List

class Solution:
  """
  Runtime: 24 ms, faster than 100.00% of Python3 online submissions for Sequential Digits.
  Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Sequential Digits.
  """
  def initial_solution(self, low: int, high: int) -> List[int]:
    """
    An initial solution that runs in O(1) in time and O(1) in space

    Args:
      low:
      high:

    Returns:

    """
    i, n, res = 0, len(str(low)), []
    seq = ''.join(str(i) for i in range(1, 10))  # 123456789

    while i < len(seq) and int(seq[i:i + n]) < low:
      if i + n == len(seq):
        i, n = 0, n + 1
      else:
        i += 1

    if not i < len(seq):
      return []

    while i < len(seq) and i + n <= len(seq) and int(seq[i:i + n]) <= high:
      res.append(int(seq[i:i + n]))
      if i + n == len(seq):
        i, n = 0, n + 1
      else:
        i += 1
    return res

  def log10_solution(self, low: int, high: int) -> List[int]:
    """
    The other solution that runs in O(1) in time and O(1) in space

    Args:
      low:
      high:

    Returns:

    """
    ans = []
    for i in range(1, 9):
      num = curr = i
      while num <= high and curr < 10:
        if num >= low:
          ans.append(num)
        curr += 1
        num = num * 10 + curr
    return sorted(ans)

  def sequentialDigits(self, low: int, high: int) -> List[int]:
    """
    An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

    Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.



    Example 1:

    Input: low = 100, high = 300
    Output: [123,234]
    Example 2:

    Input: low = 1000, high = 13000
    Output: [1234,2345,3456,4567,5678,6789,12345]


    Constraints:

    10 <= low <= high <= 10^9

    Args:
      low:
      high:

    Returns:

    """
    return self.log10_solution(low, high)
