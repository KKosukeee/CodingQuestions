"""
Solution for 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/
"""
from typing import List

class Solution:
  def initial_solution(self, mat: List[List[int]], threshold: int) -> int:
    """
    An initial solution that runs out in TLE. This runs in O(MNK) in time and
    O(MN) in space

    Args:
      mat:
      threshold:

    Returns:

    """
    dp = [[0 for _ in range(len(mat[0]) + 1)] for _ in range(len(mat) + 1)]
    for i in range(1, len(mat) + 1):
      col_sum = 0
      for j in range(1, len(mat[0]) + 1):
        col_sum += mat[i - 1][j - 1]
        dp[i][j] = dp[i - 1][j] + col_sum

    for k in reversed(range(min(len(mat), len(mat[0])))):
      for i in range(1, len(mat) - k + 1):
        for j in range(1, len(mat[0]) - k + 1):
          if dp[i + k][j + k] - dp[i + k][j - 1] - dp[i - 1][j + k] + dp[i - 1][
            j - 1] <= threshold:
            return k + 1
    return 0

  def optimal_solution(self, mat: List[List[int]], threshold: int) -> int:
    """
    An optimal solution that runs in O(MNlog(min(M,N))) in time and O(MN) in
    space

    Args:
      mat:
      threshold:

    Returns:

    """
    if not mat:
      return 0

    dp = [[0] * (len(mat[0]) + 1) for _ in range(len(mat) + 1)]
    max_side = 0

    for i in range(1, len(mat) + 1):
      for j in range(1, len(mat[0]) + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][
          j - 1]
        l, r = 1, min(i, j)
        while l <= r:
          k = (l + r) // 2
          curr_sum = dp[i][j] - dp[i - k][j] - dp[i][j - k] + dp[i - k][j - k]
          if curr_sum <= threshold:
            max_side = max(max_side, k)
            l = k + 1
          else:
            r = k - 1
    return max_side

  def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
    """
    Given a m x n matrix mat and an integer threshold. Return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.



    Example 1:


    Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
    Output: 2
    Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
    Example 2:

    Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
    Output: 0
    Example 3:

    Input: mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
    Output: 3
    Example 4:

    Input: mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
    Output: 2


    Constraints:

    1 <= m, n <= 300
    m == mat.length
    n == mat[i].length
    0 <= mat[i][j] <= 10000
    0 <= threshold <= 10^5

    Args:
      mat:
      threshold:

    Returns:

    """
    return self.initial_solution(mat, threshold)
