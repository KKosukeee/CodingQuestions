"""
Solution for 1309. Decrypt String from Alphabet to Integer Mapping
https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
"""

class Solution:
  """
  Runtime: 24 ms, faster than 89.61% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
  Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
  """
  def freqAlphabets(self, s: str) -> str:
    """
    Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

    Characters ('a' to 'i') are represented by ('1' to '9') respectively.
    Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
    Return the string formed after mapping.

    It's guaranteed that a unique mapping will always exist.



    Example 1:

    Input: s = "10#11#12"
    Output: "jkab"
    Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
    Example 2:

    Input: s = "1326#"
    Output: "acz"
    Example 3:

    Input: s = "25#"
    Output: "y"
    Example 4:

    Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
    Output: "abcdefghijklmnopqrstuvwxyz"


    Constraints:

    1 <= s.length <= 1000
    s[i] only contains digits letters ('0'-'9') and '#' letter.
    s will be valid string such that mapping is always possible.

    Args:
      s:

    Returns:

    """
    return self.one_pass(s)

  def two_passes(self, s: str) -> str:
    """
    A solution that runs twice which runs in O(N) in time and O(1) in space

    Args:
      s:

    Returns:

    """
    alpha_map = {
      '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g',
      '8': 'h', '9': 'i', '10': 'j', '11': 'k', '12': 'l', '13': 'm', '14': 'n',
      '15': 'o', '16': 'p', '17': 'q', '18': 'r', '19': 's', '20': 't',
      '21': 'u',
      '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z'
    }
    splitted = s.split('#')
    res = ''

    for i in range(len(splitted)):
      j = 0
      if i + 1 < len(splitted) and len(splitted[i]) > 2:
        while j < len(splitted[i]) - 2:
          res += alpha_map[splitted[i][j]]
          j += 1

      if i + 1 < len(splitted):
        res += alpha_map[splitted[i][j:]]
      else:
        while j < len(splitted[i]):
          res += alpha_map[splitted[i][j]]
          j += 1
    return res

  def one_pass(self, s: str) -> str:
    """
    A one pass solution that runs in O(N) in time and O(1) in space

    Args:
      s:

    Returns:

    """
    alpha_map = {
      '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g',
      '8': 'h', '9': 'i', '10': 'j', '11': 'k', '12': 'l', '13': 'm', '14': 'n',
      '15': 'o', '16': 'p', '17': 'q', '18': 'r', '19': 's', '20': 't',
      '21': 'u',
      '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z'
    }

    i, res = 0, ''
    while i < len(s):
      if i + 2 < len(s) and s[i + 2] == '#':
        res += alpha_map[s[i:i + 2]]
        i += 3
      else:
        res += alpha_map[s[i]]
        i += 1
    return res
