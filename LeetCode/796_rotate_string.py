"""
Solution for 796. Rotate String
https://leetcode.com/problems/rotate-string/
"""
from collections import defaultdict

class Solution:
    """
    Runtime: 32 ms, faster than 90.81% of Python3 online submissions for Rotate String.
    Memory Usage: 13.7 MB, less than 5.26% of Python3 online submissions for Rotate String.
    """
    def rotateString(self, A: str, B: str) -> bool:
        """
        We are given two strings, A and B.

        A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

        Example 1:
        Input: A = 'abcde', B = 'cdeab'
        Output: true

        Example 2:
        Input: A = 'abcde', B = 'abced'
        Output: false
        Note:

        A and B will have length at most 100.

        Args:
            A:
            B:

        Returns:

        """
        if not A and not B:
            return True
        if not A or not B:
            return False
        if len(A) != len(B):
            return False
        indices = defaultdict(list)
        for i in range(len(A)):
            indices[A[i]].append(i)
        for offset in indices[B[0]]:
            i, j = 0, 0
            while i < len(A) and j < len(B) and A[(offset + i) % len(A)] == B[j]:
                i, j = i+1, j+1
            if j == len(B):
                return True
        return False
    """
    First solution
    1. Try to find all indices of B[0]
    2. Loop through the A starting from the inds[B[0]]
        2.1 Continue the loop whiel A[start+i] == B[j]
    3. Return True if there is any pair, otherwise false
    """
