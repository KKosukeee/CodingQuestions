"""
Solution for 125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
"""

class Solution:
  """
  Runtime: 48 ms, faster than 77.13% of Python3 online submissions for Valid Palindrome.
  Memory Usage: 13.4 MB, less than 71.43% of Python3 online submissions for Valid Palindrome.
  """
  def isPalindrome(self, s: str) -> bool:
    """
    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

    Note: For the purpose of this problem, we define empty string as valid palindrome.

    Example 1:

    Input: "A man, a plan, a canal: Panama"
    Output: true
    Example 2:

    Input: "race a car"
    Output: false

    Args:
      s:

    Returns:

    """
    return self.one_pass(s)

  def two_pass(self, s: str) -> bool:
    """
    A two pass solution that runs in O(N) in time and space

    Args:
      s:

    Returns:

    """
    s = [char.lower() for char in s if char.isalnum()]
    return s == s[::-1]

  def one_pass(self, s: str) -> bool:
    """
    A one pass solution that runs in O(N) in time and O(1) in space

    Args:
      s:

    Returns:

    """
    i, j = 0, len(s) - 1
    while i <= j:
      while i <= j and not s[i].isalnum():
        i += 1
      while i <= j and not s[j].isalnum():
        j -= 1
      if i <= j and s[i].lower() != s[j].lower():
        return False
      i, j = i + 1, j - 1
    return True
