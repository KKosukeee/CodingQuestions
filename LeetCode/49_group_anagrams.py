"""
Solution for 49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
"""
from collections import defaultdict

class Solution:
    """
    Runtime: 128 ms, faster than 27.60% of Python3 online submissions for Group Anagrams.
    Memory Usage: 19.3 MB, less than 5.09% of Python3 online submissions for Group Anagrams.
    """
    def groupAnagrams(self, strs):
        """
        Given an array of strings, group anagrams together.

        Example:

        Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
        Output:
        [
          ["ate","eat","tea"],
          ["nat","tan"],
          ["bat"]
        ]
        Note:

        All inputs will be in lowercase.
        The order of your output does not matter.
        Args:
            strs: list<str> to group anagrams

        Returns:
            list<list<str>>: representing each group
        """
        count_dict = defaultdict(list)
        for str in strs:
            count_bin = [0] * 26

            for char in str:
                count_bin[ord(char) - ord('a')] += 1

            count_dict[tuple(count_bin)].append(str)

        return count_dict.values()
