"""
Solution for 1287. Element Appearing More Than 25% In Sorted Array
https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
"""
from collections import Counter
import bisect
from typing import List

class Solution:
  """
  Runtime: 84 ms, faster than 98.28% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
  Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
  """
  def findSpecialInteger(self, arr: List[int]) -> int:
    """
    Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

    Return that integer.



    Example 1:

    Input: arr = [1,2,2,6,6,6,6,7,10]
    Output: 6


    Constraints:

    1 <= arr.length <= 10^4
    0 <= arr[i] <= 10^5

    Args:
      arr:

    Returns:

    """
    return self.bin_search(arr)

  def counter(self, arr: List[int]) -> int:
    """
    A solution using counter that runs in O(N) in time and O(N) in space

    Args:
      arr:

    Returns:

    """
    counter = Counter(arr)
    max_freq = max(counter.values())
    for k, v in counter.items():
      if max_freq == v:
        return k

  def bin_search(self, arr: List[int]) -> int:
    """
    A solution using binary search that runs in O(log(N)) in time and O(1) in
    space

    Args:
      arr:

    Returns:

    """
    span = len(arr) // 4
    if span == 0:
      return arr[0]
    for i in range(span, len(arr), span):
      if bisect.bisect_right(arr, arr[i]) - bisect.bisect_left(arr,
                                                               arr[i]) > span:
        return arr[i]
    return arr[-1]