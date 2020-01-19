"""
Solution for 1324. Print Words Vertically
https://leetcode.com/problems/print-words-vertically/
"""
from itertools import zip_longest
from typing import List

class Solution:
  """
  Runtime: 20 ms, faster than 100.00% of Python3 online submissions for Print Words Vertically.
  Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Print Words Vertically.
  """
  def printVertically(self, s: str) -> List[str]:
    """
    Given a string s. Return all the words vertically in the same order in which they appear in s.
    Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
    Each word would be put on only one column and that in one column there will be only one word.



    Example 1:

    Input: s = "HOW ARE YOU"
    Output: ["HAY","ORO","WEU"]
    Explanation: Each word is printed vertically.
     "HAY"
     "ORO"
     "WEU"
    Example 2:

    Input: s = "TO BE OR NOT TO BE"
    Output: ["TBONTB","OEROOE","   T"]
    Explanation: Trailing spaces is not allowed.
    "TBONTB"
    "OEROOE"
    "   T"
    Example 3:

    Input: s = "CONTEST IS COMING"
    Output: ["CIC","OSO","N M","T I","E N","S G","T"]


    Constraints:

    1 <= s.length <= 200
    s contains only upper case English letters.
    It's guaranteed that there is only one space between 2 words.

    Args:
      s:

    Returns:

    """
    return self.one_linear(s)

  def one_linear(self, s):
    """
    A one-linear solution that runs in O(NM) where N = max(len(words[i])) and
    M = len(words) in time and O(MN) in space

    Args:
      s:

    Returns:

    """
    return [''.join(a).rstrip() for a in zip_longest(*s.split(), fillvalue=' ')]

  def initial(self, s: str) -> List[str]:
    """
    An initial solution that runs in O(MN) in time and space

    Args:
      s:

    Returns:

    """
    words = s.split()
    res = []
    n = max(words, key=lambda x: len(x))
    for i in range(len(n)):
      temp = ''
      for word in words:
        if not i < len(word):
          temp += ' '
        else:
          temp += word[i]
      res.append(temp.rstrip())
    return res