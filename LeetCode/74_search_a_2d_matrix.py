"""
Solution for 74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
"""


class Solution:
    """
    Runtime: 40 ms, faster than 81.48% of Python3 online submissions for Search a 2D Matrix.
    Memory Usage: 13.9 MB, less than 5.71% of Python3 online submissions for Search a 2D Matrix
    """
    def simple_approach(self, matrix, target):
        """
        Simple approach
        Args:
            matrix: 2D matrix to look a target from
            target: an integer value to look for

        Returns:
            bool: True if target exists in the matrix, otherwise False
        """
        if len(matrix) == 0:
            return False

        if len(matrix[0]) == 0:
            return False

        # Placeholder for a row
        target_row = None

        # Loop for each row, and pick by checking if target falls into the range
        for row in matrix:
            if row[0] <= target <= row[-1]:
                target_row = row
                break

        if target_row:
            # Do the binary search to determine whether the target is there or not
            return self.binary_search(target_row, target)
        else:
            return False

    def binary_search(self, row, target):
        """
        An iterative binary search method
        Args:
            row: list to look a target from
            target: integer value to look for

        Returns:
            bool: True if value exists in row, False otherwise
        """
        low = 0
        high = len(row) - 1

        while low <= high:
            mid = (low + high) // 2

            if row[mid] == target:
                return True
            elif row[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False

    def optimal_approach(self, matrix, target):
        """
        Optimal solution
        Args:
            matrix: 2D matrix to look a target from
            target: an integer value to look for

        Returns:
            bool: True if target exists in the matrix, otherwise False
        """
        if len(matrix) == 0:
            return False

        if len(matrix[0]) == 0:
            return False

        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = (m * n) - 1

        while low <= high:
            mid = (low + high) // 2
            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False

    def searchMatrix(self, matrix, target):
        """
        Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has
        the following properties:

        Integers in each row are sorted from left to right.
        The first integer of each row is greater than the last integer of the previous row.
        Example 1:

        Input:
        matrix = [
          [1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ]
        target = 3
        Output: true
        Example 2:

        Input:
        matrix = [
          [1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ]
        target = 13
        Output: false
        Main function for the question
        Args:
            matrix: 2D matrix to look a target from
            target: an integer value to look for

        Returns:
            bool: True if target exists in the matrix, otherwise False
        """
        return self.optimal_approach(matrix, target)
