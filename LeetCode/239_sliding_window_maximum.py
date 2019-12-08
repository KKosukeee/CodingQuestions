"""
Solution for 239. Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/
"""
from collections import deque
from typing import List

class Solution:
  """
  Runtime: 156 ms, faster than 96.06% of Python3 online submissions for Sliding Window Maximum.
  Memory Usage: 19.5 MB, less than 88.46% of Python3 online submissions for Sliding Window Maximum.
  """
  def initial_solution(self, nums: List[int], k: int) -> List[int]:
    """
    An initial solution that runs in O(NK) in time and O(1) in space

    Args:
      nums:
      k:

    Returns:

    """
    if not nums:
      return []
    result = []
    for i in range(len(nums) - (k - 1)):
      result.append(max(nums[i:i + k]))
    return result

  def linear_solution(self, nums: List[int], k: int) -> List[int]:
    """
    A linear solution that uses deque and runs in O(N) in time and O(K) in space

    Args:
      nums:
      k:

    Returns:

    """
    if not nums:
      return []

    def clean_deque(i):
      # the first elements gets out of the sliding window
      if deq and deq[0] == i - k:
        _ = deq.popleft()
      # Remove any elements that are smaller than the current one
      while deq and nums[i] > nums[deq[-1]]:
        _ = deq.pop()

    deq = deque()
    max_idx = 0

    # Initialize the deq with the first window
    for i in range(k):
      clean_deque(i)
      deq.append(i)
      if nums[i] > nums[max_idx]:
        max_idx = i
    output = [nums[max_idx]]

    # Create the rest of the sliding windows
    for i in range(k, len(nums)):
      clean_deque(i)
      deq.append(i)
      output.append(nums[deq[0]])
    return output

  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    """
    Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

    Example:

    Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
    Output: [3,3,5,5,6,7]
    Explanation:

    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7
    Note:
    You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

    Follow up:
    Could you solve it in linear time?

    Args:
      nums:
      k:

    Returns:

    """
    return self.linear_solution(nums, k)
