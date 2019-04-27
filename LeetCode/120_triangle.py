"""
Solution for 120. Triangle
https://leetcode.com/problems/triangle/
"""

class Solution:
    """
    Runtime: 44 ms, faster than 82.74% of Python3 online submissions for Triangle.
    Memory Usage: 13.6 MB, less than 19.85% of Python3 online submissions for Triangle.
    """
    def minimumTotal(self, triangle):
        """
        Given a triangle, find the minimum path sum from top to bottom. Each step you may move
        to adjacent numbers on the row below.

        For example, given the following triangle

        [
             [2],
            [3,4],
           [6,5,7],
          [4,1,8,3]
        ]
        The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
        Args:
            triangle: list<list<int>>: weird 2D array, not a matrix

        Returns:
            int: the minimum path from the top to the bottom
        """
        # Initialize j with len(triangle) - 1
        i = len(triangle) - 1

        # Loop while j > 0
        while i > 0:

            # Loop through all the elements in the row, except the left and right corner
            for j in range(len(triangle[i - 1])):
                # Compare with (j - 1)th row's values, and take min
                triangle[i - 1][j] += min(triangle[i][j], triangle[i][j + 1])

            i -= 1

        return triangle[0][0]
