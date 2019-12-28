"""
Solution for 1216. Valid Palindrome III
https://leetcode.com/problems/valid-palindrome-iii/
"""
from functools import lru_cache

class Solution:
  """
  Runtime: 1376 ms, faster than 20.19% of Python3 online submissions for Valid Palindrome III.
  Memory Usage: 285.6 MB, less than 100.00% of Python3 online submissions for Valid Palindrome III.
  """
  def isValidPalindrome(self, s: str, k: int) -> bool:
    """
    Given a string s and an integer k, find out if the given string is a K-Palindrome or not.

    A string is K-Palindrome if it can be transformed into a palindrome by removing at most k characters from it.



    Example 1:

    Input: s = "abcdeca", k = 2
    Output: true
    Explanation: Remove 'b' and 'e' characters.


    Constraints:

    1 <= s.length <= 1000
    s has only lowercase English letters.
    1 <= k <= s.length

    Args:
      s:
      k:

    Returns:

    """
    return self.recursive(s, k)

  def recursive(self, s: str, k: int) -> bool:
    """
    A recursive solution that runs in O(N^2) in time and O(N) in space

    Args:
      s:
      k:

    Returns:

    """
    @lru_cache(maxsize=None)
    def rec(i, j, k):
      if k < 0:
        return False
      if j - i <= k:
        return True
      if s[i] == s[j]:
        return rec(i + 1, j - 1, k)
      else:
        return rec(i + 1, j, k - 1) or rec(i, j - 1, k - 1)

    return rec(0, len(s) - 1, k)
