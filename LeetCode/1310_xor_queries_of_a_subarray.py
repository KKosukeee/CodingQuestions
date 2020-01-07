"""
Solution for 1310. XOR Queries of a Subarray
https://leetcode.com/problems/xor-queries-of-a-subarray/
"""
from functools import reduce
from typing import List

class Solution:
  """
  Runtime: 400 ms, faster than 96.30% of Python3 online submissions for XOR Queries of a Subarray.
  Memory Usage: 27.2 MB, less than 100.00% of Python3 online submissions for XOR Queries of a Subarray.
  """
  def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    """
    Given the array arr of positive integers and the array queries where queries[i] = [Li, Ri], for each query i compute the XOR of elements from Li to Ri (that is, arr[Li] xor arr[Li+1] xor ... xor arr[Ri] ). Return an array containing the result for the given queries.


    Example 1:

    Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
    Output: [2,7,14,8]
    Explanation:
    The binary representation of the elements in the array are:
    1 = 0001
    3 = 0011
    4 = 0100
    8 = 1000
    The XOR values for queries are:
    [0,1] = 1 xor 3 = 2
    [1,2] = 3 xor 4 = 7
    [0,3] = 1 xor 3 xor 4 xor 8 = 14
    [3,3] = 8
    Example 2:

    Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
    Output: [8,0,4,4]


    Constraints:

    1 <= arr.length <= 3 * 10^4
    1 <= arr[i] <= 10^9
    1 <= queries.length <= 3 * 10^4
    queries[i].length == 2
    0 <= queries[i][0] <= queries[i][1] < arr.length

    Args:
      arr:
      queries:

    Returns:

    """
    return self.optimal(arr, queries)

  def brute_force(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    """
    A brute force solution that runs in O(len(quries)*len(arr)) in time and O(1)
    in space

    Args:
      arr:
      queries:

    Returns:

    """
    res = []
    for l, r in queries:
      res.append(reduce(lambda a, b: a ^ b, arr[l:r + 1]))
    return res

  def optimal(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    """
    An optimal solution that runs in O(len(arr)+len(queries)) in time and
    O(len(arr)) in space

    Args:
      arr:
      queries:

    Returns:

    """
    prefix = [0]
    for val in arr:
      prefix.append(prefix[-1] ^ val)
    res = []
    for l, r in queries:
      res.append(prefix[l] ^ prefix[r + 1])
    return res