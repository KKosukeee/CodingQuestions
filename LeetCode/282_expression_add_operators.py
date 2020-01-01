"""
Solution for 282. Expression Add Operators
https://leetcode.com/problems/expression-add-operators/
"""
from typing import List

class Solution:
  """
  Runtime: 800 ms, faster than 68.83% of Python3 online submissions for Expression Add Operators.
  Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Expression Add Operators.
  """
  def addOperators(self, num: str, target: int) -> List[str]:
    """
    Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

    Example 1:

    Input: num = "123", target = 6
    Output: ["1+2+3", "1*2*3"]
    Example 2:

    Input: num = "232", target = 8
    Output: ["2*3+2", "2+3*2"]
    Example 3:

    Input: num = "105", target = 5
    Output: ["1*0+5","10-5"]
    Example 4:

    Input: num = "00", target = 0
    Output: ["0+0", "0-0", "0*0"]
    Example 5:

    Input: num = "3456237490", target = 9191
    Output: []

    Args:
      num:
      target:

    Returns:

    """
    return self.backtracking(num, target)

  def backtracking(self, num: str, target: int) -> List[str]:
    """
    A backtrack solution that runs in O(N*4^N) in time and O(N) in space

    Args:
      num:
      target:

    Returns:

    """
    def dfs(num, temp, curr, last, res):
      if not num:
        if curr == target:
          res.append(temp)
        return
      for i in range(1, len(num) + 1):
        val = num[:i]
        if i == 1 or (i > 1 and num[0] != '0'):
          dfs(num[i:], temp + '+' + val, curr + int(val), int(val), res)
          dfs(num[i:], temp + '-' + val, curr - int(val), -int(val), res)
          dfs(num[i:], temp + '*' + val, curr - last + last * int(val),
              last * int(val), res)

    res = []
    for i in range(1, len(num) + 1):
      if i == 1 or (i > 1 and num[0] != '0'):
        dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res)
    return res