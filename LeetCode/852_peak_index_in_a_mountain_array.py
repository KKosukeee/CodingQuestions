"""
Solution for 852. Peak Index in a Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/
"""
from typing import List

class Solution:
  """
  Runtime: 76 ms, faster than 98.05% of Python3 online submissions for Peak Index in a Mountain Array.
  Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Peak Index in a Mountain Array.
  """
  def peakIndexInMountainArray(self, A: List[int]) -> int:
    """
    Let's call an array A a mountain if the following properties hold:

    A.length >= 3
    There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
    Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

    Example 1:

    Input: [0,1,0]
    Output: 1
    Example 2:

    Input: [0,2,1,0]
    Output: 1
    Note:

    3 <= A.length <= 10000
    0 <= A[i] <= 10^6
    A is a mountain, as defined above.

    Args:
      A:

    Returns:

    """
    for i in range(1, len(A) - 1):
      if A[i - 1] < A[i] > A[i + 1]:
        return i

  """
  Simple solution
  1. Loop through the 1...len(A)-1
    1.1 Check if i is an edge or not
    1.2 If so, return the i
  """