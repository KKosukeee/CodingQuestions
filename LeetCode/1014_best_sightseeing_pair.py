"""
Solution for 1014. Best Sightseeing Pair
"""

class Solution:
    """
    Runtime: 168 ms, faster than 52.75% of Python3 online submissions for Best Sightseeing Pair.
    Memory Usage: 16.7 MB, less than 95.88% of Python3 online submissions for Best Sightseeing Pair.
    """
    def maxScoreSightseeingPair(self, A):
        """
        Given an array A of positive integers, A[i] represents the value of the i-th sightseeing
        spot, and two sightseeing spots i and j have distance j - i between them.

        The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the sum of the
        values of the sightseeing spots, minus the distance between them.

        Return the maximum score of a pair of sightseeing spots.



        Example 1:

        Input: [8,1,5,2,6]
        Output: 11
        Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
        Args:
            A: list of integers as the point for each sightseeing spot

        Returns:
            int: as the maximum score that you can get
        """
        max_score = 0
        ith_value = A[0]

        for i in range(1, len(A)):
            max_score = max(max_score, ith_value + A[i] - i)
            ith_value = max(ith_value, A[i] + i)

        return max_score
