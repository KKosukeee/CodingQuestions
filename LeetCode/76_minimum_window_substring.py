"""
Solution for 76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/
"""
from collections import Counter

class Solution:
    """
    Runtime: 156 ms, faster than 49.34% of Python3 online submissions for Minimum Window Substring.
    Memory Usage: 13.3 MB, less than 17.58% of Python3 online submissions for Minimum Window
    Substring.
    """
    def minWindow(self, s, t):
        """
        Given a string S and a string T, find the minimum window in S which will contain all the
        characters in T in complexity O(n).

        Example:

        Input: S = "ADOBECODEBANC", T = "ABC"
        Output: "BANC"
        Args:
            s: string to look for t string from
            t: target string to look from s string

        Returns:
            str: substring which contains all chars in t from s
        """

        if not t or not s:
            return ""

        dict_t = Counter(t)
        required = len(dict_t)
        l, r = 0, 0
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None

        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            while l <= r and formed == required:
                character = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                l += 1

            r += 1

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
