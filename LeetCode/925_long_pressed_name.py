"""
Solution for 925. Long Pressed Name
https://leetcode.com/problems/long-pressed-name/
"""

class Solution:
    """
    Runtime: 36 ms, faster than 93.50% of Python3 online submissions for Long Pressed Name.
    Memory Usage: 12.8 MB, less than 7.84% of Python3 online submissions for Long Pressed Name.
    """
    def isLongPressedName(self, name, typed):
        """
        Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the
        key might get long pressed, and the character will be typed 1 or more times.

        You examine the typed characters of the keyboard.  Return True if it is possible that it
        was your friends name, with some characters (possibly none) being long pressed.



        Example 1:

        Input: name = "alex", typed = "aaleex"
        Output: true
        Explanation: 'a' and 'e' in 'alex' were long pressed.
        Example 2:

        Input: name = "saeed", typed = "ssaaedd"
        Output: false
        Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
        Example 3:

        Input: name = "leelee", typed = "lleeelee"
        Output: true
        Example 4:

        Input: name = "laiden", typed = "laiden"
        Output: true
        Explanation: It's not necessary to long press any character.
        Args:
            name: name to find if typed is long pressed version of name
            typed: string object to find if typed is long pressed version of the name or not

        Returns:
            bool: True typed is long pressed version of name, otherwise False
        """
        # initialize i and j as zeros
        i, j = 0, 0
        n, m = len(name), len(typed)

        # loop while i and j are valid
        while i < n and j < m:

            # initialize char as name[i]
            char = name[i]

            # initialize count_i as one
            count_i = 0

            # loop while name[i] == char
            while i < n and name[i] == char:
                # increment i by one
                i += 1
                count_i += 1

            # initialize count_j as one
            count_j = 0

            # loop while name[j] == char
            while j < m and typed[j] == char:
                # increment j by one
                count_j += 1
                j += 1

            # compare two counts
            if not count_j >= count_i:
                # otherwise it's not valid, return False
                return False

        return i == n and j == m
