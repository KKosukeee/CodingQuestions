"""
Solution for 341. Flatten Nested List Iterator
https://leetcode.com/problems/flatten-nested-list-iterator/

Runtime: 60 ms, faster than 96.93% of Python online submissions for Flatten Nested List Iterator.
Memory Usage: 17.6 MB, less than 32.26% of Python online submissions for Flatten Nested List Iterator.
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
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

from collections import deque

class NestedIterator(object):
    """
    Given a nested list of integers, implement an iterator to flatten it.

    Each element is either an integer, or a list -- whose elements may also be integers or other lists.

    Example 1:

    Input: [[1,1],2,[1,1]]
    Output: [1,1,2,1,1]
    Explanation: By calling next repeatedly until hasNext returns false,
                 the order of elements returned by next should be: [1,1,2,1,1].
    Example 2:

    Input: [1,[4,[6]]]
    Output: [1,4,6]
    Explanation: By calling next repeatedly until hasNext returns false,
                 the order of elements returned by next should be: [1,4,6].
    """
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.flat_list = deque()
        def rec(x):
          if x.isInteger():
            self.flat_list.append(x.getInteger())
          else:
            for nl in x.getList():
              rec(nl)
        for nl in nestedList:
          rec(nl)

    def next(self):
        """
        :rtype: int
        """
        return self.flat_list.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.flat_list

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())