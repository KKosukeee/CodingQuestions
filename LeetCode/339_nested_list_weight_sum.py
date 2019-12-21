"""
Solution for 339. Nested List Weight Sum
https://leetcode.com/problems/nested-list-weight-sum/
"""
from typing import List

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
  """
  Runtime: 28 ms, faster than 89.24% of Python3 online submissions for Nested List Weight Sum.
  Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Nested List Weight Sum.
  """
  def iterative_solution(self, nestedList: List[NestedInteger]) -> int:
    """
    An interative solution that runs in O(N) in time and O(N) in space

    Args:
      nestedList:

    Returns:

    """
    factor, total = 1, 0
    while nestedList:
      temp = []
      for nl in nestedList:
        if nl.isInteger():
          total += factor * nl.getInteger()
        else:
          temp.extend(nl.getList())
      factor += 1
      nestedList = temp
    return total

  def recursive_solution(self, nestedList: List[NestedInteger]) -> int:
    """
    A recursive solution that runs in O(N) in time and space

    Args:
      nestedList:

    Returns:

    """
    def rec(nl, d):
      if nl.isInteger():
        return d * nl.getInteger()
      return sum(rec(n, d + 1) for n in nl.getList())

    return sum(rec(n, 1) for n in nestedList)

  def depthSum(self, nestedList: List[NestedInteger]) -> int:
    """
    Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

    Each element is either an integer, or a list -- whose elements may also be integers or other lists.

    Example 1:

    Input: [[1,1],2,[1,1]]
    Output: 10
    Explanation: Four 1's at depth 2, one 2 at depth 1.
    Example 2:

    Input: [1,[4,[6]]]
    Output: 27
    Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.

    Args:
      nestedList:

    Returns:

    """
    return self.recursive_solution(nestedList)
