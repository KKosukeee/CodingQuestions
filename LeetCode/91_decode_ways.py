"""
Solution for 91. Decode Ways
https://leetcode.com/problems/decode-ways/
"""

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
