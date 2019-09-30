"""
Solution for 779. K-th Symbol in Grammar
https://leetcode.com/problems/k-th-symbol-in-grammar/
"""

class Solution(object):
    """
    Runtime: 16 ms, faster than 70.34% of Python online submissions for K-th Symbol in Grammar.
    Memory Usage: 12 MB, less than 33.33% of Python online submissions for K-th Symbol in Grammar.
    """
    def initial_solution(self, N, K):
        """
        An initial solution that runs out in TLE but the concept is the correct one

        :type N: int
        :type K: int
        :rtype: int
        """

        def binary(n):
            if n == 1:
                return '0'
            b = binary(n - 1)
            return b + ''.join(['1' if char == '0' else '0' for char in b])

        return binary(N)[K - 1]

    def second_solution(self, N, K):
        """
        The second solution from the solution page that applies the bit manipulation technique so
        that the initial solution runs in linear time

        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1:
            return 0
        # Left half
        if K <= (2 ** (N - 2)):
            return self.second_solution(N - 1, K)
        # Right half
        return self.second_solution(N - 1, K - 2 ** (N - 2)) ^ 1

    def kthGrammar(self, N, K):
        """
        On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

        Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

        Examples:
        Input: N = 1, K = 1
        Output: 0

        Input: N = 2, K = 1
        Output: 0

        Input: N = 2, K = 2
        Output: 1

        Input: N = 4, K = 5
        Output: 1

        Explanation:
        row 1: 0
        row 2: 01
        row 3: 0110
        row 4: 01101001
        Note:

        N will be an integer in the range [1, 30].
        K will be an integer in the range [1, 2^(N-1)].

        :type N: int
        :type K: int
        :rtype: int
        """
        return self.second_solution(N, K)

    """
    0
    01
    0110
    01101001
    0110100110010110
    01101001100101101001011001101001
    0110100110010110100101100110100110010110011010010110100110010110
    """