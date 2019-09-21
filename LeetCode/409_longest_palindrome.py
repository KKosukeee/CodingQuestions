"""
Solution for 409. Longest Palindrome
https://leetcode.com/problems/longest-palindrome/
"""
from collections import defaultdict
from collections import Counter

class Solution:
    """
    Runtime: 36 ms, faster than 85.14% of Python3 online submissions for Longest Palindrome.
    Memory Usage: 13.7 MB, less than 8.33% of Python3 online submissions for Longest Palindrome.
    """
    def first(self, s: str) -> int:
        """
        Simple solution that I come up with first

        Args:
            s(str):

        Returns:
            int:

        """
        counter = defaultdict(int)
        even_count, odd_count = 0, 0
        for char in s:
            counter[char] += 1
            if counter[char] & 1 == 0:
                even_count, odd_count = even_count + 2, odd_count - 1
            else:
                odd_count += 1

        return even_count + min(1, odd_count)

    def second(self, s: str) -> int:
        """
        Interesting solution that I found in the discussion

        Args:
            s(str):

        Returns:
            int:

        """
        odd_counts = sum(count & 1 for count in Counter(s).values())
        return len(s) - odd_counts + min(1, odd_counts)

    def longestPalindrome(self, s: str) -> int:
        """
        Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

        This is case sensitive, for example "Aa" is not considered a palindrome here.

        Note:
        Assume the length of given string will not exceed 1,010.

        Example:

        Input:
        "abccccdd"

        Output:
        7

        Explanation:
        One longest palindrome that can be built is "dccaccd", whose length is 7.

        Args:
            s(str):

        Returns:
            int:

        """
        return self.first(s)
