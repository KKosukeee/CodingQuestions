"""
Solution for 139. Word Break
https://leetcode.com/problems/word-break/
"""
from functools import lru_cache
from typing import List

class Solution:
  """
  Runtime: 44 ms, faster than 74.54% of Python3 online submissions for Word Break.
  Memory Usage: 13.1 MB, less than 5.11% of Python3 online submissions for Word Break.
  """

  def naive_approach(self, s, wordDict):
    """
    Naive approach
    Args:
        s: str object to check if it can be constructed from words in wordDict
        wordDict: list of string containing available word

    Returns:
        bool: True if s can be constructed with words in wordDict, otherwise False
    """
    # If s is empty, then return True
    if not s:
      return True

    # Recursive case
    else:
      words = []

      # Loop for each word in wordDict
      for word in wordDict:

        # If s.startswith(word), then call recursively with s sliced
        if s.startswith(word):
          words.append(word)

      for word in words:
        if self.naive_approach(s[len(word):], wordDict):
          return True

      return False

  def optimal_approach(self, s, wordDict):
    """
    Optimal approach
    Args:
        s: str object to check if it can be constructed from words in wordDict
        wordDict: list of string containing available word

    Returns:
        bool: True if s can be constructed with words in wordDict, otherwise False
    """
    n = len(s)
    dp = [False for i in range(n + 1)]
    dp[0] = True
    for i in range(1, n + 1):
      for w in wordDict:
        if dp[i - len(w)] and s[i - len(w):i] == w:
          dp[i] = True
    return dp[-1]

  def backtracking(self, s: str, wordDict: List[str]) -> bool:
    """
    A solution that uses backtracking which runs in O(N^2) in time and O(N) in space

    Args:
      s:
      wordDict:

    Returns:

    """
    word_set = set(wordDict)

    @lru_cache(maxsize=None)
    def backtrack(s):
      if not s:
        return True
      can_form = False
      for j in range(len(s)):
        if s[:j + 1] in word_set:
          can_form |= backtrack(s[j + 1:])
      return can_form

    return backtrack(s)

  def wordBreak(self, s, wordDict):
    """
    Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
    determine if s can be segmented into a space-separated sequence of one or more dictionary
    words.

    Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.
    Example 1:

    Input: s = "leetcode", wordDict = ["leet", "code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".
    Example 2:

    Input: s = "applepenapple", wordDict = ["apple", "pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
                 Note that you are allowed to reuse a dictionary word.
    Example 3:

    Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    Output: false
    Args:
        s: str object to check if it can be constructed from words in wordDict
        wordDict: list of string containing available word

    Returns:
        bool: True if s can be constructed with words in wordDict, otherwise False
    """
    return self.optimal_approach(s, wordDict)
