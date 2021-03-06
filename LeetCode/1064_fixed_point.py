"""
Solution for 1064. Fixed Point
https://leetcode.com/problems/fixed-point/
"""
from typing import List

class Solution:
    """
    Runtime: 84 ms, faster than 8.68% of Python3 online submissions for Fixed Point.
    Memory Usage: 15.2 MB, less than 25.00% of Python3 online submissions for Fixed Point.
    """
    def fixedPoint(self, A: List[int]) -> int:
        """
        Given an array A of distinct integers sorted in ascending order, return the smallest index i that satisfies A[i] == i.  Return -1 if no such i exists.



        Example 1:

        Input: [-10,-5,0,3,7]
        Output: 3
        Explanation:
        For the given array, A[0] = -10, A[1] = -5, A[2] = 0, A[3] = 3, thus the output is 3.
        Example 2:

        Input: [0,2,5,8,17]
        Output: 0
        Explanation:
        A[0] = 0, thus the output is 0.
        Example 3:

        Input: [-10,-5,3,4,7,9]
        Output: -1
        Explanation:
        There is no such i that A[i] = i, thus the output is -1.


        Note:

        1 <= A.length < 10^4
        -10^9 <= A[i] <= 10^9

        Args:
            A(list[int]):

        Returns:
            int:

        """
        smallest_index = -1
        left, right = 0, len(A)-1
        while left <= right:
            middle = (left + right) // 2
            if A[middle] == middle:
                smallest_index = middle
                right = middle - 1
            elif A[middle] < middle:
                left = middle + 1
            else:
                right = middle - 1
        return smallest_index
    #         *
    # [-10,-5,0,3,7]
    # [  0, 1,2,3,4]