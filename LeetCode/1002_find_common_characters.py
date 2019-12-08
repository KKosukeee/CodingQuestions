"""
Solution for 1002. Find Common Characters
https://leetcode.com/problems/find-common-characters/
"""
from collections import Counter
from functools import reduce
from operator import and_
from typing import List

class Solution:
  """
  Runtime: 44 ms, faster than 92.64% of Python3 online submissions for Find Common Characters.
  Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Find Common Characters.
  """
  def initial_solution(self, A: List[str]) -> List[str]:
    """
    An initial solution that runs in O(N*max(len(A[i]))) in the worst case in
    time and O(N) in space

    Args:
      A:

    Returns:

    """
    counters, sets = [], []
    for word in A:
      counters.append(Counter(word))
      sets.append(set(word))
    result = []
    for char in reduce(lambda a, b: a.intersection(b), sets):
      result.extend([char] * min(counter[char] for counter in counters))
    return result

  def better_solution(self, A: List[str]) -> List[str]:
    """
    A better solution that runs in O(N*M) in time and O(N*M) in space

    Args:
      A:

    Returns:

    """
    counter = Counter(A[0])
    for word in A:
      counter &= Counter(word)
    return counter.elements()

  def one_linear(self, A: List[str]) -> List[str]:
    """
    A one-linear solution that is same as the self.better_solution

    Args:
      A:

    Returns:

    """
    return reduce(and_, map(Counter, A)).elements()

  def commonChars(self, A: List[str]) -> List[str]:
    return self.one_linear(A)
