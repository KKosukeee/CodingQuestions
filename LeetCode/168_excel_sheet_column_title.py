"""
Solution for 168. Excel Sheet Column Title
https://leetcode.com/problems/excel-sheet-column-title/
"""

class Solution:
    """
    Runtime: 28 ms, faster than 99.08% of Python3 online submissions for Excel Sheet Column Title.
    Memory Usage: 13.4 MB, less than 5.38% of Python3 online submissions for Excel Sheet Column
        Title.
    """
    def convertToTitle(self, n):
        """
        Given a positive integer, return its corresponding column title as appear in an Excel sheet.

        For example:

            1 -> A
            2 -> B
            3 -> C
            ...
            26 -> Z
            27 -> AA
            28 -> AB
            ...
        Example 1:

        Input: 1
        Output: "A"
        Example 2:

        Input: 28
        Output: "AB"
        Example 3:

        Input: 701
        Output: "ZY"
        Args:
            n: int value to convert into EXCEL like column string

        Returns:
            str: EXCEL-like column definition
        """
        string = ''
        while n > 0:
            n, rem = divmod(n - 1, 26)
            string += chr(ord('A') + rem)

        return string[::-1]
