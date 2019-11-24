"""
Solution for 1269. Number of Ways to Stay in the Same Place After Some Steps
https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
"""
from functools import lru_cache

class Solution:
  """
  Runtime: 256 ms, faster than 33.33% of Python3 online submissions for Number of Ways to Stay in the Same Place After Some Steps.
  Memory Usage: 68.3 MB, less than 100.00% of Python3 online submissions for Number of Ways to Stay in the Same Place After Some Steps.
  """
  def numWays(self, steps: int, arrLen: int) -> int:
    """
    You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array or stay in the same place  (The pointer should not be placed outside the array at any time).

    Given two integers steps and arrLen, return the number of ways such that your pointer still at index 0 after exactly steps steps.

    Since the answer may be too large, return it modulo 10^9 + 7.



    Example 1:

    Input: steps = 3, arrLen = 2
    Output: 4
    Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
    Right, Left, Stay
    Stay, Right, Left
    Right, Stay, Left
    Stay, Stay, Stay
    Example 2:

    Input: steps = 2, arrLen = 4
    Output: 2
    Explanation: There are 2 differents ways to stay at index 0 after 2 steps
    Right, Left
    Stay, Stay
    Example 3:

    Input: steps = 4, arrLen = 2
    Output: 8


    Constraints:

    1 <= steps <= 500
    1 <= arrLen <= 10^6

    Args:
      steps:
      arrLen:

    Returns:

    """
    @lru_cache(maxsize=None)
    def backtrack(curr, steps_left):
      if not curr >= 0 or not curr < arrLen:
        return 0
      if steps_left == curr:
        return 1
      if steps_left < curr:
        return 0
      return backtrack(curr - 1, steps_left - 1) + backtrack(curr + 1,
                                                             steps_left - 1) + backtrack(
        curr, steps_left - 1)

    return backtrack(0, steps) % (10 ** 9 + 7)

  """
  Backtracking

  """