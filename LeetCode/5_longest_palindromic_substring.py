"""
Solution 5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/
"""

class Solution:
  """
  Runtime: 1356 ms, faster than 52.50% of Python3 online submissions for Longest Palindromic Substring.
  Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Palindromic Substring.
  """
  def longestPalindrome(self, s: str) -> str:
    """
    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

    Example 1:

    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
    Example 2:

    Input: "cbbd"
    Output: "bb"

    Args:
      s:

    Returns:

    """
    return self.expand_center(s)

  def expand_center(self, s: str) -> str:
    """
    A solution that runs in O(N^2) in time and O(1) in space

    Args:
      s:

    Returns:

    """
    self.max_len = 0
    self.max_i, self.max_j = 0, 0

    def expand(i, j):
      while i >= 0 and j < len(s) and s[i] == s[j]:
        if j - i + 1 > self.max_len:
          self.max_len = j - i + 1
          self.max_i, self.max_j = i, j + 1
        i, j = i - 1, j + 1

    for i in range(len(s)):
      expand(i, i)
      expand(i, i + 1)
    return s[self.max_i:self.max_j]

  def dp(self, s: str) -> str:
    """
    A DP solution that runs in O(N^2) in time and space

    Args:
      s:

    Returns:

    """
    dp = [[False] * len(s) for _ in range(len(s))]
    max_i, max_j = 0, 0
    for i in reversed(range(len(s))):
      for j in range(i, len(s)):
        if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
          dp[i][j] = True
          if j - i + 1 > max_j - max_i:
            max_i, max_j = i, j + 1
    return s[max_i:max_j]

  """
   b  a  b  a  d
  [T, F, F, F, T]
  [F, T, F, T, F]
  [F, F, T, F, T]
  [F, F, F, T, F]
  [F, F, F, F, T]
  """
