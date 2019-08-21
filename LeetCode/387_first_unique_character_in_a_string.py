"""
Solution for 387. First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/
"""
from collections import Counter
class Solution:
    """
    Runtime: 104 ms, faster than 81.22% of Python3 online submissions for First Unique Character in a String.
    Memory Usage: 13.9 MB, less than 6.52% of Python3 online submissions for First Unique Character in a String.
    """
    def firstUniqChar(self, s):
        """
        Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

        Examples:

        s = "leetcode"
        return 0.

        s = "loveleetcode",
        return 2.
        Note: You may assume the string contain only lowercase letters.
        Args:
            s(str):

        Returns:
            int:
        """
        char_count = Counter(s)
        for i in range(len(s)):
            if char_count[s[i]] == 1:
                return i
        return -1
