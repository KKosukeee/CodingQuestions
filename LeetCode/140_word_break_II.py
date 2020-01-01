"""
Solution for 140. Word Break II
https://leetcode.com/problems/word-break-ii/
"""
from functools import lru_cache
from typing import List

class Solution:
  """
  Runtime: 48 ms, faster than 71.25% of Python3 online submissions for Word Break II.
  Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Word Break II.
  """
  def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    """
    Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

    Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.
    Example 1:

    Input:
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    Output:
    [
      "cats and dog",
      "cat sand dog"
    ]
    Example 2:

    Input:
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    Output:
    [
      "pine apple pen apple",
      "pineapple pen apple",
      "pine applepen apple"
    ]
    Explanation: Note that you are allowed to reuse a dictionary word.
    Example 3:

    Input:
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    Output:
    []

    Args:
      s:
      wordDict:

    Returns:

    """
    return self.backtracking(s, wordDict)

  def backtracking(self, s: str, wordDict: List[str]) -> List[str]:
    """
    A backtracking solution that runs in O(SW) in time and O(S) in time

    Args:
      s:
      wordDict:

    Returns:

    """
    @lru_cache(maxsize=None)
    def rec(s):
      if not s:
        return ['']
      res = []
      for word in wordDict:
        if s.startswith(word):
          sublist = rec(s[len(word):])
          for sub in sublist:
            if sub:
              res.append(word + ' ' + sub)
            else:
              res.append(word + sub)
      return res

    return rec(s)