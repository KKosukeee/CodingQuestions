"""
Solution for 1282. Group the People Given the Group Size They Belong To
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
"""
from collections import defaultdict
from typing import List

class Solution:
  """
  Runtime: 72 ms, faster than 100.00% of Python3 online submissions for Group the People Given the Group Size They Belong To.
  Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Group the People Given the Group Size They Belong To.
  """
  def initial_solution(self, groupSizes: List[int]) -> List[List[int]]:
    """
    An initial solution that runs in O(NlogN) in time and O(1) in space

    Args:
      groupSizes:

    Returns:

    """
    prev, so_far, result = 0, 0, []
    for p, size in sorted(zip(range(len(groupSizes)), groupSizes),
                          key=lambda a: a[1]):
      if prev != size or so_far >= size:
        so_far = 0
        result.append([])
      result[-1].append(p)
      prev, so_far = size, so_far + 1
    return result

  def optimal_solution(self, groupSizes: List[int]) -> List[List[int]]:
    """
     An optimal solution that runs in O(N) in time and O(N) in space

    Args:
      groupSizes:

    Returns:

    """
    buckets = defaultdict(list)
    for i, size in enumerate(groupSizes):
      buckets[size].append(i)
    result = []
    for size, bucket in buckets.items():
      if len(bucket) > size:
        placeholder = []
        while len(bucket) > size:
          placeholder.append(bucket.pop())
          if len(placeholder) == size:
            result.append(placeholder)
            placeholder = []
      result.append(bucket)
    return result

  def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
    """
    There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. Given the array groupSizes of length n telling the group size each person belongs to, return the groups there are and the people's IDs each group includes.

    You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there exists at least one solution.



    Example 1:

    Input: groupSizes = [3,3,3,3,3,1,3]
    Output: [[5],[0,1,2],[3,4,6]]
    Explanation:
    Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
    Example 2:

    Input: groupSizes = [2,1,3,3,3,2]
    Output: [[1],[0,5],[2,3,4]]


    Constraints:

    groupSizes.length == n
    1 <= n <= 500
    1 <= groupSizes[i] <= n

    Args:
      groupSizes:

    Returns:

    """
    return self.optimal_solution(groupSizes)