"""
Solution for 88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/
"""
from typing import List

class Solution:
  """
  Runtime: 32 ms, faster than 92.82% of Python3 online submissions for Merge Sorted Array.
  Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Merge Sorted Array.
  """
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

    Note:

    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
    Example:

    Input:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3

    Output: [1,2,2,3,5,6]

    Do not return anything, modify nums1 in-place instead.
    """
    self.two_pointer_optimal(nums1, m, nums2, n)

  def naive_solution(self, nums1: List[int], m: int, nums2: List[int],
                     n: int) -> None:
    """
    A naive solution that runs in O((N+M)log(N+M)) in time and O(1) in space

    Args:
      nums1:
      m:
      nums2:
      n:

    Returns:

    """
    nums1[m:] = nums2
    nums1.sort()

  def two_pointer_sub_optimal(self, nums1: List[int], m: int, nums2: List[int],
                              n: int) -> None:
    """
    A solution using two pointers that runs in O(M+N) in time and O(M) in memory

    Args:
      nums1:
      m:
      nums2:
      n:

    Returns:

    """
    copied = nums1[:m]
    i, j, k = 0, 0, 0
    while i < len(copied) and j < len(nums2):
      if copied[i] <= nums2[j]:
        nums1[k] = copied[i]
        i += 1
      else:
        nums1[k] = nums2[j]
        j += 1
      k += 1

    if i < len(copied):
      while i < len(copied):
        nums1[k] = copied[i]
        i, k = i + 1, k + 1
    if j < len(nums2):
      while j < len(nums2):
        nums1[k] = nums2[j]
        j, k = j + 1, k + 1

  def two_pointer_optimal(self, nums1: List[int], m: int, nums2: List[int],
                          n: int) -> None:
    """
    A two pointers solution that runs in O(M+N) in time and O(1) in space

    Args:
      nums1:
      m:
      nums2:
      n:

    Returns:

    """
    i, j, k = m - 1, n - 1, len(nums1) - 1
    while i >= 0 and j >= 0:
      if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
      else:
        nums1[k] = nums2[j]
        j -= 1
      k -= 1
    if i >= 0:
      while i >= 0:
        nums1[k] = nums1[i]
        i, k = i - 1, k - 1
    if j >= 0:
      while j >= 0:
        nums1[k] = nums2[j]
        j, k = j - 1, k - 1

