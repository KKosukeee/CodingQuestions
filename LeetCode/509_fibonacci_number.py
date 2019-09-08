"""
Solution for 509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/
"""
from typing import List

class Solution:
    """
    Runtime: 36 ms, faster than 73.35% of Python3 online submissions for Fibonacci Number.
    Memory Usage: 13.9 MB, less than 5.80% of Python3 online submissions for Fibonacci Number.
    """
    def recursion(self, N: int) -> int:
        """
        Solves N-th fib in brute force way. This runs in O(2^N) in space and runtime.

        Args:
            N(int):

        Returns:
            int:

        """
        if N <= 1:
            return N
        return self.recursion(N - 1) + self.recursion(N - 2)

    def top_down(self, N: int, dp: dict = {0: 0, 1: 1}) -> int:
        """
        Top-down DP solution that runs in O(N) in space and runtime

        Args:
            N(int):

        Returns:
            int:

        """
        if N in dp:
            return dp[N]
        dp[N] = self.top_down(N - 1, dp) + self.top_down(N - 2, dp)
        return dp[N]

    def bottom_up(self, N: int) -> int:
        """
        Bottom-up DP solution that runs in O(N) in space and time

        Args:
            N(int):

        Returns:
            int:

        """
        if N <= 1:
            return N
        dp = [0, 1]
        for i in range(2, N + 1):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]

    def constant(self, N: int) -> int:
        """
        Bottom-up DP solution that runs in O(N) and O(1) in time and space respectively

        Args:
            N(int):

        Returns:
            int:

        """
        if N <= 1:
            return N
        last, second_last = 0, 1
        for i in range(2, N + 1):
            last, second_last = last + second_last, last
        return last + second_last

    def fib(self, N: int) -> int:
        """
        The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

        F(0) = 0,   F(1) = 1
        F(N) = F(N - 1) + F(N - 2), for N > 1.
        Given N, calculate F(N).



        Example 1:

        Input: 2
        Output: 1
        Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
        Example 2:

        Input: 3
        Output: 2
        Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
        Example 3:

        Input: 4
        Output: 3
        Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


        Note:

        0 ≤ N ≤ 30.

        Args:
            N(int):

        Returns:
            int:

        """
        return self.constant(N)

    # fib(2) = fib(1) + fib(0)
    # fib(2) = 1 + 0
    # fib(2) = 1

    # fib(5) = fib(4) + fib(3)
    # fib(4) = fib(3) + fib(2)
    # fib(3) = fib(2) + fib(1)
    # fib(2) = fib(1) + fib(0)
    # fib(2) = 1 + 0 = 1
    # O(2^N)

    #