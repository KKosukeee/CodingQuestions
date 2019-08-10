"""
Solution for 1043. Partition Array for Maximum Sum
https://leetcode.com/problems/partition-array-for-maximum-sum/
"""
class Solution:
    """
    Runtime: 504 ms, faster than 59.59% of Python3 online submissions for Partition Array for Maximum Sum.
    Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Partition Array for Maximum Sum.
    """
    def maxSumAfterPartitioning(self, A, K):
        """
        Given an integer array A, you partition the array into (contiguous) subarrays of length at most K.  After partitioning, each subarray has their values changed to become the maximum value of that subarray.

        Return the largest sum of the given array after partitioning.



        Example 1:

        Input: A = [1,15,7,9,2,5,10], K = 3
        Output: 84
        Explanation: A becomes [15,15,15,9,10,10,10]


        Note:

        1 <= K <= A.length <= 500
        0 <= A[i] <= 10^6
        Args:
            A: list<int>
            K: int

        Returns:
            int:
        """
        n = len(A)
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            num = -1
            for j in range(1, min(i, K)+1):
                num = max(num, A[i-j])
                dp[i] = max(dp[i], dp[i-j]+num*j)
        return dp[n]