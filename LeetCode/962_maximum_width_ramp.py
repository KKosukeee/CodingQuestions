"""
Solution for 962. Maximum Width Ramp
https://leetcode.com/problems/maximum-width-ramp/
"""
import bisect
from typing import List

class Solution:
    """
    Runtime: 340 ms, faster than 89.50% of Python3 online submissions for Maximum Width Ramp.
    Memory Usage: 20.7 MB, less than 100.00% of Python3 online submissions for Maximum Width Ramp.
    """
    def dp(self, A: List[int]) -> int:
        """
        A dp solution that runs in O(N^2) in time and O(N) in space

        Args:
            A:

        Returns:

        """
        dp = {}

        def rec(i):
            if i in dp:
                return dp[i]
            max_width = 0
            for j in range(i + 1, len(A)):
                if A[j] >= A[i]:
                    max_width = max(max_width, rec(j) + j - i)
            dp[i] = max_width
            return dp[i]

        return max(rec(i) for i in range(len(A)))

    def sort_solution(self, A: List[int]) -> int:
        """
        Sorting solution that runs in O(Nlog(N)) in time and O(1) in space

        Args:
            A:

        Returns:

        """
        max_width, min_prev = 0, float('inf')
        for i in sorted(range(len(A)), key=lambda x: A[x]):
            max_width = max(max_width, i - min_prev)
            min_prev = min(min_prev, i)
        return max_width

    def decreasing_stack(self, A: List[int]) -> int:
        """
        Stack solution that runs in O(Nlog(N)) in time and O(N) in space

        Args:
            A:

        Returns:

        """
        max_width, stack = 0, []
        for i in reversed(range(len(A))):
            if not stack or A[i] > stack[-1][0]:
                stack.append((A[i], i))
            else:
                j = stack[bisect.bisect(stack, (A[i], i))][1]
                max_width = max(max_width, j - i)
        return max_width

    def linear_solution(self, A: List[int]) -> int:
        """
        A linear solution that runs in O(N) in time and O(N) in space

        Args:
            A:

        Returns:

        """
        s = []
        for i in range(len(A)):
            if not s or A[s[-1]] > A[i]:
                s.append(i)
        max_width = 0
        for j in reversed(range(len(A))):
            while s and A[s[-1]] <= A[j]:
                max_width = max(max_width, j - s.pop())
        return max_width

    def maxWidthRamp(self, A: List[int]) -> int:
        """
        Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.

        Find the maximum width of a ramp in A.  If one doesn't exist, return 0.



        Example 1:

        Input: [6,0,8,2,1,5]
        Output: 4
        Explanation:
        The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
        Example 2:

        Input: [9,8,1,0,1,9,4,0,4,1]
        Output: 7
        Explanation:
        The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.


        Note:

        2 <= A.length <= 50000
        0 <= A[i] <= 50000Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.

        Find the maximum width of a ramp in A.  If one doesn't exist, return 0.



        Example 1:

        Input: [6,0,8,2,1,5]
        Output: 4
        Explanation:
        The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
        Example 2:

        Input: [9,8,1,0,1,9,4,0,4,1]
        Output: 7
        Explanation:
        The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.


        Note:

        2 <= A.length <= 50000
        0 <= A[i] <= 50000

        Args:
            A:

        Returns:

        """
        return self.linear_solution(A)

    """
    DP solution
    T: O(N^2), S: O(N)
    Base case
    1. If i exists in dp array, then return the val
    Recursive case
    1. Find an index j that is j > i and nums[j] >= num[i]
    2. Call the recusive function on j, then add the reutrning value plus j - i
    3. Store the value in the dp array, then return it

    Sort algorithm
    T: O(Nlog(N)), S: O(1)
    1. Loop through the array in sorted via value
        1.1 Given i, find the minimum indices that are seen
        1.2 Update the maximum width
    2. Return the width

    Decreasing stack
    T: O(Nlog(N)), S: O(N)
    1. Loop through the array in back order
        1.1 If the current element i is larger than the peek value, append it
        1.2 If 1.1 doesn't meet, find the farest value that is max(i..j), A[j] >= A[i]
        1.3 Update the maximum width
    2. Return the max_width

    Linear solution
    T: O(N), S: O(N)
    1. Loop through array
        1.1 If not stack, or the peek value being larger than the current, append the index i
    2. Loop through the array in back order
        2.1 Loop while the peek value is less than or equal to the current element A[j]
            2.1.1 Update the max_width after popping the index value
    """

