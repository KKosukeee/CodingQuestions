"""
Solution for 1288. Remove Covered Intervals
https://leetcode.com/problems/remove-covered-intervals/
"""
from typing import List

class Solution:
  """
  Runtime: 96 ms, faster than 80.41% of Python3 online submissions for Remove Covered Intervals.
  Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Remove Covered Intervals.
  """
  def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
    """
    Given a list of intervals, remove all intervals that are covered by another interval in the list. Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

    After doing so, return the number of remaining intervals.



    Example 1:

    Input: intervals = [[1,4],[3,6],[2,8]]
    Output: 2
    Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.


    Constraints:

    1 <= intervals.length <= 1000
    0 <= intervals[i][0] < intervals[i][1] <= 10^5
    intervals[i] != intervals[j] for all i != j

    Args:
      intervals:

    Returns:

    """
    return self.sort(intervals)

  def sort(self, intervals: List[List[int]]) -> int:
    """
    A solution using sorting that runs in O(Nlog(N)) in time and O(1) in space

    Args:
      intervals:

    Returns:

    """
    intervals.sort(key=lambda x: (x[0], -x[1]))
    res, right = 0, 0
    for i, j in intervals:
      res += j > right
      right = max(right, j)
    return res