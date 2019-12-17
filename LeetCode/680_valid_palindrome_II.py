"""
Solution for 680. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/
"""

class Solution:
  """
  Runtime: 104 ms, faster than 79.87% of Python3 online submissions for Valid Palindrome II.
  Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Valid Palindrome II.
  """
  def brute_force(self, s: str) -> bool:
    """
    A brute force solution that runs in TLE

    Args:
      s:

    Returns:

    """
    if self.is_palindrome(s):
      return True
    for i in range(len(s)):
      if self.is_palindrome(s[:i] + s[i + 1:]):
        return True
    return False

  def is_palindrome(self, s):
    if len(s) % 2 == 1:
      m = len(s) // 2
      return self.is_palindrome(s[:m] + s[m + 1:])
    i, j = len(s) // 2 - 1, len(s) // 2
    while 0 <= i < len(s) and 0 <= j < len(s):
      if s[i] != s[j]:
        return False
      i, j = i - 1, j + 1
    return True

  def optimal_solution(self, s: str) -> bool:
    """
    An optimal solution that runs in O(N) in time and O(1) in space

    Args:
      s:

    Returns:

    """
    def is_palindrome(i, j):
      return all(s[k] == s[j - k + i] for k in range(i, j))

    for i in range(len(s) // 2):
      if s[i] != s[~i]:
        j = len(s) - 1 - i
        return is_palindrome(i + 1, j) or is_palindrome(i, j - 1)
    return True

  """
  abcd
  """

  def better_solution(self, s: str) -> bool:
    """
    Slightly more readable solution that runs in O(N) in time and O(N) in space
    as well dude. 

    Args:
      s:

    Returns:

    """
    i, j = 0, len(s) - 1
    while i <= j:
      if s[i] != s[j]:
        one, two = s[i + 1:j + 1], s[i:j]
        return one == one[::-1] or two == two[::-1]
      i, j = i + 1, j - 1
    return True

  def validPalindrome(self, s: str) -> bool:
    """
    Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

    Example 1:
    Input: "aba"
    Output: True
    Example 2:
    Input: "abca"
    Output: True
    Explanation: You could delete the character 'c'.
    Note:
    The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

    Args:
      s:

    Returns:

    """
    return self.better_solution(s)

  """
  aabaa
  aabcaa
  aabcdaa
  """