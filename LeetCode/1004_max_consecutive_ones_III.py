"""
Solution for 1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/
"""
from typing import List

class Solution:
  """
  Runtime: 608 ms, faster than 94.09% of Python3 online submissions for Max Consecutive Ones III.
  Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Max Consecutive Ones III.
  """
  def longestOnes(self, A: List[int], K: int) -> int:
    """
    Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

    Return the length of the longest (contiguous) subarray that contains only 1s.



    Example 1:

    Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
    Output: 6
    Explanation:
    [1,1,1,0,0,1,1,1,1,1,1]
    Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
    Example 2:

    Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
    Output: 10
    Explanation:
    [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.


    Note:

    1 <= A.length <= 20000
    0 <= K <= A.length
    A[i] is 0 or 1

    Args:
      A:
      K:

    Returns:

    """
    return self.efficient_sliding_window(A, K)

  def sliding_window(self, A: List[int], K: int) -> int:
    """
    A sliding window approach that runs in O(N) in time and O(1) in space

    Args:
      A:
      K:

    Returns:

    """
    i, j, k = 0, 0, 0
    res = 0

    while j < len(A):
      while j < len(A) and k <= K:
        if A[j] == 0:
          k += 1
        res = max(res, j - i)
        j += 1
      while i < j and k > K:
        if A[i] == 0:
          k -= 1
        i += 1
    if k <= K:
      return max(res, j - i)
    return res

  def efficient_sliding_window(self, A: List[int], K: int) -> int:
    """
    An efficient sliding window approach that runs in O(N) in time and O(1) in
    space

    Args:
      A:
      K:

    Returns:

    """
    left = 0
    for right in range(len(A)):
      K -= 1 - A[right]
      if K < 0:
        K += 1 - A[left]
        left += 1
    return right - left + 1