"""
Solution for 72. Edit Distance
https://leetcode.com/problems/edit-distance/
"""

class Solution:
    """
    Runtime: 128 ms, faster than 94.95% of Python3 online submissions for Edit Distance.
    Memory Usage: 30.5 MB, less than 5.48% of Python3 online submissions for Edit Distance.
    """
    def minDistance(self, word1, word2, cache={}):
        """
        Given two words word1 and word2, find the minimum number of operations required to convert
        word1 to word2.

        You have the following 3 operations permitted on a word:

        Insert a character
        Delete a character
        Replace a character
        Example 1:

        Input: word1 = "horse", word2 = "ros"
        Output: 3
        Explanation:
        horse -> rorse (replace 'h' with 'r')
        rorse -> rose (remove 'r')
        rose -> ros (remove 'e')
        Example 2:

        Input: word1 = "intention", word2 = "execution"
        Output: 5
        Explanation:
        intention -> inention (remove 't')
        inention -> enention (replace 'i' with 'e')
        enention -> exention (replace 'n' with 'x')
        exention -> exection (replace 'n' with 'c')
        exection -> execution (insert 'u')
        Args:
            word1: string to represent a word
            word2: string to represent a word
            cache: dict for memoization

        Returns:
            int: indicating number of steps it requires to get exact same word for both 1 and 2
        """
        cache_key = (word1, word2)
        if cache_key in cache:
            return cache[cache_key]
        result = 0
        if not word1 or not word2:
            result = len(word1) + len(word2)
            cache[cache_key] = result
            return result
        if word1 == word2:
            cache[cache_key] = result
            return result
        char1 = word1[0]
        char2 = word2[0]
        if char1 == char2:
            result = self.minDistance(word1[1:], word2[1:], cache)
        else:
            first = self.minDistance(word1[1:], word2, cache)
            second = self.minDistance(word1, word2[1:], cache)
            third = self.minDistance(word2[0] + word1[1:], word2, cache)
            result = min([first, second, third]) + 1
        cache[cache_key] = result
        return result
