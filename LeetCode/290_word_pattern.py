"""
Solution for 290. Word Pattern
https://leetcode.com/problems/word-pattern/
"""

class Solution:
    """
    Runtime: 36 ms, faster than 61.84% of Python3 online submissions for Word Pattern.
    Memory Usage: 13.6 MB, less than 5.13% of Python3 online submissions for Word Pattern.
    """
    def wordPattern(self, pattern, str):
        """
        Given a pattern and a string str, find if str follows the same pattern.

        Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

        Example 1:

        Input: pattern = "abba", str = "dog cat cat dog"
        Output: true
        Example 2:

        Input:pattern = "abba", str = "dog cat cat fish"
        Output: false
        Example 3:

        Input: pattern = "aaaa", str = "dog cat cat dog"
        Output: false
        Example 4:

        Input: pattern = "abba", str = "dog dog dog dog"
        Output: false
        Notes:
        You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
        Args:
            pattern: str value to match with str
            str: str value to match with pattern

        Returns:
            bool: True if it matches, False otherwise
        """
        words = str.split(' ')
        if len(words) != len(pattern):
            return False
        pattern_map = {}
        word_map = {}
        for char, word in zip(pattern, words):
            if char in pattern_map and pattern_map[char] != word:
                return False
            else:
                pattern_map[char] = word
            if word in word_map and word_map[word] != char:
                return False
            else:
                word_map[word] = char
        return True
