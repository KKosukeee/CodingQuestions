"""
Solution for 231. Power of Two
"""

class Solution:
    """
    Runtime: 32 ms, faster than 93.30% of Python3 online submissions for Power of Two.
    Memory Usage: 13.1 MB, less than 92.37% of Python3 online submissions for Power of Two.
    """
    def isPowerOfTwo(self, n):
        """
        Given an integer, write a function to determine if it is a power of two.

        Example 1:

        Input: 1
        Output: true
        Explanation: 20 = 1
        Example 2:

        Input: 16
        Output: true
        Explanation: 24 = 16
        Example 3:

        Input: 218
        Output: false
        Args:
            n: int value to determine whether n is power of two

        Returns:
            bool: True if n is power of 2, False otherwise
        """
        if n <= 0:
            return False

        while n % 1 == 0:
            if n == 1:
                return True

            n /= 2

        return False