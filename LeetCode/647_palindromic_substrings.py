"""
Solution for 647. Palindromic Substrings
https://leetcode.com/problems/palindromic-substrings/
"""
from functools import lru_cache

class Solution:
  """
  Runtime: 160 ms, faster than 54.46% of Python3 online submissions for Palindromic Substrings.
  Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Palindromic Substrings.
  """
  def countSubstrings(self, s: str) -> int:
    """
    Given a string, your task is to count how many palindromic substrings in this string.

    The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

    Example 1:

    Input: "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".


    Example 2:

    Input: "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


    Note:

    The input string length won't exceed 1000.

    Args:
      s:

    Returns:

    """
    return self.optimal_solution(s)

  def initial_solution(self, s: str) -> int:
    """
    An initial solution that runs in O(N^3) in time and O(1) in space

    Args:
      s:

    Returns:

    """
    @lru_cache(maxsize=None)
    def is_palindrome(i, j):
      if not i < j:
        return True
      if s[i] == s[j]:
        return is_palindrome(i + 1, j - 1)
      return False

    palins = set()
    for i in range(len(s)):
      for j in range(i, len(s)):
        if is_palindrome(i, j):
          palins.add((i, j))
    return len(palins)

  def optimal_solution(self, s: str) -> int:
    """
    An optimal solution that runs in O(N^2) in time and O(1) in space

    Args:
      s:

    Returns:

    """
    self.count = 0

    def expand_window(i, j):
      while i >= 0 and j < len(s) and s[i] == s[j]:
        i, j = i - 1, j + 1
        self.count += 1

    for i in range(len(s)):
      expand_window(i, i)
      expand_window(i, i + 1)
    return self.count

  def dp(self, s: str) -> int:
    """
    A DP solution that runs in O(N^2) in time and space

    Args:
      s:

    Returns:

    """
    dp = [[False] * len(s) for _ in range(len(s))]
    res = 0
    for i in reversed(range(len(s))):
      for j in range(i, len(s)):
        if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
          dp[i][j] = True
          res += 1
    return res
