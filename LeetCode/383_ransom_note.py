"""
Solution for 383. Ransom Note
https://leetcode.com/problems/ransom-note/
"""
from collections import Counter
class Solution:
    """
    Runtime: 56 ms, faster than 65.53% of Python3 online submissions for Ransom Note.
    Memory Usage: 13.9 MB, less than 25.00% of Python3 online submissions for Ransom Note.
    """
    def canConstruct(self, ransomNote, magazine):
        """
        Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

        Each letter in the magazine string can only be used once in your ransom note.

        Note:
        You may assume that both strings contain only lowercase letters.

        canConstruct("a", "b") -> false
        canConstruct("aa", "ab") -> false
        canConstruct("aa", "aab") -> true
        Args:
            ransomNote(str):
            magazine(str):

        Returns:
            bool:
        """
        ransom_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)
        return not ransom_counter - magazine_counter
