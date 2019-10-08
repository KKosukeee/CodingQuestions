"""
Solution for 931. Minimum Falling Path Sum
https://leetcode.com/problems/minimum-falling-path-sum/
"""

class Solution(object):
    """
    Runtime: 144 ms, faster than 10.56% of Python online submissions for Minimum Falling Path Sum.
    Memory Usage: 12.4 MB, less than 57.14% of Python online submissions for Minimum Falling Path Sum.
    """
    def top_down_dfs(self, A):
        """
        A top-down solution that runs in O(N^2) in time and space

        :type A: List[List[int]]
        :rtype: int
        """
        memo = {(len(A) - 1, j): A[-1][j] for j in range(len(A))}

        def dfs(i, j):
            if i == len(A) - 1:
                return A[i][j]
            if (i, j) in memo:
                return memo[(i, j)]
            min_path = min(dfs(i + 1, j + x) for x in [-1, 0, 1] if 0 <= j + x < len(A))
            memo[(i, j)] = min_path + A[i][j]
            return memo[(i, j)]

        min_path = float('inf')
        for j in range(len(A)):
            min_path = min(min_path, dfs(0, j))
        return min_path

    def bottom_up_dfs(self, A):
        """
        A bottom-up solution that runs in O(N^2) in time and O(1) in space

        :type A: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(A)):
            for j in range(len(A)):
                A[i][j] += min(A[i - 1][j + x] for x in [-1, 0, 1] if 0 <= j + x < len(A))
        return min(A[-1])

    def minFallingPathSum(self, A):
        """
        Given a square array of integers A, we want the minimum sum of a falling path through A.

        A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.



        Example 1:

        Input: [[1,2,3],[4,5,6],[7,8,9]]
        Output: 12
        Explanation:
        The possible falling paths are:
        [1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
        [2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
        [3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
        The falling path with the smallest sum is [1,4,7], so the answer is 12.



        Note:

        1 <= A.length == A[0].length <= 100
        -100 <= A[i][j] <= 100

        :type A: List[List[int]]
        :rtype: int
        """
        return self.bottom_up_dfs(A)

    """
    FAST
    * Analyse the first solution
    * Sub-problem
    * Turn the solution around

    1,2,3
    4,5,6
    7,8,9
    """