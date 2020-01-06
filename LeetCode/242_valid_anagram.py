"""
Solution for 242. Valid Anagram
https://leetcode.com/problems/valid-anagram/
"""
from collections import Counter

class Solution:
  """
  Runtime: 48 ms, faster than 61.01% of Python3 online submissions for Valid Anagram.
  Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Valid Anagram.
  """
  def isAnagram(self, s: str, t: str) -> bool:
    """
    Given two strings s and t , write a function to determine if t is an anagram of s.

    Example 1:

    Input: s = "anagram", t = "nagaram"
    Output: true
    Example 2:

    Input: s = "rat", t = "car"
    Output: false
    Note:
    You may assume the string contains only lowercase alphabets.

    Follow up:
    What if the inputs contain unicode characters? How would you adapt your solution to such case?

    Args:
      s:
      t:

    Returns:

    """
    return self.hash_map(s, t)

  def hash_map(self, s: str, t: str) -> bool:
    """
    A solution using a hash map that runs in O(len(s) + len(t)) in time and O(s) in space

    Args:
      s:
      t:

    Returns:

    """
    counter = Counter(s)
    for char in t:
      if char not in counter:
        return False
      counter[char] -= 1
    return all(counter[char] == 0 for char in counter.keys())

  def counter(self, s: str, t: str) -> bool:
    """
    A solution using counter data structure which runs in O(len(s)+len(t)) in
    time and space

    Args:
      s:
      t:

    Returns:

    """
    return Counter(s) == Counter(t)

  def sort(self, s: str, t: str) -> bool:
    """
    A solution using a sorting algorithm that runs in O(len(s)log(len(s))) in time
    and O(1) in space

    Args:
      s:
      t:

    Returns:

    """
    if len(s) != len(t):
      return False
    return sorted(s) == sorted(t)