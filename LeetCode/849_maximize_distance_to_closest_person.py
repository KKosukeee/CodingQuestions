"""
Solution for 849. Maximize Distance to Closest Person
https://leetcode.com/problems/maximize-distance-to-closest-person/
"""

class Solution:
    """
    Runtime: 60 ms, faster than 51.55% of Python3 online submissions for Maximize Distance to
        Closest Person.
    Memory Usage: 13.5 MB, less than 60.00% of Python3 online submissions for Maximize Distance to
        Closest Person.
    """
    def maxDistToClosest(self, seats):
        """
        In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the
        seat is empty.

        There is at least one empty seat, and at least one person sitting.

        Alex wants to sit in the seat such that the distance between him and the closest person to
        him is maximized.

        Return that maximum distance to closest person.

        Example 1:

        Input: [1,0,0,0,1,0,1]
        Output: 2
        Explanation:
        If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
        If Alex sits in any other open seat, the closest person has distance 1.
        Thus, the maximum distance to the closest person is 2.
        Example 2:

        Input: [1,0,0,0]
        Output: 3
        Explanation:
        If Alex sits in the last seat, the closest person is 3 seats away.
        This is the maximum distance possible, so the answer is 3.
        Args:
            seats: list of integers where the values are either 0 or 1

        Returns:
            int: maximum distance the person can take as the distance
        """
        i, j = 0, 1
        n = len(seats)

        while i < n and seats[i] != 1:
            i += 1

        dist = i
        j = i + 1

        while i < n:
            while j < n and seats[j] != 1:
                j += 1

            if j < n:
                dist = max(dist, min(abs(i - (i + j) // 2), abs(j - (i + j) // 2)))
            else:
                dist = max(dist, j - 1 - i)

            i = j
            j += 1

        return dist
