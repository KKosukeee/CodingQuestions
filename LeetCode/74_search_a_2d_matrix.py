"""
Solution for 74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
"""

class Solution:
    """
    Runtime: 36 ms, faster than 96.37% of Python3 online submissions for Search a 2D Matrix.
    Memory Usage: 14 MB, less than 33.84% of Python3 online submissions for Search a 2D Matrix.
    """
    def searchMatrix(self, matrix, target):
        """
        Simple approach
        Args:
            matrix: 2D matrix to look a target from
            target: an integer value to look for

        Returns:
            bool: True if target exists in the matrix, otherwise False
        """
        # Check if the matrix is empty, if so return False
        if len(matrix) == 0:
            return False

        if len(matrix[0]) == 0:
            return False

        # Determine which row we should look for
        row = self.vertical_search(matrix, target)

        # Given the row, do the binary search to determine if the value exists or not
        return self.horizontal_search(matrix[row], target)

    def vertical_search(self, matrix, target):
        """
        This determines which row we should look for to find the target value
        Args:
            matrix: 2D matrix to look a target from
            target: an integer value to look for

        Returns:
            bool: True if target exists in the matrix, otherwise False
        """
        # Initialize low and high
        low, high = 0, len(matrix) - 1

        # Keep dividing in half, until the low exceeds the high
        while low <= high:

            # Create a pointer that points the middle value
            mid = (low + high) // 2

            # If the value falls into the range, then we know that row should contain the target
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return mid

            # If the middle row's first is larger than the target, then look for the left half
            elif target < matrix[mid][0]:
                high = mid - 1

            # If the middle row's last element is smaller than the target, the look for right half
            elif target > matrix[mid][-1]:
                low = mid + 1

        return -1

    def horizontal_search(self, row, target):
        """
        This function determines if the target value exists in the row or not
        Args:
            row: 1D array where each element is integer
            target: int value to look from row

        Returns:
            bool: True if the target value exists in the row, otherwise False will be returned
        """
        # Initialize low and high for a binary search
        low, high = 0, len(row) - 1

        # Keep divining into a half, until the left point exceeds the right pointer
        while low <= high:
            # Get the middle pointer
            mid = (low + high) // 2

            # If the middle value is the one we are looking for, then return True
            if row[mid] == target:
                return True

            # If the middle value is larger than the target, then look for the left half
            elif target < row[mid]:
                high = mid - 1

            # If the middle value is smaller than the target, then look for the right half
            else:
                low = mid + 1

        # If the code reaches to this point, then this means we couldn't find the target
        return False
