"""
Solution for 739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/
"""

class Solution:
    """
    Runtime: 308 ms, faster than 72.32% of Python3 online submissions for Daily Temperatures.
    Memory Usage: 16.8 MB, less than 8.66% of Python3 online submissions for Daily Temperatures.
    """
    def dailyTemperatures(self, T):
        """
        Given a list of daily temperatures T, return a list such that, for each day in the input,
        tells you how many days you would have to wait until a warmer temperature. If there is no
        future day for which this is possible, put 0 instead.

        For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your
        output should be [1, 1, 4, 2, 1, 1, 0, 0].
        Args:
            T:

        Returns:

        """
        stack = []
        result = [0] * len(T)

        # Loop from backward
        for i in range(len(T) - 1, -1, -1):

            # Pop an element until the top element in the stack is warmer than the current one
            while stack and T[i] >= T[stack[-1]]:
                _ = stack.pop()

            # If there is an element left in the stack, the check the difference between current i
            if stack:
                result[i] = stack[-1] - i

            stack.append(i)

        return result
