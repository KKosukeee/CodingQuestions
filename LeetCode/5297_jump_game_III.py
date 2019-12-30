"""
Solution for 5297. Jump Game III
https://leetcode.com/problems/jump-game-iii/
"""
from collections import deque
from typing import List

class Solution:
  """
  Runtime: 240 ms, faster than 100.00% of Python3 online submissions for Jump Game III.
  Memory Usage: 19.1 MB, less than 100.00% of Python3 online submissions for Jump Game III.
  """
  def canReach(self, arr: List[int], start: int) -> bool:
    """
    Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

    Notice that you can not jump outside of the array at any time.



    Example 1:

    Input: arr = [4,2,3,0,3,1,2], start = 5
    Output: true
    Explanation:
    All possible ways to reach at index 3 with value 0 are:
    index 5 -> index 4 -> index 1 -> index 3
    index 5 -> index 6 -> index 4 -> index 1 -> index 3
    Example 2:

    Input: arr = [4,2,3,0,3,1,2], start = 0
    Output: true
    Explanation:
    One possible way to reach at index 3 with value 0 is:
    index 0 -> index 4 -> index 1 -> index 3
    Example 3:

    Input: arr = [3,0,2,1,2], start = 2
    Output: false
    Explanation: There is no way to reach at index 1 with value 0.


    Constraints:

    1 <= arr.length <= 5 * 10^4
    0 <= arr[i] < arr.length
    0 <= start < arr.length

    Args:
      arr:
      start:

    Returns:

    """
    return self.bfs(arr, start)

  def dfs(self, arr: List[int], start: int) -> bool:
    """
    A DFS solution that runs in O(N) in time and O(N) in space

    Args:
      arr:
      start:

    Returns:

    """
    visited = set()

    def dfs(i):
      if not i < len(arr):
        return False
      if arr[i] == 0:
        return True
      can_reach = False
      if 0 <= i + arr[i] < len(arr) and i + arr[i] not in visited:
        visited.add(i + arr[i])
        can_reach |= dfs(i + arr[i])
      if 0 <= i - arr[i] < len(arr) and i - arr[i] not in visited:
        visited.add(i - arr[i])
        can_reach |= dfs(i - arr[i])
      return can_reach

    return dfs(start)

  def bfs(self, arr: List[int], start: int) -> bool:
    """
    A BFS solution that runs in O(N) in time and O(N) in space

    Args:
      arr:
      start:

    Returns:

    """
    q, visited = deque([start]), set([start])
    while q:
      ind = q.popleft()
      if arr[ind] == 0:
        return True
      if 0 <= ind + arr[ind] < len(arr) and ind + arr[ind] not in visited:
        visited.add(ind + arr[ind])
        q.append(ind + arr[ind])
      if 0 <= ind - arr[ind] < len(arr) and ind - arr[ind] not in visited:
        visited.add(ind - arr[ind])
        q.append(ind - arr[ind])
    return False
