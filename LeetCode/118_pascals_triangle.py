"""
Solution for 118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/
"""

class Solution:
    """
    Runtime: 32 ms, faster than 98.16% of Python3 online submissions for Pascal's Triangle.
    Memory Usage: 13.1 MB, less than 53.10% of Python3 online submissions for Pascal's Triangle.
    """
    def generate(self, numRows):
        """
        Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


        In Pascal's triangle, each number is the sum of the two numbers directly above it.

        Example:

        Input: 5
        Output:
        [
             [1],
            [1,1],
           [1,2,1],
          [1,3,3,1],
         [1,4,6,4,1]
        ]
        Args:
            numRows: int value representing the number of rows for the output triangle

        Returns:
            list<list<int>>: list of list of integer forming as a pascal triangle
        """
        # Create a triangle shape with those elements
        triangle = []
        for i in range(numRows):
            elements = []

            for j in range(i + 1):
                if j == 0 or j == i:
                    elements.append(1)
                else:
                    elements.append(0)

            triangle.append(elements)

        # Loop for each element in the triangle
        for i in range(numRows):
            for j in range(len(triangle[i])):

                # If the element is zero, then look above numbers
                if triangle[i][j] == 0:
                    triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Return it
        return triangle
