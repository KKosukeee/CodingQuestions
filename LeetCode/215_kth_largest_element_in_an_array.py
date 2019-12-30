"""
Solution for 215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
import random
import heapq
from typing import List

class Solution:
  """
  Runtime: 48 ms, faster than 48.58% of Python3 online submissions for Kth Largest Element
      in an Array.
  Memory Usage: 13.6 MB, less than 10.53% of Python3 online submissions for Kth Largest Element
      in an Array.
  """

  # O(k+(n-k)log(k)) time, min-heap
  def findKthLargest(self, nums, k):
    """
    Find the kth largest element in an unsorted array. Note that it is the kth largest element
    in the sorted order, not the kth distinct element.

    Example 1:

    Input: [3,2,1,5,6,4] and k = 2
    Output: 5
    Example 2:

    Input: [3,2,3,1,2,4,5,5,6] and k = 4
    Output: 4

    Args:
        nums: an unsorted array which you get kth largest number from
        k: an integer to take kth largest number from the array

    Returns:
        int: kth largest number from nums array
    """
    # Initialize heap array
    heap = []

    # Loop through nums to push into the heap
    for num in nums:
      heapq.heappush(heap, num)

    # Pop an element len(nums) - k times from the heap
    for _ in range(len(nums) - k):
      heapq.heappop(heap)

    # Return the popped value
    return heapq.heappop(heap)

  def sort(self, nums: List[int], k: int) -> int:
    """
    A sort solution that runs in O(NlogN) in time and O(1) in space

    Args:
      nums:
      k:

    Returns:

    """
    nums.sort(reverse=True)
    return nums[k - 1]

  def heap(self, nums: List[int], k: int) -> int:
    """
    A heap solution that runs in O(NlogK) in time and O(N) in space

    Args:
      nums:
      k:

    Returns:

    """
    heapq.heapify(nums)
    return heapq.nlargest(k, nums)[-1]

  def quick_select(self, nums: List[int], k: int) -> int:
    """
    A quick select solution that runs in O(NlogN) in time and O(logN) in space

    Args:
      nums:
      k:

    Returns:

    """
    def partition(left, right, index):
      pivot = nums[index]
      nums[index], nums[right] = nums[right], nums[index]
      store_index = left
      for i in range(left, right):
        if nums[i] < pivot:
          nums[store_index], nums[i] = nums[i], nums[store_index]
          store_index += 1

      nums[right], nums[store_index] = nums[store_index], nums[right]
      return store_index

    def select(left, right, k):
      if left == right:
        return nums[left]
      index = partition(left, right, random.randint(left, right))
      if k == index:
        return nums[k]
      elif k < index:
        return select(left, index - 1, k)
      else:
        return select(index + 1, right, k)

    return select(0, len(nums) - 1, len(nums) - k)
