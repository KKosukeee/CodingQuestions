"""
Solution for 516. Longest Palindromic Subsequence
https://leetcode.com/problems/longest-palindromic-subsequence/
"""
from functools import lru_cache

class Solution:
  """
  Runtime: 840 ms, faster than 87.71% of Python3 online submissions for Longest Palindromic Subsequence.
  Memory Usage: 224.5 MB, less than 7.69% of Python3 online submissions for Longest Palindromic Subsequence.
  """
  def longestPalindromeSubseq(self, s: str) -> int:
    """
    Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

    Example 1:
    Input:

    "bbbab"
    Output:
    4
    One possible longest palindromic subsequence is "bbbb".
    Example 2:
    Input:

    "cbbd"
    Output:
    2
    One possible longest palindromic subsequence is "bb".

    Args:
      s:

    Returns:

    """
    return self.top_down(s)

  def top_down(self, s: str) -> int:
    """
    A top-down solution that runs in O(N) in time and O(N) in space

    Args:
      s:

    Returns:

    """
    @lru_cache(maxsize=None)
    def rec(i, j):
      if i > j:
        return 0
      if i == j:
        return 1
      if s[i] == s[j]:
        return rec(i + 1, j - 1) + 2
      return max(rec(i + 1, j), rec(i, j - 1))

    return rec(0, len(s) - 1)
