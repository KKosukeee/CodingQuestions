"""
Solution for 795. Number of Subarrays with Bounded Maximum
https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/
"""
from typing import List

class Solution:
    """
    Runtime: 388 ms, faster than 71.82% of Python3 online submissions for Number of Subarrays with Bounded Maximum.
    Memory Usage: 15.2 MB, less than 14.29% of Python3 online submissions for Number of Subarrays with Bounded Maximum.
    """
    def dp(self, A: List[int], L: int, R: int) -> int:
        """
        DP solution that runs in O(N) and O(N) in runtime and space respectively

        Args:
            A(list[int]):
            L(int):
            R(int):

        Returns:
            int:

        """
        dp = [0] * (len(A) + 1)
        last_invalid = -1
        for i in range(len(A)):
            # Maximum subarray ending at i is the previous max
            if A[i] < L:
                dp[i + 1] = dp[i]
            # Maximum subarray ending at i doesn't exist.
            elif A[i] > R:
                last_invalid = i
            # Maximum subarray extends to i, increment current the diff to the result
            else:
                dp[i + 1] = i - last_invalid
        return sum(dp)

    def constant(self, A: List[int], L: int, R: int) -> int:
        """
        DP solution that runs in O(N) and O(1)

        Args:
            A(list[int]):
            L(int):
            R(int):

        Returns:
            int:

        """
        i, so_far, count = -1, 0, 0
        for j in range(len(A)):
            if A[j] < L:
                count += so_far
            elif A[j] > R:
                i = j
                so_far = 0
            else:
                so_far = j - i
                count += so_far
        return count

    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        """
        We are given an array A of positive integers, and two positive integers L and R (L <= R).

        Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.

        Example :
        Input:
        A = [2, 1, 4, 3]
        L = 2
        R = 3
        Output: 3
        Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
        Note:

        L, R  and A[i] will be an integer in the range [0, 10^9].
        The length of A will be in the range of [1, 50000].

        Args:
            A(list[int]):
            L(int):
            R(int):

        Returns:
            int:

        """
        return self.constant(A, L, R)

    #           *        *
    #    [2, 1, 4, 3, 1, 3]
    # [0, 1, 1, 0, 1, 1, 3]
    #    [2]
    #    [2, 1]
    #             [3]
    #             [3, 1]
    #             [3, 1, 3]
    #                [1, 3]
    #                   [3]
    #           *        *
    #    [2, 1, 4, 2, 3, 1]
    # [0, 1, 1, 0, 1, 2, 2]
    #
    # [2]
    # [2, 1]
    # [2, 1, 4] ->  [1, 4]
    # [2, 1, 4, 3]
    #    [1]
    #    [1, 4] ->  [1, 4]
    #    [1, 4, 3]
    #       [4]
    #       [4, 3]
    #          [3]