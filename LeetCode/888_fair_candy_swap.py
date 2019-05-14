"""
Solution for 888. Fair Candy Swap
https://leetcode.com/problems/fair-candy-swap/
"""

class Solution:
    """
    Runtime: 64 ms, faster than 97.72% of Python3 online submissions for Fair Candy Swap.
    Memory Usage: 15.1 MB, less than 5.05% of Python3 online submissions for Fair Candy Swap.
    """
    def fairCandySwap(self, A, B):
        """
        Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy
        that Alice has, and B[j] is the size of the j-th bar of candy that Bob has.

        Since they are friends, they would like to exchange one candy bar each so that after the
        exchange, they both have the same total amount of candy.  (The total amount of candy a
        person has is the sum of the sizes of candy bars they have.)

        Return an integer array ans where ans[0] is the size of the candy bar that Alice must
        exchange, and ans[1] is the size of the candy bar that Bob must exchange.

        If there are multiple answers, you may return any one of them.  It is guaranteed an answer
        exists.



        Example 1:

        Input: A = [1,1], B = [2,2]
        Output: [1,2]
        Example 2:

        Input: A = [1,2], B = [2,3]
        Output: [1,2]
        Example 3:

        Input: A = [2], B = [1,3]
        Output: [2,3]
        Example 4:

        Input: A = [1,2,5], B = [2,4]
        Output: [5,4]
        Args:
            A: Candies that Alice have initially
            B: Candies that Bob have initially
        Returns:
            list<int>: where the first element is the candy that Alice exchange and the second
                where the Bob exchange
        """
        sum_a, sum_b = sum(A), sum(B)
        set_b = set(B)

        for x in A:
            b_j = ((sum_b - sum_a) / 2) + x
            if b_j in set_b:
                return [x, int(b_j)]
