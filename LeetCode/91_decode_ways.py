"""
Solution for 91. Decode Ways
https://leetcode.com/problems/decode-ways/
"""
from functools import lru_cache

class Solution:
    """
    Runtime: 36 ms, faster than 99.97% of Python3 online submissions for Decode Ways.
    Memory Usage: 13.2 MB, less than 18.18% of Python3 online submissions for Decode Ways.
    """
    def numDecodings(self, s):
        """
        A message containing letters from A-Z is being encoded to numbers using the following
        mapping:

        'A' -> 1
        'B' -> 2
        ...
        'Z' -> 26
        Given a non-empty string containing only digits, determine the total number of ways to
        decode it.

        Example 1:

        Input: "12"
        Output: 2
        Explanation: It could be decoded as "AB" (1 2) or "L" (12).
        Example 2:

        Input: "226"
        Output: 3
        Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
        Args:
            s: string to find how many decode ways exists in the string

        Returns:
            int: indicating how many ways to decode the input string
        """
        arr = [0] * (len(s) + 1)
        arr[-1] = 1
        arr[-2] = 1 if s[-1] != '0' else 0

        for i in reversed(range(0, len(s) - 1)):
            if s[i] == '1':
                arr[i] = arr[i + 1] + arr[i + 2]
            elif s[i] == '2':
                arr[i] = arr[i + 1]
                if s[i + 1] <= '6':
                    arr[i] += arr[i + 2]
            elif s[i] == '0':
                arr[i] = 0
            else:
                arr[i] = arr[i + 1]

        return arr[0]

    def brute_force(self, s: str) -> int:
        """
        A brute force solution that runs in O(2^N) in time and space

        Args:
            s(str):

        Returns:
            int:

        """
        if len(s) <= 0:
            return 0
        if s[0] == '0':
            return 0
        if int(s) <= 26:
            return 1 if int(s) < 10 or s[-1] == '0' else 2
        if int(s[:2]) <= 26:
            return self.brute_force(s[1:]) + self.brute_force(s[2:])
        else:
            return self.brute_force(s[1:])

    def top_down(self, s: str) -> int:
        """
        A top-down solution that runs in O(N) in time and space

        Args:
            s(str):

        Returns:
            int:

        """
        @lru_cache(None)
        def rec(s):
            if len(s) <= 0:
                return 0
            if s[0] == '0':
                return 0
            if int(s) <= 26:
                return 1 if int(s) < 10 or s[-1] == '0' else 2
            if int(s[:2]) <= 26:
                return rec(s[1:]) + rec(s[2:])
            else:
                return rec(s[1:])

        return rec(s)

    def bottom_up(self, s: str) -> int:
        """
        A bottom-up solution that runs in O(N) in time and space

        Args:
            s:

        Returns:

        """
        dp = [1 if s[0] != '0' else 0]
        for i in range(1, len(s)):
            ways = dp[-1] if s[i] != '0' else 0
            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                ways += dp[i - 2] if i - 2 >= 0 else 1
            dp.append(ways)
        return dp[-1]

    def optimal(self, s: str) -> int:
        """
        An optimal solution thar runs in O(N) in time and O(1) in space

        Args:
            s(str):

        Returns:
            int:

        """
        pprev, prev = 0, 1 if s[0] != '0' else 0
        for i in range(1, len(s)):
            ways = prev if s[i] != '0' else 0
            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                ways += pprev if i - 2 >= 0 else 1
            pprev = prev
            prev = ways
        return prev
