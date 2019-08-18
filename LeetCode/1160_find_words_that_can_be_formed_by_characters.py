"""
Solution for 1160. Find Words That Can Be Formed by Characters
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
"""
from collections import Counter
class Solution:
    """
    Runtime: 420 ms, faster than 100.00% of Python3 online submissions for Find Words That Can Be Formed by Characters.
    Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Find Words That Can Be Formed by Characters.
    """
    def countCharacters(self, words, chars):
        """
        You are given an array of strings words and a string chars.

        A string is good if it can be formed by characters from chars (each character can only be used once).

        Return the sum of lengths of all good strings in words.



        Example 1:

        Input: words = ["cat","bt","hat","tree"], chars = "atach"
        Output: 6
        Explanation:
        The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
        Example 2:

        Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
        Output: 10
        Explanation:
        The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


        Note:

        1 <= words.length <= 1000
        1 <= words[i].length, chars.length <= 100
        All strings contain lowercase English letters only.
        Args:
            words(list[str]):
            chars(str):

        Returns:
            int:
        """
        char_counter = Counter(chars)
        char_count = 0
        for word in words:
            word_counter = Counter(word)
            if not word_counter - char_counter:
                char_count += len(word)
        return char_count
