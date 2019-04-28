"""
Solution for 6. ZigZag Conversion
https://leetcode.com/problems/zigzag-conversion/
"""

class Solution:
    """
    Runtime: 64 ms, faster than 96.41% of Python3 online submissions for ZigZag Conversion.
    Memory Usage: 13.1 MB, less than 11.29% of Python3 online submissions for ZigZag Conversion.
    """
    def convert(self, s, numRows):
        """
        The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like
        this: (you may want to display this pattern in a fixed font for better legibility)

        P   A   H   N
        A P L S I I G
        Y   I   R
        And then read line by line: "PAHNAPLSIIGYIR"

        Write the code that will take a string and make this conversion given a number of rows:

        string convert(string s, int numRows);
        Example 1:

        Input: s = "PAYPALISHIRING", numRows = 3
        Output: "PAHNAPLSIIGYIR"
        Example 2:

        Input: s = "PAYPALISHIRING", numRows = 4
        Output: "PINALSIGYAHRPI"
        Explanation:

        P     I    N
        A   L S  I G
        Y A   H R
        P     I
        Args:
            s: string to return the zigzag pattern from
            numRows: int indicating the # of rows

        Returns:
            str: zigzag pattern string
        """
        if numRows == 1:
            return s

        # Initialize current row
        current_row = 0

        # Initialize direction
        direction = -1

        # Initialize row container
        row_container = [""] * numRows

        # Initialize concat_string
        concat_string = ''

        # Loop through s
        for i in range(len(s)):

            # Append s[i] to corresponding row container
            row_container[current_row] += s[i]

            # Change direction
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1

            # Move onto next row
            current_row += direction

        # Loop through row container
        for i in range(len(row_container)):
            # Concatenate string
            concat_string += row_container[i]

        # Return the concatenated string
        return concat_string
