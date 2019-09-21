"""
Solution for 266. Palindrome Permutation
https://leetcode.com/problems/palindrome-permutation/
"""
from collections import defaultdict

class Solution:
    """
    Runtime: 28 ms, faster than 97.34% of Python3 online submissions for Palindrome Permutation.
    Memory Usage: 13.6 MB, less than 50.00% of Python3 online submissions for Palindrome Permutation.
    """
    def canPermutePalindrome(self, s: str) -> bool:
        """
        Given a string, determine if a permutation of the string could form a palindrome.

        Example 1:

        Input: "code"
        Output: false
        Example 2:

        Input: "aab"
        Output: true
        Example 3:

        Input: "carerac"
        Output: true

        Args:
            s(str):

        Returns:
            bool:

        """
        counter = defaultdict(int)
        odd_count = 0
        for char in s:
            counter[char] += 1
            if counter[char] % 2 == 0:
                odd_count -= 1
            else:
                odd_count += 1
        return odd_count <= 1
    