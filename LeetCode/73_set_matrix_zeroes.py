"""
Solution for 73. Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/
"""

class Solution:
    """
    Runtime: 92 ms, faster than 81.76% of Python3 online submissions for Set Matrix Zeroes.
    Memory Usage: 13.6 MB, less than 5.26% of Python3 online submissions for Set Matrix Zeroes.
    """
    def setZeroes(self, matrix):
        """
        Given a m x n matrix, if an element is 0, set its entire row and column to 0.
        Do it in-place.

        Example 1:

        Input:
        [
          [1,1,1],
          [1,0,1],
          [1,1,1]
        ]
        Output:
        [
          [1,0,1],
          [0,0,0],
          [1,0,1]
        ]
        Example 2:

        Input:
        [
          [0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]
        ]
        Output:
        [
          [0,0,0,0],
          [0,4,5,0],
          [0,3,1,0]
        ]
        Args:
            matrix: 2D array to set zeros
        Returns:

        """
        # Initialize row and col set
        row_set, col_set = set(), set()

        # Loop for each row
        for i in range(len(matrix)):

            # Loop for each col
            for j in range(len(matrix[0])):

                # If the value is zero, then put it in row and col sets
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)

        # Loop through row set to update row values to zero
        for row in row_set:
            matrix[row] = [0] * len(matrix[0])

        # Loop through col set to update col values to zero
        for col in col_set:
            for i in range(len(matrix)):
                matrix[i][col] = 0
