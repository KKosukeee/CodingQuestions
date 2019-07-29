"""
Solution for 227. Basic Calculator II
https://leetcode.com/problems/basic-calculator-ii/
"""

class Solution:
    """
    Runtime: 148 ms, faster than 25.47% of Python3 online submissions for Basic Calculator II.
    Memory Usage: 15.5 MB, less than 18.91% of Python3 online submissions for Basic Calculator II.
    """
    def calculate(self, s):
        """
        Implement a basic calculator to evaluate a simple expression string.

        The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

        Example 1:

        Input: "3+2*2"
        Output: 7
        Example 2:

        Input: " 3/2 "
        Output: 1
        Example 3:

        Input: " 3+5 / 2 "
        Output: 5
        Note:

        You may assume that the given expression is always valid.
        Do not use the eval built-in library function.
        Args:
            s: str representing a equation

        Returns:
            int: after the input is evaluated
        """
        stack = []
        last_sign = ''
        ops = {'+', '-', '*', '/'}
        i = 0

        while i < len(s):
            if s[i] in ops:
                last_sign = s[i]

            if s[i] == '*' or s[i] == '/':
                popped = stack.pop()
                op = s[i]
                while i < len(s) and not s[i].isdigit():
                    i += 1
                char_int = ''
                while i < len(s) and s[i].isdigit():
                    char_int += s[i]
                    i += 1
                stack.append(self.op(popped, int(char_int), op))
                continue
            elif s[i].isdigit():
                char_int = ''
                while i < len(s) and s[i].isdigit():
                    char_int += s[i]
                    i += 1

                if last_sign != '-':
                    stack.append(int(char_int))
                else:
                    stack.append(-int(char_int))
                continue
            i += 1

        return sum(stack)

    def op(self, a, b, o):
        """
        This method does the calculation
        Args:
            a: int value
            b: int value
            o: str value

        Returns:
            int: after the evaluation
        """
        if o == '+':
            return int(a + b)
        elif o == '-':
            return int(a - b)
        elif o == '*':
            return int(a * b)
        else:
            return int(a / b)
