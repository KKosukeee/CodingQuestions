"""
Solution for 930. Binary Subarrays With Sum
https://leetcode.com/problems/binary-subarrays-with-sum/
"""
from collections import defaultdict

class Solution:
    """
    Runtime: 336 ms, faster than 37.09% of Python3 online submissions for Binary Subarrays With Sum.
    Memory Usage: 18.3 MB, less than 25.00% of Python3 online submissions for Binary Subarrays With Sum.
    """
    def numSubarraysWithSum(self, A, S):
        """
        In an array A of 0s and 1s, how many non-empty subarrays have sum S?



        Example 1:

        Input: A = [1,0,1,0,1], S = 2
        Output: 4
        Explanation:
        The 4 subarrays are bolded below:
        [1,0,1,0,1]
        [1,0,1,0,1]
        [1,0,1,0,1]
        [1,0,1,0,1]


        Note:

        A.length <= 30000
        0 <= S <= A.length
        A[i] is either 0 or 1.

        Args:
            A(list[int]):
            S(int):

        Returns:
            int:

        """
        cum_sum = [0]
        counter = defaultdict(int)
        for i in range(len(A)):
            cum_sum.append(cum_sum[-1]+A[i])
        count = 0
        for i in range(len(cum_sum)):
            count += counter[cum_sum[i]]
            counter[cum_sum[i]+S] += 1
        return count
