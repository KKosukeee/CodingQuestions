"""
Solution for 20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
"""

class Solution:
    """
    Runtime: 36 ms, faster than 88.33% of Python3 online submissions for Valid Parentheses.
    Memory Usage: 13.3 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.
    """
    def isValid(self, s):
        """
        Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine
        if the input string is valid.

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Note that an empty string is also considered valid.

        Example 1:

        Input: "()"
        Output: true
        Example 2:

        Input: "()[]{}"
        Output: true
        Example 3:

        Input: "(]"
        Output: false
        Example 4:

        Input: "([)]"
        Output: false
        Example 5:

        Input: "{[]}"
        Output: true
        Args:
            s: string of parentheses

        Returns:
            bool if the parentheses in the s is valid or not
        """
        # 1
        if not s:
            return True

        # 2
        if not len(s) % 2 == 0:
            return False

        comp = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []

        for char in s:
            # 3
            if char in comp:
                popped = stack.pop() if stack else '@'
                if popped != comp[char]:
                    return False
            # 2
            else:
                stack.append(char)

        return not stack
