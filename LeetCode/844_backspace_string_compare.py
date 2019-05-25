"""
Solution for 844. Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/
"""
from itertools import zip_longest

class Solution:
    """
    Runtime: 24 ms, faster than 99.92% of Python3 online submissions for Backspace String Compare.
    Memory Usage: 13.3 MB, less than 9.92% of Python3 online submissions for Backspace String
        Compare.
    """
    def backspaceCompare(self, S, T):
        """
        Given two strings S and T, return if they are equal when both are typed into empty text
        editors. # means a backspace character.

        Example 1:

        Input: S = "ab#c", T = "ad#c"
        Output: true
        Explanation: Both S and T become "ac".
        Example 2:

        Input: S = "ab##", T = "c#d#"
        Output: true
        Explanation: Both S and T become "".
        Example 3:

        Input: S = "a##c", T = "#a#c"
        Output: true
        Explanation: Both S and T become "c".
        Example 4:

        Input: S = "a#c", T = "b"
        Output: false
        Explanation: S becomes "c" while T becomes "b".
        Args:
            S: The first string to compare
            T: The second string to compare

        Returns:
            bool: If both strings are the same, False otherwise
        """
        for s, t in zip_longest(self.get_next(S), self.get_next(T)):
            if s != t:
                return False

        return True

    def get_next(self, s):
        """
        This yield next char that should be compared by the definition
        Args:
            s: whole string to compare with

        Returns:
            str: a valid char from s with the definition
        """
        hash_count = 0
        for c in reversed(s):
            if c == '#':
                hash_count += 1
            else:
                if hash_count > 0:
                    hash_count -= 1
                else:
                    yield c
