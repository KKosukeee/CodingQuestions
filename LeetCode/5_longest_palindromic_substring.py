"""
Solution 5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/
"""

class Solution:
    """
    Runtime: 1896 ms, faster than 43.67% of Python3 online submissions for Longest Palindromic
        Substring.
    Memory Usage: 13.1 MB, less than 25.51% of Python3 online submissions for Longest Palindromic
        Substring.
    """
    # Brute force -> O(n ^ 3)
    def naive_approach(self, s):
        """
        Naive approach for the question
        Args:
            s: str object to find longest palindromic substring from

        Returns:
            str: longest palindromic string
        """
        result = ''

        for i in range(len(s)):  # -> O(n)
            j = len(s)

            while i != j + 1:  # -> O(n - 1)
                string = s[i:j]
                reverse = string[::-1]

                if string == reverse and len(string) > len(result):
                    result = string

                j -= 1

        return result

    def optimal_approach(self, s):
        """
        Optimal approach for the question
        Args:
            s: str object to find longest palindromic substring from

        Returns:
            str: longest palindromic string
        """
        result = ''

        for i in range(len(s)):  # -> O(n)
            tmp = self.helper(s, i, i)  # -> O(n)

            if len(tmp) > len(result):
                result = tmp

            tmp = self.helper(s, i, i + 1)  # -> O(n)

            if len(tmp) > len(result):
                result = tmp

        return result

    def helper(self, s, l, r):
        """
        A helper recursive function
        Args:
            s: str to find longest palindromic string from
            l: left pointer to expand
            r: right pointer to expand

        Returns:
            str: longest palindromic string
        """
        result = ''

        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len(result):
                result = s[l:r + 1]

            l -= 1
            r += 1

        return result

    def longestPalindrome(self, s):
        """
        Given a string s, find the longest palindromic substring in s. You may assume that the
        maximum length of s is 1000.

        Example 1:

        Input: "babad"
        Output: "bab"
        Note: "aba" is also a valid answer.
        Example 2:

        Input: "cbbd"
        Output: "bb"
        Args:
            s: str object to find longest palindromic substring from

        Returns:
            str: longest palindromic string
        """
        return self.optimal_approach(s)
