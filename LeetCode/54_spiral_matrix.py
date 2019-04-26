"""
Solution for 54. Spiral Matrix
https://leetcode.com/problems/spiral-matrix/
"""

class Solution:
    """
    Runtime: 36 ms, faster than 77.01% of Python3 online submissions for Spiral Matrix.
    Memory Usage: 13.3 MB, less than 5.18% of Python3 online submissions for Spiral Matrix.
    """
    def spiralOrder(self, matrix):
        """
        Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix
        in spiral order.

        Example 1:

        Input:
        [
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]
        Output: [1,2,3,6,9,8,7,4,5]
        Example 2:

        Input:
        [
          [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9,10,11,12]
        ]
        Output: [1,2,3,4,8,12,11,10,9,5,6,7]
        Args:
            matrix: 2D matrix

        Returns:
            list<int>: list of integer values in spiral order in matrix
        """
        if not matrix:
            return []

        # Initialize index i and j
        i, j, k = 0, 0, 0

        # Initialize a direction with a tuple
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        # Initialize result array for keeping spiral order
        result = [matrix[i][j]]
        matrix[i][j] = -float('inf')

        # Loop, while exploring is True
        while True:
            if not self.check_direction(matrix, i, j, directions[k]):
                k = (k + 1) % 4

                if not self.check_direction(matrix, i, j, directions[k]):
                    break

            i += directions[k][0]
            j += directions[k][1]
            result.append(matrix[i][j])
            matrix[i][j] = -float('inf')

        return result

    def check_direction(self, matrix, row, col, direction):
        """
        Checks if the direction is valid or not for given row and col
        Args:
            matrix: 2D matrix same as the main function's matrix
            row: current row index value which could be >= len(matrix)
            col: current col index value which could be >= len(matrix[0])
            direction: tuple of integers for heading direction

        Returns:
            bool: True if the heading direction is valid, otherwise False
        """
        new_row = row + direction[0]
        new_col = col + direction[1]

        if 0 <= new_row < len(matrix) and \
                0 <= new_col < len(matrix[0]) and \
                matrix[new_row][new_col] != -float('inf'):
            return True
        else:
            return False
