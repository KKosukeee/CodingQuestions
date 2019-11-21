"""
Solution for 582. Kill Process
https://leetcode.com/problems/kill-process/
"""
from collections import defaultdict
from collections import deque
from typing import List

class Solution:
  """
  Runtime: 464 ms, faster than 97.55% of Python3 online submissions for Kill Process.
  Memory Usage: 22.6 MB, less than 100.00% of Python3 online submissions for Kill Process.
  """
  def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[
    int]:
    """
    Given n processes, each process has a unique PID (process id) and its PPID (parent process id).

    Each process only has one parent process, but may have one or more children processes. This is just like a tree structure. Only one process has PPID that is 0, which means this process has no parent process. All the PIDs will be distinct positive integers.

    We use two list of integers to represent a list of processes, where the first list contains PID for each process and the second list contains the corresponding PPID.

    Now given the two lists, and a PID representing a process you want to kill, return a list of PIDs of processes that will be killed in the end. You should assume that when a process is killed, all its children processes will be killed. No order is required for the final answer.

    Example 1:
    Input:
    pid =  [1, 3, 10, 5]
    ppid = [3, 0, 5, 3]
    kill = 5
    Output: [5,10]
    Explanation:
               3
             /   \
            1     5
                 /
                10
    Kill 5 will also kill 10.
    Note:
    The given kill id is guaranteed to be one of the given PIDs.
    n >= 1.

    Args:
      pid:
      ppid:
      kill:

    Returns:

    """
    graph = defaultdict(list)
    for i, parent in enumerate(ppid):
      graph[parent].append(pid[i])
    queue = deque([kill])
    killed = []
    while queue:
      node = queue.popleft()
      killed.append(node)
      queue.extend(graph[node])
    return killed

  """
  {
    3: [1, 5],
    0: [3],
    5: [10],
  }
  [5]

  Graph solution
  T: O(N), S: O(N)
  1. Build a graph -> O(N)
  2. Starting from the killing node, traverse the graph -> O(N)
  3. Append all nodes starting from the killing node, -> O(N)
  4. Return all nodes in the list -> O(1)

  Algorithm
  1. Find the 
  """