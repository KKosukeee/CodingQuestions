"""
Solution for 28. Implement strStr()
https://leetcode.com/problems/implement-strstr/
"""

class Solution:
    """
    Runtime: 40 ms, faster than 54.47% of Python3 online submissions for Implement strStr().
    Memory Usage: 13.2 MB, less than 5.13% of Python3 online submissions for Implement strStr().
    """
    def strStr(self, haystack, needle):
        """
        Implement strStr().

        Return the index of the first occurrence of needle in haystack, or -1 if needle is not
        part of haystack.

        Example 1:

        Input: haystack = "hello", needle = "ll"
        Output: 2
        Example 2:

        Input: haystack = "aaaaa", needle = "bba"
        Output: -1
        Args:
            haystack: str object to look for needle
            needle: str to find in haystack

        Returns:
            int: index value for a needle in haystack string
        """
        if not needle:
            return 0

        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            if needle == haystack[i:i + len(needle)]:
                return i
        return -1
