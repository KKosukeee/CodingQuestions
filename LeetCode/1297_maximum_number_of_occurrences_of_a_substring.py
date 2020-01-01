"""
Solution for 1297. Maximum Number of Occurrences of a Substring
https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/
"""
from collections import defaultdict

class Solution:
  """
  Runtime: 208 ms, faster than 63.51% of Python3 online submissions for Maximum Number of Occurrences of a Substring.
  Memory Usage: 14.9 MB, less than 100.00% of Python3 online submissions for Maximum Number of Occurrences of a Substring.
  """
  def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    """
    Given a string s, return the maximum number of ocurrences of any substring under the following rules:

    The number of unique characters in the substring must be less than or equal to maxLetters.
    The substring size must be between minSize and maxSize inclusive.


    Example 1:

    Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
    Output: 2
    Explanation: Substring "aab" has 2 ocurrences in the original string.
    It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
    Example 2:

    Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
    Output: 2
    Explanation: Substring "aaa" occur 2 times in the string. It can overlap.
    Example 3:

    Input: s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
    Output: 3
    Example 4:

    Input: s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
    Output: 0


    Constraints:

    1 <= s.length <= 10^5
    1 <= maxLetters <= 26
    1 <= minSize <= maxSize <= min(26, s.length)
    s only contains lowercase English letters.

    Args:
      s:
      maxLetters:
      minSize:
      maxSize:

    Returns:

    """
    return self.optimized(s, maxLetters, minSize, maxSize)

  def sliding_window(self, s: str, maxLetters: int, minSize: int,
                     maxSize: int) -> int:
    """
    A slinding window approach that runs in O(len(S)*minSize) in time and
    O(minSize) in space

    Args:
      s:
      maxLetters:
      minSize:
      maxSize:

    Returns:

    """
    freq_map = defaultdict(int)
    for i in range(len(s) - minSize + 1):
      if len(set(s[i:i + minSize])) <= maxLetters:
        freq_map[s[i:i + minSize]] += 1
    return max(freq_map.values(), default=0)

  def optimized(self, s: str, maxLetters: int, minSize: int,
                maxSize: int) -> int:
    """
    An optimized solution that runs in O(len(s)) in time and O(minSize) in space

    Args:
      s:
      maxLetters:
      minSize:
      maxSize:

    Returns:

    """
    freq_map = defaultdict(int)
    window = defaultdict(int)
    i = 0
    for j in range(len(s)):
      window[s[j]] += 1
      if j - i + 1 > minSize:
        while j - i + 1 > minSize:
          window[s[i]] -= 1
          if window[s[i]] == 0:
            del window[s[i]]
          i += 1
      if j - i + 1 == minSize and len(window) <= maxLetters:
        freq_map[s[i:j + 1]] += 1
    return max(freq_map.values(), default=0)