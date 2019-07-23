"""
Solution for 813. Largest Sum of Averages
https://leetcode.com/problems/largest-sum-of-averages/
"""
class Solution:
    """
    Runtime: 592 ms, faster than 18.69% of Python3 online submissions for Largest Sum of Averages.
    Memory Usage: 13.9 MB, less than 29.12% of Python3 online submissions for Largest Sum of Averages.
    """
    def largestSumOfAverages(self, A, K):
        """
        We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

        Note that our partition must use every number in A, and that scores are not necessarily integers.

        Example:
        Input:
        A = [9,1,2,3,9]
        K = 3
        Output: 20
        Explanation:
        The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
        We could have also partitioned A into [9, 1], [2], [3, 9], for example.
        That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
        Args:
            A: list<int> to look for the largest sum of averages
            K: int value representing the partition

        Returns:
            int: representing the largest average
        """
        cum_sum = [0]
        for v in A:
            cum_sum.append(cum_sum[-1] + v)

        def average(i, j):
            return (cum_sum[j] - cum_sum[i]) / float(j - i)

        N = len(A)
        dp = [average(i, N) for i in range(N)]

        for k in range(K - 1):
            for i in range(N):
                for j in range(i + 1, N):
                    dp[i] = max(dp[i], dp[j] + average(i, j))

        return dp[0]
