"""
Solution for 896. Monotonic Array
https://leetcode.com/problems/monotonic-array/
"""

class Solution(object):
    """
    Runtime: 440 ms, faster than 80.00% of Python online submissions for Monotonic Array.
    Memory Usage: 17.1 MB, less than 27.27% of Python online submissions for Monotonic Array.
    """
    def two_pass(self, A):
        """
        A two-pass solution that runs in O(N) in space and time

        :type A: List[int]
        :rtype: bool
        """
        return all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or all(
            A[i] >= A[i + 1] for i in range(len(A) - 1))

    def one_pass(self, A):
        """
        A one-pass solution that runs in O(N) in space and time

        :type A: List[int]
        :rtype: bool
        """
        comp = 0
        for i in range(len(A) - 1):
            if A[i] != A[i + 1]:
                c = -1 if A[i] < A[i + 1] else 1
                if comp and comp != c:
                    return False
                comp = c
        return True

    def isMonotonic(self, A):
        """
        An array is monotonic if it is either monotone increasing or monotone decreasing.

        An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

        Return true if and only if the given array A is monotonic.



        Example 1:

        Input: [1,2,2,3]
        Output: true
        Example 2:

        Input: [6,5,4,4]
        Output: true
        Example 3:

        Input: [1,3,2]
        Output: false
        Example 4:

        Input: [1,2,4,5]
        Output: true
        Example 5:

        Input: [1,1,1]
        Output: true


        Note:

        1 <= A.length <= 50000
        -100000 <= A[i] <= 100000

        :type A: List[int]
        :rtype: bool
        """
        return self.one_pass(A)