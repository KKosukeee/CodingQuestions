"""
Solution for 809. Expressive Words
https://leetcode.com/problems/expressive-words/
"""
from itertools import groupby
from typing import List

class Solution:
  """
  Runtime: 48 ms, faster than 89.27% of Python3 online submissions for Expressive Words.
  Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Expressive Words.
  """
  def ugly_solution(self, S: str, words: List[str]) -> int:
    """
    An ugly solution that works and runs in O(len(S)+len(W)*max(len(W[i])) in time
    and space

    Args:
      S:
      words:

    Returns:

    """
    count = 0
    k, v = [], []
    for key, value in groupby(S):
      k.append(key)
      v.append(list(value))
    kk, vv = [], []
    for word in words:
      kkk, vvv = [], []
      for key, value in groupby(word):
        kkk.append(key)
        vvv.append(list(value))
      kk.append(kkk)
      vv.append(vvv)
    for kkk, vvv in zip(kk, vv):
      valid = True
      if len(kkk) != len(k) or kkk != k:
        continue
      for _v, _vvv in zip(v, vvv):
        if len(_v) < len(_vvv):
          valid = False
          break
        if len(_v) < 3 and len(_v) != len(_vvv):
          valid = False
          break
      count += int(valid)
    return count

  def better_solution(self, S: str, words: List[str]) -> int:
    """
    A better solution that runs in same run and time complexity

    Args:
      S:
      words:

    Returns:

    """
    def encode(S):
      return zip(*[(k, len(list(v))) for k, v in groupby(S)])

    k, v = encode(S)
    count = 0
    for word in words:
      kk, vv = encode(word)
      if k != kk:
        continue
      count += int(all(c1 >= max(c2, 3) or c1 == c2 for c1, c2 in zip(v, vv)))
    return count

  def expressiveWords(self, S: str, words: List[str]) -> int:
    """
    Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

    For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

    For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

    Given a list of query words, return the number of words that are stretchy.



    Example:
    Input:
    S = "heeellooo"
    words = ["hello", "hi", "helo"]
    Output: 1
    Explanation:
    We can extend "e" and "o" in the word "hello" to get "heeellooo".
    We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.


    Notes:

    0 <= len(S) <= 100.
    0 <= len(words) <= 100.
    0 <= len(words[i]) <= 100.
    S and all words in words consist only of lowercase letters

    Args:
      S:
      words:

    Returns:

    """
    return self.better_solution(S, words)

  """
  1. Tokenize the S
  2. Loop through words
    2.1 Compare the string
    2.2 
        *  *
  S = "hello" 
  words = ["hello", "hi", "helo", "heello", "wello", "helllo"]
  """