"""
Solution for 921. Minimum Add to Make Parentheses Valid
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
"""

class Solution:
    """
    Runtime: 36 ms, faster than 92.95% of Python3 online submissions for Minimum Add to Make
        Parentheses Valid.
    Memory Usage: 13.3 MB, less than 13.19% of Python3 online submissions for Minimum Add to Make
        Parentheses Valid.
    """
    def minAddToMakeValid(self, S):
        """
        Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses
        ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

        Formally, a parentheses string is valid if and only if:

        It is the empty string, or
        It can be written as AB (A concatenated with B), where A and B are valid strings, or
        It can be written as (A), where A is a valid string.
        Given a parentheses string, return the minimum number of parentheses we must add to make
        the resulting string valid.



        Example 1:

        Input: "())"
        Output: 1
        Example 2:

        Input: "((("
        Output: 3
        Example 3:

        Input: "()"
        Output: 0
        Example 4:

        Input: "()))(("
        Output: 4
        Args:
            S: str representing parentheses

        Returns:
            int: distance to make S valid
        """
        balance, result = 0, 0
        for char in S:
            if char == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    result += 1

        return result + balance
