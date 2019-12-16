"""
Solution for 1060. Missing Element in Sorted Array
https://leetcode.com/problems/missing-element-in-sorted-array/
"""
from typing import List

class Solution:
  """
  Runtime: 304 ms, faster than 94.87% of Python3 online submissions for Missing Element in Sorted Array.
  Memory Usage: 19.1 MB, less than 100.00% of Python3 online submissions for Missing Element in Sorted Array.
  """
  def initial_solution(self, nums: List[int], k: int) -> int:
    """
    An initial solution that runs in O(N) where N == len(nums) in time and O(1)
    in space

    Args:
      nums:
      k:

    Returns:

    """
    for i in range(len(nums) - 1):
      n = nums[i + 1] - nums[i] - 1
      if k > n:
        k -= n
      else:
        return nums[i] + k
    return nums[-1] + k

  def bin_search(self, nums: List[int], k: int) -> int:
    """
    A binary search solution that runs in O(logN) in time and O(1) in space

    Args:
      nums:
      k:

    Returns:

    """
    missing = lambda i: nums[i] - nums[0] - i
    n = len(nums)

    if k > missing(n - 1):
      return nums[-1] + k - missing(n - 1)

    left, right = 0, n - 1
    while left != right:
      middle = (left + right) // 2
      if missing(middle) < k:
        left = middle + 1
      else:
        right = middle

    return nums[left - 1] + k - missing(left - 1)

  def missingElement(self, nums: List[int], k: int) -> int:
    """
    Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.



    Example 1:

    Input: A = [4,7,9,10], K = 1
    Output: 5
    Explanation:
    The first missing number is 5.
    Example 2:

    Input: A = [4,7,9,10], K = 3
    Output: 8
    Explanation:
    The missing numbers are [5,6,8,...], hence the third missing number is 8.
    Example 3:

    Input: A = [1,2,4], K = 3
    Output: 6
    Explanation:
    The missing numbers are [3,5,6,7,...], hence the third missing number is 6.


    Note:

    1 <= A.length <= 50000
    1 <= A[i] <= 1e7
    1 <= K <= 1e8

    Args:
      nums:
      k:

    Returns:

    """
    return self.bin_search(nums, k)