"""
Solution for 7. Reverse Integer
https://leetcode.com/problems/reverse-integer/
"""

class Solution:
    """
    Runtime: 40 ms, faster than 99.91% of Python3 online submissions for Reverse Integer.
    Memory Usage: 13.2 MB, less than 5.71% of Python3 online submissions for Reverse Integer.
    """
    def reverse(self, x):
        """
        Given a 32-bit signed integer, reverse digits of an integer.

        Example 1:

        Input: 123
        Output: 321
        Example 2:

        Input: -123
        Output: -321
        Example 3:

        Input: 120
        Output: 21
        Args:
            x: integer to reverse the order from

        Returns:
            int: reversed integer
        """
        # Initialize reversed with zero
        rev = 0

        if x < 0:
            factor = -1
        else:
            factor = 1

        x *= factor

        # Loop, while x is not 0
        while x != 0:

            # Get last digit
            pop = x % 10

            # Remove last digit from x
            x = x // 10

            # Check if added value is not going to overflow
            if rev > 2 ** 31 / 10 or (rev == 2 ** 31 / 10 and pop > 7):
                return 0

            if rev < -2 ** 31 / 10 or (rev == -2 ** 31 / 10 and pop < -8):
                return 0

            # Add last digit to reversed
            rev = rev * 10 + pop

        return factor * rev
