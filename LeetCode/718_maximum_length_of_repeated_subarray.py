"""
Solution for 718. Maximum Length of Repeated Subarray
https://leetcode.com/problems/maximum-length-of-repeated-subarray/
"""

class Solution:
    """
    Runtime: 2648 ms, faster than 76.33% of Python3 online submissions for Maximum Length of
        Repeated Subarray.
    Memory Usage: 38.3 MB, less than 66.49% of Python3 online submissions for Maximum Length of
        Repeated Subarray.
    """
    def findLength(self, A, B):
        """
        Given two integer arrays A and B, return the maximum length of an subarray that appears in
        both arrays.

        Example 1:

        Input:
        A: [1,2,3,2,1]
        B: [3,2,1,4,7]
        Output: 3
        Explanation:
        The repeated subarray with maximum length is [3, 2, 1].

        Args:
            A: list<int> to find common subarray from
            B: list<int> to find common subarray from

        Returns:
            int: the maximum length of the common array
        """
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1

        return max(max(row) for row in memo)
