"""
Solution for 340. Longest Substring with At Most K Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
"""
from collections import defaultdict
from collections import OrderedDict

class Solution:
  """
  Runtime: 72 ms, faster than 86.01% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.
  Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.
  """
  def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
    """
    Given a string, find the length of the longest substring T that contains at most k distinct characters.

    Example 1:

    Input: s = "eceba", k = 2
    Output: 3
    Explanation: T is "ece" which its length is 3.
    Example 2:

    Input: s = "aa", k = 1
    Output: 2
    Explanation: T is "aa" which its length is 2.

    Args:
      s:
      k:

    Returns:

    """
    return self.optimal_solution(s, k)

  def initial_solution(self, s: str, k: int) -> int:
    """
    An initial solution that runs in O(N) in time and O(K) in space

    Args:
      s:
      k:

    Returns:

    """
    counter = defaultdict(int)
    i, j, res = 0, 0, 0

    while j < len(s):
      while j < len(s) and len(counter) <= k:
        counter[s[j]] += 1
        j += 1
        if len(counter) <= k:
          res = max(res, j - i)
      while i < j and len(counter) > k:
        counter[s[i]] -= 1
        if counter[s[i]] == 0:
          del counter[s[i]]
        i += 1
    return res

  def optimized_solution(self, s: str, k: int) -> int:
    """
    A time optimized solution that runs in O(NK) in time and O(k) in space

    Args:
      s:
      k:

    Returns:

    """
    index_map = {}
    i, j, res = 0, 0, 0
    while j < len(s):
      while j < len(s) and len(index_map) <= k:
        index_map[s[j]] = j
        j += 1
        if len(index_map) <= k:
          res = max(res, j - i)
      while i < j and len(index_map) > k:
        i = min(index_map.values())
        del index_map[s[i]]
        i += 1
    return res

  def optimal_solution(self, s: str, k: int) -> int:
    """
    An optimal solution combining the initial and optimized solution. It runs
    in O(N) in time and O(K) in space

    Args:
      s:
      k:

    Returns:

    """
    ordered_map = OrderedDict()
    i, j, res = 0, 0, 0
    while j < len(s):
      while j < len(s) and len(ordered_map) <= k:
        if s[j] in ordered_map:
          del ordered_map[s[j]]
        ordered_map[s[j]] = j
        j += 1
        if len(ordered_map) <= k:
          res = max(res, j - i)
      while i < j and len(ordered_map) > k:
        _, i = ordered_map.popitem(last=False)
        i += 1
    return res
