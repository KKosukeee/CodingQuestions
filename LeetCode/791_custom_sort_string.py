"""
Solution for 791. Custom Sort String
https://leetcode.com/problems/custom-sort-string/
"""
from collections import defaultdict
from collections import Counter

class Solution:
  """
  Runtime: 24 ms, faster than 95.14% of Python3 online submissions for Custom Sort String.
  Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Custom Sort String.
  """
  def customSortString(self, S: str, T: str) -> str:
    """
    S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

    S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

    Return any permutation of T (as a string) that satisfies this property.

    Example :
    Input:
    S = "cba"
    T = "abcd"
    Output: "cbad"
    Explanation:
    "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
    Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.


    Note:

    S has length at most 26, and no character is repeated in S.
    T has length at most 200.
    S and T consist of lowercase letters only.

    Args:
      S:
      T:

    Returns:

    """
    return self.sort_solution(S, T)

  def optimal_solution(self, S: str, T: str) -> str:
    """
    An optimal solution that runs in O(M+N) where M = len(S) and N = len(T) in
    time and O(1) in space

    Args:
      S:
      T:

    Returns:

    """
    index_map = defaultdict(lambda: -1)
    chars_map = defaultdict(list)
    for i, char in enumerate(S):
      index_map[char] = i
    for char in T:
      chars_map[index_map[char]].append(char)
    return ''.join(''.join(chars_map[i]) for i in range(-1, 26))

  def counter_solution(self, S: str, T: str) -> str:
    """
    A solution that uses counter that runs in O(M+N) in time and O(1) in space

    Args:
      S:
      T:

    Returns:

    """
    counter = Counter(T)
    ans = []
    for char in S:
      ans.append(char * counter[char])
      counter[char] = 0
    for char in counter:
      ans.append(char * counter[char])
    return ''.join(ans)

  def sort_solution(self, S: str, T: str) -> str:
    """
    A sort solution that runs in O(M+Nlog(N)) in time and O(1) in space

    Args:
      S:
      T:

    Returns:

    """
    order_map = defaultdict(lambda: -1)
    for i, char in enumerate(S):
      order_map[char] = i
    return ''.join(sorted(T, key=lambda char: order_map[char]))