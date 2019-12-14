"""
Solution for 636. Exclusive Time of Functions
https://leetcode.com/problems/exclusive-time-of-functions/
"""
from typing import List

class Solution:
  """
  Runtime: 68 ms, faster than 97.28% of Python3 online submissions for Exclusive Time of Functions.
  Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Exclusive Time of Functions.
  """
  def stack_solution(self, n: int, logs: List[str]) -> List[int]:
    stack, res, prev = [], [0] * n, 0
    for log in logs:
      fid, status, time = log.split(':')
      fid, time = int(fid), int(time)
      if status == 'start':
        if stack:
          res[stack[-1]] += time - prev
        stack.append(fid)
        prev = time
      else:
        res[stack.pop()] += time - prev + 1
        prev = time + 1
    return res

  def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
    return self.stack_solution(n, logs)


class Solution:
  def stack_solution(self, n: int, logs: List[str]) -> List[int]:
    stack, res, prev = [], [0] * n, 0
    for log in logs:
      fid, status, time = log.split(':')
      fid, time = int(fid), int(time)
      if status == 'start':
        if stack:
          res[stack[-1]] += time - prev
        stack.append(fid)
        prev = time
      else:
        res[stack.pop()] += time - prev + 1
        prev = time + 1
    return res

  def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
    return self.stack_solution(n, logs)
