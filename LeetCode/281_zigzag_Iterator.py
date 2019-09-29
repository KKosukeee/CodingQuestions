"""
Solution for 281. Zigzag Iterator
https://leetcode.com/problems/zigzag-iterator/
"""
from collections import deque
class ZigzagIterator(object):
    """
    Runtime: 52 ms, faster than 24.18% of Python online submissions for Zigzag Iterator.
    Memory Usage: 12 MB, less than 54.55% of Python online submissions for Zigzag Iterator.
    """
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.

        Given two 1d vectors, implement an iterator to return their elements alternately.

        Example:

        Input:
        v1 = [1,2]
        v2 = [3,4,5,6]

        Output: [1,3,2,4,5,6]

        Explanation: By calling next repeatedly until hasNext returns false,
                     the order of elements returned by next should be: [1,3,2,4,5,6].
        Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

        Clarification for the follow up question:
        The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:

        Input:
        [1,2,3]
        [4,5,6,7]
        [8,9]

        Output: [1,4,8,2,5,9,3,6,7].

        :type v1: List[int]
        :type v2: List[int]
        """
        self.vectors = [deque(v1), deque(v2)]
        self.index = 0
        self.k = 2

    def next(self):
        """
        :rtype: int
        """
        while not self.vectors[self.index]:
            self.index = (self.index + 1) % self.k
        element = self.vectors[self.index].popleft()
        self.index = (self.index + 1) % self.k
        return element

    def hasNext(self):
        """
        :rtype: bool
        """
        return any(vector for vector in self.vectors)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())