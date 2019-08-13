"""
Solution for 476. Number Complement
https://leetcode.com/problems/number-complement/
"""
import math
class Solution:
    """
    Runtime: 32 ms, faster than 90.72% of Python3 online submissions for Number Complement.
    Memory Usage: 13.8 MB, less than 10.00% of Python3 online submissions for Number Complement.
    """
    def findComplement(self, num):
        """
        Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

        Note:
        The given integer is guaranteed to fit within the range of a 32-bit signed integer.
        You could assume no leading zero bit in the integer’s binary representation.
        Example 1:
        Input: 5
        Output: 2
        Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
        Example 2:
        Input: 1
        Output: 0
        Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
        Args:
            num(int):

        Returns:
            int:
        """
        if num < 1:
            return 0
        power = int(math.ceil(math.log(num+1e-7, 2)))
        return num ^ (2**power-1)
