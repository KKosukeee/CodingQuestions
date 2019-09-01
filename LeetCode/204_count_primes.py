"""
Solution for 204. Count Primes
https://leetcode.com/problems/count-primes/
"""

class Solution:
    """
    Runtime: 488 ms, faster than 61.39% of Python3 online submissions for Count Primes.
    Memory Usage: 25.3 MB, less than 79.31% of Python3 online submissions for Count Primes.
    """
    def countPrimes(self, n):
        """
        Count the number of prime numbers less than a non-negative number, n.

        Example:

        Input: 10
        Output: 4
        Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

        Args:
            n(int):

        Returns:
            int:

        """
        if n < 2:
            return 0
        is_prime = [True] * n
        is_prime[0], is_prime[1] = False, False
        count = 0
        for i in range(2, n):
            if not is_prime[i]:
                continue
            count += 1
            for j in range(i * i, n, i):
                is_prime[j] = False
        return count
