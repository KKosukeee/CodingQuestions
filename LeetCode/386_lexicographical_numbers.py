"""
Solution for 386. Lexicographical Numbers
https://leetcode.com/problems/lexicographical-numbers/
"""

class Solution:
    """
    Runtime: 164 ms, faster than 60.66% of Python3 online submissions for Lexicographical Numbers.
    Memory Usage: 21.6 MB, less than 9.16% of Python3 online submissions for Lexicographical
        Numbers.
    """
    def lexicalOrder(self, n):
        """
        Given an integer n, return 1 - n in lexicographical order.

        For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

        Please optimize your algorithm to use less time and space. The input size may be as
        large as 5,000,000.
        Args:
            n: int value representing the range that we need to sort

        Returns:
            list<int>: where the number of element is n and sorted in lexicographic order
        """
        result = []

        def dfs(current):
            if current <= n:
                result.append(current)

                # Call for multiple of 10
                dfs(current * 10)

                # Avoid duplicate, cause I have already done for multiple of 10
                if (current + 1) % 10 != 0:
                    dfs(current + 1)

        dfs(1)
        return result