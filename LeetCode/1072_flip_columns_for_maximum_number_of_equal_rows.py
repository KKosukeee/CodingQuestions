"""
Solution for 1072. Flip Columns For Maximum Number of Equal Rows
"""
from collections import defaultdict

class Solution:
    """
    Runtime: 160 ms, faster than 95.19% of Python3 online submissions for Flip Columns For Maximum
        Number of Equal Rows.
    Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for Flip Columns For
        Maximum Number of Equal Rows.
    """
    def maxEqualRowsAfterFlips(self, matrix):
        """
        Given a matrix consisting of 0s and 1s, we may choose any number of columns in the matrix
        and flip every cell in that column.  Flipping a cell changes the value of that cell from
        0 to 1 or from 1 to 0.

        Return the maximum number of rows that have all values equal after some number of flips.



        Example 1:

        Input: [[0,1],[1,1]]
        Output: 1
        Explanation: After flipping no values, 1 row has all values equal.
        Example 2:

        Input: [[0,1],[1,0]]
        Output: 2
        Explanation: After flipping values in the first column, both rows have equal values.
        Example 3:

        Input: [[0,0,0],[0,0,1],[1,1,0]]
        Output: 2
        Explanation: After flipping values in the first two columns, the last two rows have equal
        values.
        Args:
            matrix: list of list of integer where each element consists of 1 or 0.

        Returns:
            int: max number of equal row represented in int
        """
        if len(matrix[0]) <= 1:
            return len(matrix)

        max_count = 0
        row_dict = defaultdict(int)

        for row in matrix:
            if row[0] == 1:
                row = self.flip_row(row)

            row_dict[tuple(row)] += 1
            max_count = max(max_count, row_dict[tuple(row)])

        return max_count

    def flip_row(self, row):
        """
        This flips 0 and 1, returns the same size of array
        Args:
            row: list of int with the same shape of the input

        Returns:
            list<int>: where each element is flipped, meaning 1 becomes 0 and 0 becomes 1
        """
        return [0 if i else 1 for i in row]
