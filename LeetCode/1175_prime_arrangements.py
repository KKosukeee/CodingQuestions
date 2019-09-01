"""
Solution for 1175. Prime Arrangements
https://leetcode.com/problems/prime-arrangements/
"""
import math

class Solution:
    """
    Runtime: 28 ms, faster than 100.00% of Python3 online submissions for Prime Arrangements.
    Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Prime Arrangements.
    """
    def numPrimeArrangements(self, n):
        """
        Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

        (Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

        Since the answer may be large, return the answer modulo 10^9 + 7.



        Example 1:

        Input: n = 5
        Output: 12
        Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
        Example 2:

        Input: n = 100
        Output: 682289015


        Constraints:

        1 <= n <= 100

        Args:
            n(int):

        Returns:
            int:

        """
        is_prime = [True] * (n + 1)
        is_prime[0], is_prime[1] = False, False
        count = 0

        for i in range(2, n + 1):
            if not is_prime[i]:
                continue
            count += 1
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
        return math.factorial(count) * math.factorial(n - count) % (10 ** 9 + 7)
    # 1*2*3*4 1*2
    # P(N, R) = (N)! / (N-R)!