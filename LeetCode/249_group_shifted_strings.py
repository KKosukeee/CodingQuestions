"""
Solution for 249. Group Shifted Strings
https://leetcode.com/problems/group-shifted-strings/
"""
from collections import defaultdict
from typing import List

class Solution:
  """
  Runtime: 28 ms, faster than 99.87% of Python3 online submissions for Group Shifted Strings.
  Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Group Shifted Strings.
  """
  def groupStrings(self, strings: List[str]) -> List[List[str]]:
    """
    Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

    "abc" -> "bcd" -> ... -> "xyz"
    Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

    Example:

    Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
    Output:
    [
      ["abc","bcd","xyz"],
      ["az","ba"],
      ["acef"],
      ["a","z"]
    ]

    Args:
      strings:

    Returns:

    """
    group = defaultdict(list)
    for word in strings:
      dist = ()
      for i in range(len(word) - 1):
        dist += ((ord(word[i + 1]) - ord(word[i])) % 26,)
      group[dist].append(word)
    return list(group.values())

  """
  - Any group should have the same length
  - Any word with length 1 will be grouped with any word with length equals to one

  Graph solution:
  1. Convert the strings list into distance format i.e. "abc" -> "11"
  2. Sort the tokens by the length of the word
  3. Do the two-pointer to find the same tokens
  """