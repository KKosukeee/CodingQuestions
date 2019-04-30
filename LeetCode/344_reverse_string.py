"""
Solution for 344. Reverse String
https://leetcode.com/problems/reverse-string/
"""

class Solution:
    """
    Runtime: 172 ms, faster than 69.43% of Python3 online submissions for Reverse String.
    Memory Usage: 17.7 MB, less than 11.40% of Python3 online submissions for Reverse String.
    """
    def reverseString(self, s):
        """
        Write a function that reverses a string. The input string is given as an array of
        characters char[].

        Do not allocate extra space for another array, you must do this by modifying the input
        array in-place with O(1) extra memory.

        You may assume all the characters consist of printable ascii characters.

        Example 1:

        Input: ["h","e","l","l","o"]
        Output: ["o","l","l","e","h"]
        Example 2:

        Input: ["H","a","n","n","a","h"]
        Output: ["h","a","n","n","a","H"]
        Args:
            s: list of string to swap with

        Returns:

        """
        for i in range(len(s) // 2):
            swapping = len(s) - (i + 1)
            s[i], s[swapping] = s[swapping], s[i]
