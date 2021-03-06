"""
Solution for 905. Sort Array By Parity
https://leetcode.com/problems/sort-array-by-parity/
"""

class Solution:
    """
    Runtime: 68 ms, faster than 88.16% of Python3 online submissions for Sort Array By Parity.
    Memory Usage: 13.9 MB, less than 15.18% of Python3 online submissions for Sort Array By Parity.
    """
    def two_pointer(self, A):
        """
        Solves the problem with two pointer approach. At the worst time, the runtime would be O(2N)
        Args:
            A: list of integers where we sort by the parity

        Returns:
            list<int>: where A is sorted in parity
        """
        i, j = 0, 0
        while j < len(A) and i < len(A):
            if A[j] % 2 == 0:
                while i < len(A) and i < j and A[i] % 2 == 0:
                    i += 1

                A[i], A[j] = A[j], A[i]

            j += 1
        return A

    def quick_sort(self, A):
        """
        Does in the similar way as the quick sort does. In the worst, it will be O(N)
        Args:
            A: list of integers where we sort by the parity

        Returns:
            list<int>: where A is sorted in parity
        """
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 != 0 and A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0:
                i += 1

            if A[j] % 2 != 0:
                j -= 1

        return A

    def sortArrayByParity(self, A):
        """
        Given an array A of non-negative integers, return an array consisting of all the even
        elements of A, followed by all the odd elements of A.

        You may return any answer array that satisfies this condition.



        Example 1:

        Input: [3,1,2,4]
        Output: [2,4,3,1]
        The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
        Args:
            A: list of integers where we sort by the parity

        Returns:
            list<int>: where A is sorted in parity
        """
        return self.quick_sort(A)
