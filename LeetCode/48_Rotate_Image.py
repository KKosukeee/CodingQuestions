"""
Solution for 48. Rotate Image
https://leetcode.com/problems/rotate-image/
"""


class Solution:
    """
    Runtime: 40 ms, faster than 74.53% of Python3 online submissions for Rotate Image.
    Memory Usage: 13.4 MB, less than 5.35% of Python3 online submissions for Rotate Image.
    """
    def rotate(self, matrix):
        """
        Main function to solve a question.
        Do not return anything, modify matrix in-place instead.
        Args:
            matrix: 2D matrix containing integer values.

        Returns:

        """

        # Create a set for recording swapped indices
        swapped_indices = set()

        # Loop through for each element to swap them
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # Calculate new location
                new_col = len(matrix[0]) - i - 1
                new_row = j

                # If current indices are not swapped already, then swap them
                if (i, j) not in swapped_indices:
                    matrix[i][j], matrix[new_row][new_col] = matrix[new_row][new_col], matrix[i][j]

                    # Now new_row and new_col are in right place, add it.
                    swapped_indices.add((new_row, new_col))
