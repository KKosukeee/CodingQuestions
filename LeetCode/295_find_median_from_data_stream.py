"""
Solution for 295. Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/
"""
import heapq
import bisect

class MedianFinder:

  def __init__(self):
    """
    initialize your data structure here.
    """
    self.list = []
    self.low_heap, self.high_heap = [], []

  def addNum(self, num: int) -> None:
    self.heap_solution(num)

  def heap_solution(self, num):
    heapq.heappush(self.low_heap, -num)
    heapq.heappush(self.high_heap, -heapq.heappop(self.low_heap))

    if len(self.low_heap) < len(self.high_heap):
      heapq.heappush(self.low_heap, -heapq.heappop(self.high_heap))

  def bin_search(self, num):
    bisect.insort(self.list, num)

  def findMedian(self) -> float:
    return self.heap_solution_med()

  def bin_search_med(self) -> float:
    if len(self.list) % 2 == 0:
      return (self.list[len(self.list) // 2] + self.list[
        len(self.list) // 2 - 1]) / 2.
    return self.list[len(self.list) // 2]

  def heap_solution_med(self) -> float:
    if len(self.low_heap) == len(self.high_heap):
      return (-self.low_heap[0] + self.high_heap[0]) / 2.
    return -self.low_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()