"""
Solution for 438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""
from collections import Counter
from typing import List

class Solution:
  """
  Runtime: 156 ms, faster than 41.24% of Python3 online submissions for Find All Anagrams in a String.
  Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Find All Anagrams in a String.
  """
  def sub_optimal_solution(self, s: str, p: str) -> List[int]:
    """
    One of the optimal solutions using hash map which runs in O(N) in time and
    O(1) in space

    Args:
      s:
      p:

    Returns:

    """
    if len(s) < len(p):
      return []

    n, res = len(p), []
    s_counter, p_counter = Counter(s[:n]), Counter(p)

    if s_counter == p_counter:
      res.append(0)

    for i in range(1, len(s) - n + 1):
      s_counter[s[i - 1]] -= 1
      s_counter[s[i + n - 1]] += 1

      if s_counter[s[i - 1]] == 0:
        del s_counter[s[i - 1]]

      if s_counter == p_counter:
        res.append(i)
    return res

  def other_sub_optimal_solution(self, s: str, p: str) -> List[int]:
    """
    One of the optimal solutions  that runs in O(N) in time and O(1) in space

    Args:
      s:
      p:

    Returns:

    """
    if len(s) < len(p):
      return []
    n, res = len(p), []
    counter = Counter(p)
    for i in range(len(p)):
      if s[i] in counter:
        counter[s[i]] -= 1

    if all(v == 0 for v in counter.values()):
      res.append(0)

    for i in range(1, len(s) - n + 1):
      if s[i - 1] in counter:
        counter[s[i - 1]] += 1
      if s[i + n - 1] in counter:
        counter[s[i + n - 1]] -= 1
      if all(v == 0 for v in counter.values()):
        res.append(i)
    return res

  def findAnagrams(self, s: str, p: str) -> List[int]:
    """
    Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

    Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

    The order of output does not matter.

    Example 1:

    Input:
    s: "cbaebabacd" p: "abc"

    Output:
    [0, 6]

    Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".
    Example 2:

    Input:
    s: "abab" p: "ab"

    Output:
    [0, 1, 2]

    Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".

    Args:
      s:
      p:

    Returns:

    """
    return self.other_sub_optimal_solution(s, p)