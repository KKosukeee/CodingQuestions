"""
Solution for 1109. Corporate Flight Bookings
https://leetcode.com/problems/corporate-flight-bookings/
"""

class Solution:
    def corpFlightBookings(self, bookings, n):
        """
        There are n flights, and they are labeled from 1 to n.

        We have a list of flight bookings.  The i-th booking bookings[i] = [i, j, k] means that we booked k seats from flights labeled i to j inclusive.

        Return an array answer of length n, representing the number of seats booked on each flight in order of their label.



        Example 1:

        Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
        Output: [10,55,45,25,25]


        Constraints:

        1 <= bookings.length <= 20000
        1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
        1 <= bookings[i][2] <= 10000
        Args:
            bookings(list[list[int]]):
            n(int):

        Returns:
            list[int]:

        """
        result = [0] * (n+1)
        for start, end, seat in bookings:
            result[start-1] += seat
            result[end] -= seat
        for i in range(1, n):
            result[i] += result[i-1]
        return result[:-1]
