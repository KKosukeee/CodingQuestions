"""
Solution for 1154. Day of the Year
https://leetcode.com/problems/ordinal-number-of-date/
"""

class Solution:
    """
    Runtime: 36 ms, faster than 100.00% of Python3 online submissions for Day of the Year.
    Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Day of the Year.
    """
    def dayOfYear(self, date):
        """
        Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.



        Example 1:

        Input: date = "2019-01-09"
        Output: 9
        Explanation: Given date is the 9th day of the year in 2019.
        Example 2:

        Input: date = "2019-02-10"
        Output: 41
        Example 3:

        Input: date = "2003-03-01"
        Output: 60
        Example 4:

        Input: date = "2004-03-01"
        Output: 61


        Constraints:

        date.length == 10
        date[4] == date[7] == '-', and all other date[i]'s are digits
        date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
        Args:
            date(str): str value

        Returns:
            int: int
        """
        date_by_year = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        year, month, date = [int(x) for x in date.split('-')]
        dates = 0

        if self.is_leap(year):
            date_by_year[2] += 1

        for key in range(1, month):
            dates += date_by_year[key]
        return dates + date

    def is_leap(self, year):
        """
        is it leap year?
        Args:
            year(int): int value

        Returns:
            bool: True or False
        """
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
            else:
                return True
        return False
