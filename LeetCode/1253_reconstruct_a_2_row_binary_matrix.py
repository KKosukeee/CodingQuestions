"""
Solution for 1253. Reconstruct a 2-Row Binary Matrix
https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/
"""
from typing import List

class Solution:
    """
    Runtime: 792 ms, faster than 100.00% of Python3 online submissions for Reconstruct a 2-Row Binary Matrix.
    Memory Usage: 23.6 MB, less than 100.00% of Python3 online submissions for Reconstruct a 2-Row Binary Matrix.
    """
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        """
        Given the following details of a matrix with n columns and 2 rows :

        The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.
        The sum of elements of the 0-th(upper) row is given as upper.
        The sum of elements of the 1-st(lower) row is given as lower.
        The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum is given as an integer array with length n.
        Your task is to reconstruct the matrix with upper, lower and colsum.

        Return it as a 2-D integer array.

        If there are more than one valid solution, any of them will be accepted.

        If no valid solution exists, return an empty 2-D array.



        Example 1:

        Input: upper = 2, lower = 1, colsum = [1,1,1]
        Output: [[1,1,0],[0,0,1]]
        Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.
        Example 2:

        Input: upper = 2, lower = 3, colsum = [2,2,1,1]
        Output: []
        Example 3:

        Input: upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
        Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]


        Constraints:

        1 <= colsum.length <= 10^5
        0 <= upper, lower <= colsum.length
        0 <= colsum[i] <= 2

        Args:
            upper:
            lower:
            colsum:

        Returns:

        """
        ones, twos = [], []
        for i in range(len(colsum)):
            if colsum[i] == 1:
                ones.append(i)
            elif colsum[i] == 2:
                twos.append(i)
        up, low = [0] * len(colsum), [0] * len(colsum)
        for i in twos:
            up[i], upper = 1, upper - 1
            low[i], lower = 1, lower - 1
            if upper < 0 or lower < 0:
                return []
        for i in ones:
            if upper > 0:
                up[i], upper = up[i] + 1, upper - 1
            elif lower > 0:
                low[i], lower = low[i] + 1, lower - 1
            else:
                return []
        return [up, low] if upper == 0 and lower == 0 else []
