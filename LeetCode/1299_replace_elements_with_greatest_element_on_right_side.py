"""
Solution for 1299. Replace Elements with Greatest Element on Right Side
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
"""
from collections import deque
from typing import List

class Solution:
  """
  Runtime: 80 ms, faster than 75.23% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
  Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
  """
  def replaceElements(self, arr: List[int]) -> List[int]:
    """
    Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

    After doing so, return the array.



    Example 1:

    Input: arr = [17,18,5,4,6,1]
    Output: [18,6,6,6,1,-1]


    Constraints:

    1 <= arr.length <= 10^4
    1 <= arr[i] <= 10^5

    Args:
      arr:

    Returns:

    """
    return self.queue(arr)

  def stack(self, arr: List[int]) -> List[int]:
    """
    A solution using a stack that runs in O(N) in time and O(N) in space

    Args:
      arr:

    Returns:

    """
    m, res = arr[-1], [-1]
    for i in reversed(range(len(arr) - 1)):
      res.append(m)
      m = max(m, arr[i])
    return res[::-1]

  def queue(self, arr: List[int]) -> List[int]:
    """
    A solution using a queue that runs in O(N) in time and space

    Args:
      arr:

    Returns:

    """
    m, res = arr[-1], deque([-1])
    for i in reversed(range(len(arr) - 1)):
      res.appendleft(m)
      m = max(m, arr[i])
    return list(res)

  def in_place(self, arr: List[int]) -> List[int]:
    """
    A solution that doesn't use any additional space that runs same as queue or
    stack solution

    Args:
      arr:

    Returns:

    """
    m = -1
    for i in reversed(range(len(arr))):
      m, arr[i] = max(m, arr[i]), m
    return arr
