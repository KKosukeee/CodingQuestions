"""
Solution for 405. Convert a Number to Hexadecimal
https://leetcode.com/problems/convert-a-number-to-hexadecimal/
"""
class Solution:
    """
    Runtime: 32 ms, faster than 88.97% of Python3 online submissions for Convert a Number to Hexadecimal.
    Memory Usage: 13.8 MB, less than 50.00% of Python3 online submissions for Convert a Number to Hexadecimal.
    """
    def toHex(self, num):
        """
        Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

        Note:

        All letters in hexadecimal (a-f) must be in lowercase.
        The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
        The given number is guaranteed to fit within the range of a 32-bit signed integer.
        You must not use any method provided by the library which converts/formats the number to hex directly.
        Example 1:

        Input:
        26

        Output:
        "1a"
        Example 2:

        Input:
        -1

        Output:
        "ffffffff"
        Args:
            num(int):

        Returns:
            str:
        """
        if not num:
            return '0'
        if num < 0:
            num += 2 ** 32
        s = ''
        while num:
            rem = num & 15
            if rem >= 10:
                rem = chr(ord('a') + rem - 10)
            s = str(rem) + s
            num >>= 4
        return s
