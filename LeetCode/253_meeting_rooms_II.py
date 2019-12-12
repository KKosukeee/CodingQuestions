"""
Solution for 253. Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/submissions/
"""
from collections import defaultdict
import heapq
from typing import List

class Solution:
  """
  Runtime: 72 ms, faster than 97.71% of Python3 online submissions for Meeting Rooms II.
  Memory Usage: 16.1 MB, less than 5.41% of Python3 online submissions for Meeting Rooms II.
  """
  def initial_solution(self, intervals: List[List[int]]) -> int:
    """
    An initial solution that runs in O(NLog(N)) in time and O(N) in space

    Args:
      intervals:

    Returns:

    """
    self.schedule = defaultdict(int)

    for start, end in intervals:
      self.schedule[start] += 1
      self.schedule[end] -= 1

    active, maximum = 0, 0
    for key in sorted(self.schedule.keys()):
      active += self.schedule[key]
      maximum = max(maximum, active)

    return maximum

  def heap_solution(self, intervals: List[List[int]]) -> int:
    """
    A heap solution that runs in O(Nlog(N)) in time and O(N) in space

    Args:
      intervals:

    Returns:

    """
    if not intervals:
      return 0
    intervals.sort()
    maximum, pq = 1, [intervals[0][1]]
    for start, end in intervals[1:]:
      if start >= pq[0]:
        _ = heapq.heappop(pq)
      heapq.heappush(pq, end)
      maximum = max(maximum, len(pq))
    return maximum

  def two_pointer_solution(self, intervals: List[List[int]]) -> int:
    """
    A two pointer solution that runs in O(NlogN) in time and O(N) in space

    Args:
      intervals:

    Returns:

    """
    if not intervals:
      return 0

    start, end = [], []
    for s, e in intervals:
      start.append(s),
      end.append(e)

    start.sort()
    end.sort()

    i, j = 0, 0
    active, maximum = 0, 0
    while i < len(start) and j < len(end):
      if start[i] >= end[j]:
        active -= 1
        j += 1
      else:
        active += 1
        i += 1
      maximum = max(maximum, active)
    return maximum

  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    """
    Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

    Example 1:

    Input: [[0, 30],[5, 10],[15, 20]]
    Output: 2
    Example 2:

    Input: [[7,10],[2,4]]
    Output: 1
    NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

    Args:
      intervals:

    Returns:

    """
    return self.heap_solution(intervals)