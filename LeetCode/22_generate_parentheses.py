"""
Solution for 22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/
"""

class Solution(object):
    """
    Runtime: 44 ms, faster than 60.80% of Python3 online submissions for Generate Parentheses.
    Memory Usage: 13.5 MB, less than 5.10% of Python3 online submissions for Generate Parentheses.
    """
    def generateParenthesis(self, N):
        """
        Given n pairs of parentheses, write a function to generate all combinations of well-formed
        parentheses.

        For example, given n = 3, a solution set is:

        [
          "((()))",
          "(()())",
          "(())()",
          "()(())",
          "()()()"
        ]
        Args:
            N: integer to generate parentheses of

        Returns:
            list<str>: list of string with valid parentheses
        """
        ans = []

        def backtrack(S='', left=0, right=0):
            """
            backtrack function
            Args:
                S: string to construct parentheses with
                left: counter for opening parentheses
                right: counter for closing parentheses

            Returns:

            """
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)

        backtrack()
        return ans
