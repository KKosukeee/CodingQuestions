"""
Solution for 1272. Remove Interval
https://leetcode.com/problems/remove-interval/
"""
from copy import deepcopy
from typing import List

class Solution:
  """
  Runtime: 400 ms, faster than 89.03% of Python3 online submissions for Remove Interval.
  Memory Usage: 19.5 MB, less than 100.00% of Python3 online submissions for Remove Interval.
  """
  def initial_solution(self, intervals: List[List[int]],
                       toBeRemoved: List[int]) -> List[List[int]]:
    """
    An initial solution that runs in O(N) in time and O(N) in space

    Args:
      intervals:
      toBeRemoved:

    Returns:

    """
    start_times = [interval[0] for interval in intervals]
    end_times = [interval[1] for interval in intervals]
    start_pivot = bisect.bisect_right(start_times, toBeRemoved[0])
    end_pivot = bisect.bisect_right(end_times, toBeRemoved[1])

    left_half = deepcopy(intervals[:start_pivot])
    if left_half:
      left_half[-1][1] = min(left_half[-1][1], toBeRemoved[0])
    right_half = intervals[end_pivot:]
    if right_half:
      right_half[0][0] = max(right_half[0][0], toBeRemoved[1])
    return filter(lambda x: x[0] < x[1], left_half + right_half)

  def better_solution(self, intervals: List[List[int]],
                      toBeRemoved: List[int]) -> List[List[int]]:
    """
    A better solution that runs in O(N) in time and O(1) in space

    Args:
      intervals:
      toBeRemoved:

    Returns:

    """
    new_intervals = []
    for interval in intervals:
      if toBeRemoved[0] < interval[0] < toBeRemoved[1] and toBeRemoved[0] < \
          interval[1] < toBeRemoved[1]:
        continue
      elif interval[1] < toBeRemoved[0]:
        new_intervals.append(interval)
      elif interval[0] > toBeRemoved[1]:
        new_intervals.append(interval)
      elif not toBeRemoved[0] < interval[0] < toBeRemoved[1] and not \
      toBeRemoved[0] < interval[1] < toBeRemoved[1]:
        new_intervals.extend(
          [[interval[0], toBeRemoved[0]], [toBeRemoved[1], interval[1]]])
      elif toBeRemoved[0] < interval[0] < toBeRemoved[1]:
        new_intervals.append([toBeRemoved[1], interval[1]])
      elif toBeRemoved[0] < interval[1] < toBeRemoved[1]:
        new_intervals.append([interval[0], toBeRemoved[0]])
    return filter(lambda x: x[0] < x[1], new_intervals)

  def discussion_solution(self, intervals: List[List[int]],
                          toBeRemoved: List[int]) -> List[List[int]]:
    """
    The clean solution that runs in O(N) in time and O(1) in space

    Args:
      intervals:
      toBeRemoved:

    Returns:

    """
    # Initialize a placeholder
    new_intervals = []

    # Loop through intervals
    for low, high in intervals:

      # Unpack the toBeRemoved
      remove_low, remove_high = toBeRemoved

      # Check if interval has overlap with toBeRemoved
      if high <= remove_low or low >= remove_high:

        # Append the interval, if there is no overlap
        new_intervals.append([low, high])

      # If it DOES have overlaps
      else:

        # Check if overlap is ending side
        if low < remove_low:
          new_intervals.append([low, remove_low])

        # Or starting side
        if high > remove_high:
          new_intervals.append([remove_high, high])

    return new_intervals

  def removeInterval(self, intervals: List[List[int]],
                     toBeRemoved: List[int]) -> List[List[int]]:
    """
    Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b] represents the set of real numbers x such that a <= x < b.

    We remove the intersections between any interval in intervals and the interval toBeRemoved.

    Return a sorted list of intervals after all such removals.



    Example 1:

    Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
    Output: [[0,1],[6,7]]
    Example 2:

    Input: intervals = [[0,5]], toBeRemoved = [2,3]
    Output: [[0,2],[3,5]]


    Constraints:

    1 <= intervals.length <= 10^4
    -10^9 <= intervals[i][0] < intervals[i][1] <= 10^9

    Args:
      intervals:
      toBeRemoved:

    Returns:

    """
    return self.discussion_solution(intervals, toBeRemoved)

  """
  Binary search
  1. Find where toBeRemoved[0] falls into 
  2. Find where toBeRemoved[1] falls into
  3. 
  """