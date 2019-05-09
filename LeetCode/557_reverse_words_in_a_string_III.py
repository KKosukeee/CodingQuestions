"""
Solution for 557. Reverse Words in a String III
https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""

class Solution:
    """
    Runtime: 36 ms, faster than 99.34% of Python3 online submissions for Reverse Words in a
        String III.
    Memory Usage: 13.7 MB, less than 5.70% of Python3 online submissions for Reverse Words in a
        String III.
    """
    def reverseWords(self, s):
        """
        Given a string, you need to reverse the order of characters in each word within a sentence
        while still preserving whitespace and initial word order.

        Example 1:
        Input: "Let's take LeetCode contest"
        Output: "s'teL ekat edoCteeL tsetnoc"
        Args:
            s: string where you swap for each word

        Returns:
            str: string object which is from input s but for each word swapped
        """
        swapped_words = []

        for word in s.split():
            swapped_words.append(word[::-1])

        return ' '.join(swapped_words)
