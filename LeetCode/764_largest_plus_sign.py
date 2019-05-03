"""
Solution for 764. Largest Plus Sign
https://leetcode.com/problems/largest-plus-sign/
"""

class Solution:
    """
    Runtime: 1680 ms, faster than 86.34% of Python3 online submissions for Largest Plus Sign.
    Memory Usage: 16.4 MB, less than 46.15% of Python3 online submissions for Largest Plus Sign.
    """
    def orderOfLargestPlusSign(self, N, mines):
        """
        In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the
        given list mines which are 0. What is the largest axis-aligned plus sign of 1s contained
        in the grid? Return the order of the plus sign. If there is none, return 0.

        An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4
        arms of length k-1 going up, down, left, and right, and made of 1s. This is demonstrated
        in the diagrams below. Note that there could be 0s or 1s beyond the arms of the plus sign,
        only the relevant area of the plus sign is checked for 1s.

        Examples of Axis-Aligned Plus Signs of Order k:

        Order 1:
        000
        010
        000

        Order 2:
        00000
        00100
        01110
        00100
        00000

        Order 3:
        0000000
        0001000
        0001000
        0111110
        0001000
        0001000
        0000000
        Example 1:

        Input: N = 5, mines = [[4, 2]]
        Output: 2
        Explanation:
        11111
        11111
        11111
        11111
        11011
        In the above grid, the largest plus sign can only be order 2.  One of them is marked in
        bold.
        Example 2:

        Input: N = 2, mines = []
        Output: 1
        Explanation:
        There is no plus sign of order 2, but there is of order 1.
        Example 3:

        Input: N = 1, mines = [[0, 0]]
        Output: 0
        Explanation:
        There is no plus sign, so return 0.
        Args:
            N: length of a square
            mines: list of list of integers indicating where zero values are

        Returns:
            int: maximum order of plus sign in the square
        """
        # create set object for constant lookup
        banned = {tuple(mine) for mine in mines}

        # initalize dp array with same size as the matrix
        dp = [[0] * N for _ in range(N)]
        ans = 0

        # loop horizontaly first
        for r in range(N):
            count = 0

            # update dp array for left direction
            for c in range(N):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = count

            count = 0

            # update dp array for right direction
            for c in range(N - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]: dp[r][c] = count

        # loop vertically
        for c in range(N):
            count = 0

            # update dp array with down direction
            for r in range(N):
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]: dp[r][c] = count

            count = 0

            # update dp array with up direction
            for r in range(N - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]: dp[r][c] = count
                if dp[r][c] > ans: ans = dp[r][c]

        return ans
