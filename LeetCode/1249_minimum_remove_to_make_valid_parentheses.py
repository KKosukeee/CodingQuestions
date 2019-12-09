"""
Solution for 1249. Minimum Remove to Make Valid Parentheses
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
"""

class Solution:
  """
  Runtime: 136 ms, faster than 57.24% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
  Memory Usage: 14.9 MB, less than 100.00% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
  """
  def three_pass(self, s: str) -> str:
    """
    An initial solution that runs in  O(N) in time and O(N) in space

    Args:
      s:

    Returns:

    """
    stack, invalid = [], set()
    for i, char in enumerate(s):
      if char == '(':
        stack.append(i)
      elif char == ')':
        if stack:
          _ = stack.pop()
        else:
          invalid.add(i)
    if stack:
      while stack:
        invalid.add(stack.pop())

    result = []
    for i, char in enumerate(s):
      if i not in invalid:
        result.append(char)
    return ''.join(result)

  def two_pass(self, s: str) -> str:
    """
    A second solution that runs in same time and space complexity as the first
    solution

    Args:
      s:

    Returns:

    """
    def remove(s, o, c):
      balance, chars = 0, []
      for char in s:
        if char == o:
          balance += 1
        elif char == c:
          if balance == 0:
            continue
          balance -= 1
        chars.append(char)
      return ''.join(chars)

    s = remove(s, '(', ')')
    s = remove(s[::-1], ')', '(')
    return s[::-1]

  def minRemoveToMakeValid(self, s: str) -> str:
    return self.two_pass(s)
