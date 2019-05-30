"""
Solution for 70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/
"""

class Solution:
    """
    Runtime: 48 ms, faster than 16.88% of Python3 online submissions for Climbing Stairs.
    Memory Usage: 13.2 MB, less than 5.18% of Python3 online submissions for Climbing Stairs.
    """

    def recursion(self, current, n):
        """
        This solves the question in recursive way
        Args:
            current: int value representing the current step
            n: int value representing the number of steps you need to take

        Returns:
            int: representing the ways to get to n from 0
        """
        if current == n:
            return 1
        elif current > n:
            return 0

        return self.recursion(current+1, n) + self.recursion(current+2, n)

    def dp(self, current, n, memo):
        """
        This solves the question using DP
        Args:
            current: int value representing the current step
            n: int value representing the number of steps you need to take

        Returns:
            int: representing the ways to get to n from 0
        """
        if current == n:
            return 1
        elif current > n:
            return 0

        if current in memo:
            return memo[current]

        memo[current+1] = self.dp(current+1, n, memo)
        memo[current+2] = self.dp(current+2, n, memo)
        memo[current] = memo[current+1] + memo[current+2]
        return memo[current]

    def optimized_dp(self, n):
        """
        This solution does the similar thing as self.dp, but uses less memory
        Args:
            n: int value representing the number of steps you need to take

        Returns:
            int: representing the ways to get to n from 0
        """
        if n < 2:
            return 1

        # Only remember previous two steps
        first_last = 0
        second_last = 0

        for i in range(2, n):
            current_step = first_last + second_last
            second_last, first_last = first_last, current_step

        return first_last

    def climbStairs(self, n):
        """
        You are climbing a stair case. It takes n steps to reach to the top.

        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to
        the top?

        Note: Given n will be a positive integer.

        Example 1:

        Input: 2
        Output: 2
        Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps
        Example 2:

        Input: 3
        Output: 3
        Explanation: There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step
        Args:
            n: int value representing the number of steps you need to take

        Returns:
            int: representing the ways to get to n from 0
        """
        return self.dp(0, n, {})
