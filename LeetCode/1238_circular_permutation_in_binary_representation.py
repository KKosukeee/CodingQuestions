"""
Solution for 1238. Circular Permutation in Binary Representation
https://leetcode.com/problems/circular-permutation-in-binary-representation/
"""
from typing import List

class Solution:
    """
    Runtime: 236 ms, faster than 72.13% of Python3 online submissions for Circular Permutation in Binary Representation.
    Memory Usage: 21.5 MB, less than 100.00% of Python3 online submissions for Circular Permutation in Binary Representation.
    """
    def brute_force(self, n: int, start: int) -> List[int]:
        """
        A brute force solution that runs O(2^n*n) in time and O(2^n) in space

        Args:
            n:
            start:

        Returns:

        """
        def backtracking(permu, used):
            if len(used) == 2 ** n:
                if permu[0] in self.adjacents(permu[-1], n):
                    return permu
                return []
            for adjacent in self.adjacents(permu[-1], n):
                if adjacent not in used:
                    cand = backtracking(permu + [adjacent],
                                        used.union(set([adjacent])))
                    if cand: return cand

        return backtracking([start], set([start]))

    def adjacents(self, bit, n):
        """
        A helper function

        Args:
            bit:
            n:

        Returns:

        """
        s = bin(bit)[2:].zfill(n)
        return [int(s[:i] + '1' + s[i + 1:], 2) if s[i] == '0' else
                int(s[:i] + '0' + s[i + 1:], 2) for i in range(n)]

    def gray_code(self, n: int, start: int) -> List[int]:
        """
        The best solution using gray code that runs in O(2^n) in time and space

        Args:
            n:
            start:

        Returns:

        """
        array = list(map(lambda x: x ^ (x >> 1), range(0, 2 ** n)))
        index = array.index(start)
        return array[index:] + array[:index]

    def circularPermutation(self, n: int, start: int) -> List[int]:
        """
        Given 2 integers n and start. Your task is return any permutation p of (0,1,2.....,2^n -1) such that :

        p[0] = start
        p[i] and p[i+1] differ by only one bit in their binary representation.
        p[0] and p[2^n -1] must also differ by only one bit in their binary representation.


        Example 1:

        Input: n = 2, start = 3
        Output: [3,2,0,1]
        Explanation: The binary representation of the permutation is (11,10,00,01).
        All the adjacent element differ by one bit. Another valid permutation is [3,1,0,2]
        Example 2:

        Input: n = 3, start = 2
        Output: [2,6,7,5,4,0,1,3]
        Explanation: The binary representation of the permutation is (010,110,111,101,100,000,001,011).


        Constraints:

        1 <= n <= 16
        0 <= start < 2 ^ n

        Args:
            n:
            start:

        Returns:

        """
        return self.gray_code(n, start)

    """
    Backtracking
    T: O(N^log(N)), S: O(N), N = N^2-1
    1. Create gray code for each num up to N^2-1
    2. Starting from the start, get all bits that are one bit far
    3. Keep record of bits that are used
    4. When there is no bit that is one far from the current, do nothing
    5. When there is no bit AND len(used) == N^2-1 AND the current bit is one far from the start, new permu!
    """