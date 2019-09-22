"""
Solution for 264. Ugly Number II
https://leetcode.com/problems/ugly-number-ii/
"""
import heapq

class Solution:
    """
    Runtime: 156 ms, faster than 77.31% of Python3 online submissions for Ugly Number II.
    Memory Usage: 13.9 MB, less than 20.00% of Python3 online submissions for Ugly Number II.
    """
    def brute_force(self, n: int) -> int:
        """
        Brute force solution that runs in O(n log(n))

        Args:
            n(int):

        Returns:
            int:

        """
        def max_divide(x, y):
            """
            Divide the x with y as long as possible

            Args:
                x(int):
                y(int):

            Returns:
                int:

            """
            while x % y == 0:
                x /= y
            return x

        x = 2
        current = 1
        while True:
            xx = max_divide(x, 2)
            xx = max_divide(xx, 3)
            xx = max_divide(xx, 5)
            if xx == 1:
                current += 1
            if current == n:
                break
            x += 1
        return int(x)

    def heap(self, n: int) -> int:
        """
        Solution using a heap that runs in O(n log(n))

        Args:
            n(int):

        Returns:
            int:

        """
        if n <= 1:
            return 1
        heap = [1]
        seen = set([1])
        nth = []
        for _ in range(n):
            popped = heapq.heappop(heap)
            if popped * 2 not in seen:
                heapq.heappush(heap, popped * 2)
            if popped * 3 not in seen:
                heapq.heappush(heap, popped * 3)
            if popped * 5 not in seen:
                heapq.heappush(heap, popped * 5)
            seen.update([popped * 2, popped * 3, popped * 5])
            nth.append(popped)
        return nth[n - 1]

    def dp(self, n: int) -> int:
        """
        DP solution that runs in O(n)

        Args:
            n(int):

        Returns:
            int:

        """
        nth = [1]
        i, j, k = 0, 0, 0
        for _ in range(1, n):
            min_ug = min(2 * nth[i], 3 * nth[j], 5 * nth[k])
            if min_ug == 2 * nth[i]:
                i += 1
            if min_ug == 3 * nth[j]:
                j += 1
            if min_ug == 5 * nth[k]:
                k += 1
            nth.append(min_ug)
        return nth[-1]

    def nthUglyNumber(self, n: int) -> int:
        """
        Write a program to find the n-th ugly number.

        Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

        Example:

        Input: n = 10
        Output: 12
        Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
        Note:

        1 is typically treated as an ugly number.
        n does not exceed 1690.

        Args:
            n(int):

        Returns:
            int:

        """
        return self.dp(n)

    # 1 2 3 4 5 6 8

    # ugly = 2 * {2,3,5} -> ugly
    # ugly = 3 * {2,3,5} -> ugly
    # ugly = n * {2,3,5} -> ugly
    # * * * * * * * * *  *
    # 1,2,3,4,5,6,8,9,10,12...
    # L1 = [2,4,6,8,10,12...]
    # L2 = [3,6,9,12...]
    # L3 = [5,10...]
