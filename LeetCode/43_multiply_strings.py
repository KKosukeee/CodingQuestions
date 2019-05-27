"""
Solution for 43. Multiply Strings
https://leetcode.com/problems/multiply-strings/
"""

class Solution:
    """
    Runtime: 40 ms, faster than 92.53% of Python3 online submissions for Multiply Strings.
    Memory Usage: 13.2 MB, less than 51.11% of Python3 online submissions for Multiply Strings.
    """
    def multiply(self, num1, num2):
        """
        Given two non-negative integers num1 and num2 represented as strings, return the product
        of num1 and num2, also represented as a string.

        Example 1:

        Input: num1 = "2", num2 = "3"
        Output: "6"
        Example 2:

        Input: num1 = "123", num2 = "456"
        Output: "56088"
        Args:
            num1: string of digits to multiply with
            num2: string of digits to multiply with

        Returns:
            str: representing num1 * num2
        """
        # Construct upper part
        if len(num2) > len(num1):
            num1, num2 = num2, num1

        longer_digit = 0

        for i in range(len(num1) - 1):
            longer_digit += ord(num1[i]) - ord('1') + 1
            longer_digit *= 10

        longer_digit += ord(num1[-1]) - ord('1') + 1
        result_string = 0

        # Multiply for each digit in lower part
        for i in range(len(num2) - 1):
            result_string += longer_digit * (ord(num2[i]) - ord('1') + 1)
            result_string *= 10

        result_string += longer_digit * (ord(num2[-1]) - ord('1') + 1)
        return str(result_string)
