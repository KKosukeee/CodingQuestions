"""
Solution for 539. Minimum Time Difference
https://leetcode.com/problems/minimum-time-difference/
"""

class Solution:
    """
    Runtime: 68 ms, faster than 43.02% of Python3 online submissions for Minimum Time Difference.
    Memory Usage: 14.6 MB, less than 69.97% of Python3 online submissions for Minimum Time
        Difference.
    """
    def findMinDifference(self, timePoints):
        """
        Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum
        minutes difference between any two time points in the list.
        Example 1:
        Input: ["23:59","00:00"]
        Output: 1
        Args:
            timePoints: list of str where each element is representing a time

        Returns:
            int: representing the minimum distance
        """
        timePoints.sort()
        min_dif = 24 * 60

        for i in range(1, len(timePoints) + 1):
            first_time = self.convert(timePoints[i - 1])
            second_time = self.convert(timePoints[i % len(timePoints)])

            if i == len(timePoints):
                second_time += 24 * 60

            min_dif = min(min_dif, second_time - first_time)

        return min_dif

    def convert(self, time):
        """
        This function converts time string into a number representing seconds
        Args:
            time: str as the time string value

        Returns:
            int: representing the time in minutes
        """
        hour, minutes = time.split(':')
        return int(hour) * 60 + int(minutes)
