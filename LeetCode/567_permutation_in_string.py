"""
Solution for 567. Permutation in String
https://leetcode.com/problems/permutation-in-string/
"""
from collections import Counter

class Solution:
  """
  Runtime: 52 ms, faster than 97.89% of Python3 online submissions for Permutation in String.
  Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Permutation in String.
  """
  def counter_solution(self, s1: str, s2: str) -> bool:
    """
    A solution using hash map that runs in O(max(M, N)) in time and O(1) in space

    Args:
      s1:
      s2:

    Returns:

    """
    c1 = Counter(s1)
    c2 = Counter(s2[:len(s1)])

    if c1 == c2:
      return True

    for i in range(len(s1), len(s2)):
      popout = i - len(s1)
      c2[s2[popout]] -= 1
      c2[s2[i]] += 1

      if c2[s2[popout]] == 0:
        del c2[s2[popout]]

      if c1 == c2:
        return True

    return False

  def bucket_solution(self, s1: str, s2: str) -> bool:
    """
    A solution using bucket that runs same as the counter solution

    Args:
      s1:
      s2:

    Returns:

    """
    c1, c2 = [0 for _ in range(26)], [0 for _ in range(26)]
    for char in s1:
      c1[ord(char) - ord('a')] += 1
    for char in s2[:len(s1)]:
      c2[ord(char) - ord('a')] += 1
    if c1 == c2:
      return True
    for i in range(len(s1), len(s2)):
      c2[ord(s2[i - len(s1)]) - ord('a')] -= 1
      c2[ord(s2[i]) - ord('a')] += 1

      if c1 == c2:
        return True

    return False

  def checkInclusion(self, s1: str, s2: str) -> bool:
    """
    Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.



    Example 1:

    Input: s1 = "ab" s2 = "eidbaooo"
    Output: True
    Explanation: s2 contains one permutation of s1 ("ba").
    Example 2:

    Input:s1= "ab" s2 = "eidboaoo"
    Output: False


    Note:

    The input strings only contain lower case letters.
    The length of both given strings is in range [1, 10,000].

    Args:
      s1:
      s2:

    Returns:

    """
    return self.bucket_solution(s1, s2)