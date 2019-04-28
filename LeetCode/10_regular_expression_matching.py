"""
Solution for 10. Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/
"""

class Solution:
    """
    Runtime: 1572 ms, faster than 14.97% of Python3 online submissions for Regular Expression
        Matching.
    Memory Usage: 13.2 MB, less than 5.32% of Python3 online submissions for Regular Expression
        Matching.
    """
    def isMatch(self, text, pattern):
        """
        Given an input string (s) and a pattern (p), implement regular expression matching with
        support for '.' and '*'.

        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.
        The matching should cover the entire input string (not partial).

        Note:

        s could be empty and contains only lowercase letters a-z.
        p could be empty and contains only lowercase letters a-z, and characters like . or *.
        Example 1:

        Input:
        s = "aa"
        p = "a"
        Output: false
        Explanation: "a" does not match the entire string "aa".
        Example 2:

        Input:
        s = "aa"
        p = "a*"
        Output: true
        Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating
        'a' once, it becomes "aa".
        Example 3:

        Input:
        s = "ab"
        p = ".*"
        Output: true
        Explanation: ".*" means "zero or more (*) of any character (.)".
        Example 4:

        Input:
        s = "aab"
        p = "c*a*b"
        Output: true
        Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches
        "aab".
        Example 5:

        Input:
        s = "mississippi"
        p = "mis*is*p*."
        Output: false
        Args:
            text:
            pattern:

        Returns:

        """
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])
