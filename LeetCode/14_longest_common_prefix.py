"""
Solution for 14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/
"""

class Solution:
    """
    Runtime: 36 ms, faster than 98.11% of Python3 online submissions for Longest Common Prefix.
    Memory Usage: 13.4 MB, less than 5.10% of Python3 online submissions for Longest Common Prefix.
    """
    def longestCommonPrefix(self, strs):
        """
        Write a function to find the longest common prefix string amongst an array of strings.

        If there is no common prefix, return an empty string "".

        Example 1:

        Input: ["flower","flow","flight"]
        Output: "fl"
        Example 2:

        Input: ["dog","racecar","car"]
        Output: ""
        Explanation: There is no common prefix among the input strings.
        Args:
            strs: string to find the longest common prefix

        Returns:
            str: substring from strs
        """
        if len(strs) == 0:
            return ""

        min_str = min(strs)
        max_str = max(strs)

        for i in range(len(min_str)):
            if min_str[i] != max_str[i]:
                return min_str[:i]

        return min_str
