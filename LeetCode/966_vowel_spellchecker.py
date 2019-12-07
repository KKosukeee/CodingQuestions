"""
Solution for 966. Vowel Spellchecker
https://leetcode.com/problems/vowel-spellchecker/
"""
from typing import List

class Solution:
  """
  Runtime: 180 ms, faster than 97.59% of Python3 online submissions for Vowel Spellchecker.
  Memory Usage: 15.5 MB, less than 100.00% of Python3 online submissions for Vowel Spellchecker.
  """
  def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
    """
    Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

    For a given query word, the spell checker handles two categories of spelling mistakes:

    Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
    Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
    Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
    Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
    Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
    Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
    Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
    Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
    In addition, the spell checker operates under the following precedence rules:

    When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
    When the query matches a word up to capitlization, you should return the first such match in the wordlist.
    When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
    If the query has no matches in the wordlist, you should return the empty string.
    Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].



    Example 1:

    Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
    Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]


    Note:

    1 <= wordlist.length <= 5000
    1 <= queries.length <= 5000
    1 <= wordlist[i].length <= 7
    1 <= queries[i].length <= 7
    All strings in wordlist and queries consist only of english letters.

    Args:
      wordlist:
      queries:

    Returns:

    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = [''] * len(queries)

    exact_words = set(wordlist)
    capital_words = {}
    vowel_words = {}

    for i, word in enumerate(wordlist):
      capital_key = word.lower()
      vowel_key = ''.join(
        [char if char not in vowels else '*' for char in capital_key])

      capital_words.setdefault(capital_key, i)
      vowel_words.setdefault(vowel_key, i)

    for i, query in enumerate(queries):
      if query in exact_words:
        result[i] = query
        continue
      lowered = query.lower()
      if lowered in capital_words:
        result[i] = wordlist[capital_words[lowered]]
        continue
      voweled = ''.join(
        [char if char not in vowels else '*' for char in lowered])
      if voweled in vowel_words:
        result[i] = wordlist[vowel_words[voweled]]
    return result

  """
  1. Find the exact match
  2. Find the capitalization matter
  3. Find the vowel matter
  """