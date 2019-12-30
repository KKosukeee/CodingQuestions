"""
Solution for 5295. Find N Unique Integers Sum up to Zero
https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
"""
from typing import List

class Solution:
  """
  Runtime: 28 ms, faster than 100.00% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
  Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
  """
  def sumZero(self, n: int) -> List[int]:
    """
    Given an integer n, return any array containing n unique integers such that they add up to 0.



    Example 1:

    Input: n = 5
    Output: [-7,-1,1,3,4]
    Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
    Example 2:

    Input: n = 3
    Output: [-1,0,1]
    Example 3:

    Input: n = 1
    Output: [0]


    Constraints:

    1 <= n <= 1000

    Args:
      n:

    Returns:

    """
    return self.initial_solution(n)

  def initial_solution(self, n: int) -> List[int]:
    """
    An initial solution that runs in O(N) in time and O(N) in space

    Args:
      n:

    Returns:

    """
    def rec(n, curr):
      if n == 0:
        return []
      if n % 2 != 0:
        return rec(n - 1, curr) + [0]
      return rec(n - 2, curr + 1) + [curr, -curr]

    return rec(n, 1)