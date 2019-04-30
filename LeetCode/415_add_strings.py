"""
Solution for 415. Add Strings
https://leetcode.com/problems/add-strings/
"""

class Solution:
    """
    Runtime: 52 ms, faster than 79.99% of Python3 online submissions for Add Strings.
    Memory Usage: 13.1 MB, less than 5.83% of Python3 online submissions for Add Strings.
    """
    def addStrings(self, num1, num2):
        """
        Given two non-negative integers num1 and num2 represented as string, return the sum of
        num1 and num2.

        Note:

        The length of both num1 and num2 is < 5100.
        Both num1 and num2 contains only digits 0-9.
        Both num1 and num2 does not contain any leading zero.
        You must not use any built-in BigInteger library or convert the inputs to integer directly.
        Args:
            num1: string representing integer
            num2: string representing integer

        Returns:
            str: sum of num1 and num2 representing in string
        """
        i = len(num1) - 1
        j = len(num2) - 1
        answer = ''
        carry = 0

        while i >= 0 or j >= 0:
            if i >= 0:
                val1 = int(num1[i])
            else:
                val1 = 0

            if j >= 0:
                val2 = int(num2[j])
            else:
                val2 = 0

            added = val1 + val2 + carry
            if added >= 10:
                added %= 10
                carry = 1
            else:
                carry = 0

            answer = str(added) + answer
            i -= 1
            j -= 1

        if carry == 1:
            answer = '1' + answer

        return answer
