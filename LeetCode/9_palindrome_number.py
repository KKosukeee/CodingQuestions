"""
Solution for 9. Palindrome Number
https://leetcode.com/problems/palindrome-number/
"""

class Solution:
    """
    Runtime: 92 ms, faster than 83.29% of Python3 online submissions for Palindrome Number.
    Memory Usage: 13.2 MB, less than 5.03% of Python3 online submissions for Palindrome Number.
    """
    def isPalindrome(self, x):
        """
        Determine whether an integer is a palindrome. An integer is a palindrome when it reads the
        same backward as forward.

        Example 1:

        Input: 121
        Output: true
        Example 2:

        Input: -121
        Output: false
        Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
        Therefore it is not a palindrome.
        Example 3:

        Input: 10
        Output: false
        Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
        Args:
            x:

        Returns:

        """
        # If x < 0, then return False
        if x < 0:
            return False

        # If x < 10, then return True
        if x < 10:
            return True

        # Initialize reversed integer
        reversed_x = 0

        # Crete copy of x
        copied_x = x

        # Loop, while x > 10
        while copied_x > 0:
            # Get last digit
            last_digit = copied_x % 10

            # Divide x by 10
            copied_x = copied_x // 10

            # Add the last digit to reversed integer
            reversed_x = reversed_x * 10 + last_digit

        # If reversed integer == x, then return True
        if reversed_x == x:
            return True
        else:
            return False
