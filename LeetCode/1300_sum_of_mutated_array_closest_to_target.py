"""
Solution for 1300. Sum of Mutated Array Closest to Target
https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/
"""
from typing import List

class Solution:
  """
  Runtime: 100 ms, faster than 32.28% of Python3 online submissions for Sum of Mutated Array Closest to Target.
  Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Sum of Mutated Array Closest to Target.
  """
  def findBestValue(self, arr: List[int], target: int) -> int:
    """
    Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

    In case of a tie, return the minimum such integer.

    Notice that the answer is not neccesarilly a number from arr.



    Example 1:

    Input: arr = [4,9,3], target = 10
    Output: 3
    Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
    Example 2:

    Input: arr = [2,3,5], target = 10
    Output: 5
    Example 3:

    Input: arr = [60864,25176,27249,21296,20204], target = 56803
    Output: 11361


    Constraints:

    1 <= arr.length <= 10^4
    1 <= arr[i], target <= 10^5

    Args:
      arr:
      target:

    Returns:

    """
    return self.bin_search(arr, target)

  def bin_search(self, arr: List[int], target: int) -> int:
    """
    A solution using a binary search that runs in O(Nlog(N)) in time and O(1)
    in space

    Args:
      arr:
      target:

    Returns:

    """
    low, high = 0, max(arr)
    diff, res = float('inf'), 1
    while low <= high:
      mid = (low + high) // 2
      smaller = list(filter(lambda x: x < mid, arr))
      s = sum(smaller) + (len(arr) - len(smaller)) * mid
      if s <= target:
        low = mid + 1
      else:
        high = mid - 1
      if abs(s - target) < diff or (abs(s - target) == diff and mid < res):
        diff = abs(s - target)
        res = mid
    return res