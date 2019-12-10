"""
Solution for 621. Task Scheduler
https://leetcode.com/problems/task-scheduler/
"""
import heapq
from collections import Counter
from typing import List

class Solution:
  """
  Runtime: 680 ms, faster than 27.95% of Python3 online submissions for Task Scheduler.
  Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Task Scheduler.
  """
  def leastInterval(self, tasks: List[str], n: int) -> int:
    """
    Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

    However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

    You need to return the least number of intervals the CPU will take to finish all the given tasks.



    Example:

    Input: tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8
    Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.


    Note:

    The number of tasks is in the range [1, 10000].
    The integer n is in the range [0, 100].

    Args:
      tasks:
      n:

    Returns:

    """
    counter = Counter(tasks)
    pq = [(-v, k) for k, v in counter.items()]
    heapq.heapify(pq)
    curr_time = 0

    while pq:
      i, temp = 0, []
      while i <= n:
        curr_time += 1
        if pq:
          v, k = heapq.heappop(pq)
          if v != -1:
            temp.append((v + 1, k))
        if not pq and not temp:
          break
        else:
          i += 1
      for item in temp:
        heapq.heappush(pq, item)
    return curr_time