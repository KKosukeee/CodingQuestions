"""
Solution for 171. Excel Sheet Column Number
https://leetcode.com/problems/excel-sheet-column-number/
"""

class Solution:
    """
    Runtime: 40 ms, faster than 92.78% of Python3 online submissions for Excel Sheet Column Number.
    Memory Usage: 13.4 MB, less than 12.10% of Python3 online submissions for Excel Sheet Column
        Number.
    """
    def titleToNumber(self, s):
        """
        Given a column title as appear in an Excel sheet, return its corresponding column number.

        For example:

            A -> 1
            B -> 2
            C -> 3
            ...
            Z -> 26
            AA -> 27
            AB -> 28
            ...
        Example 1:

        Input: "A"
        Output: 1
        Example 2:

        Input: "AB"
        Output: 28
        Example 3:

        Input: "ZY"
        Output: 701
        Args:
            s: string value which you convert into int with EXCEL definition

        Returns:
            int: from s
        """
        result = 0
        for i in range(len(s)):
            n = len(s) - i - 1
            diff = ord(s[i]) - ord('A')
            result += 26 ** n * (diff + 1)

        return result
