"""
Solution for 131. Palindrome Partitioning
"""

class Solution:
    """
    Runtime: 84 ms, faster than 89.37% of Python3 online submissions for Palindrome Partitioning.
    Memory Usage: 13.7 MB, less than 22.87% of Python3 online submissions for Palindrome Partitioning.
    """
    def partition(self, s):
        """
        Given a string s, partition s such that every substring of the partition is a palindrome.

        Return all possible palindrome partitioning of s.

        Example:

        Input: "aab"
        Output:
        [
          ["aa","b"],
          ["a","a","b"]
        ]Given a string s, partition s such that every substring of the partition is a palindrome.

        Return all possible palindrome partitioning of s.

        Example:

        Input: "aab"
        Output:
        [
          ["aa","b"],
          ["a","a","b"]
        ]
        Args:
            s: str value to find the palindrome partitions

        Returns:
            list<list<str>>: where each list is a palindrome subset
        """
        output = []
        dp = [[False for j in range(len(s))] for i in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True

        for diff in range(1, len(s)):
            for left in range(len(s) - diff):
                right = left + diff

                if diff == 1 and s[left] == s[right]:
                    dp[left][right] = True

                if s[left] == s[right] and dp[left + 1][right - 1]:
                    dp[left][right] = True

        def dfs(left, path):
            if left >= len(s):
                output.append(path)
                return

            for right in range(left, len(s)):
                if dp[left][right]:
                    dfs(right + 1, path + [s[left:right + 1]])

        output = []
        dfs(0, [])

        return output
