"""
Solution for 983. Minimum Cost For Tickets
https://leetcode.com/problems/minimum-cost-for-tickets/
"""
import bisect
from functools import lru_cache
from typing import List

class Solution:
    """
    Runtime: 52 ms, faster than 59.29% of Python3 online submissions for Minimum Cost For Tickets.
    Memory Usage: 14.1 MB, less than 7.14% of Python3 online submissions for Minimum Cost For Tickets.
    """
    def top_down(self, days: List[int], costs: List[int]) -> int:
        """
        Top-down DP solution that runs in O(N) where N = len(days)

        Args:
            days(list[int]):
            costs(list[int]):

        Returns:
            int:

        """
        day_pass = {0: 0, 1: 6, 2: 29}

        @lru_cache(None)
        def recursion(current):
            if not current < len(days):
                return 0
            min_cost = float('inf')
            for i in range(len(costs)):
                min_cost = min(min_cost,
                               recursion(bisect.bisect(days, days[current] + day_pass[i])) + costs[
                                   i])
            return min_cost

        return recursion(0)

    def bottom_up(self, days: List[int], costs: List[int]) -> int:
        """
        Bottom-up solution that runs in O(N)

        Args:
            days(list[int]):
            costs(list[int]):

        Returns:
            int:

        """
        dp = [float('inf')] * len(days)
        dp[0] = min(costs)
        day_pass = {0: 1, 1: 7, 2: 30}
        for i in range(1, len(days)):
            for j in range(len(costs)):
                k = bisect.bisect(days, days[i] - day_pass[j]) - 1
                if k >= 0:
                    dp[i] = min(dp[i], dp[k] + costs[j])
                else:
                    dp[i] = min(dp[i], costs[j])
        return dp[-1]

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

        Train tickets are sold in 3 different ways:

        a 1-day pass is sold for costs[0] dollars;
        a 7-day pass is sold for costs[1] dollars;
        a 30-day pass is sold for costs[2] dollars.
        The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

        Return the minimum number of dollars you need to travel every day in the given list of days.



        Example 1:

        Input: days = [1,4,6,7,8,20], costs = [2,7,15]
        Output: 11
        Explanation:
        For example, here is one way to buy passes that lets you travel your travel plan:
        On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
        On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
        On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
        In total you spent $11 and covered all the days of your travel.
        Example 2:

        Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
        Output: 17
        Explanation:
        For example, here is one way to buy passes that lets you travel your travel plan:
        On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
        On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
        In total you spent $17 and covered all the days of your travel.


        Note:

        1 <= days.length <= 365
        1 <= days[i] <= 365
        days is in strictly increasing order.
        costs.length == 3
        1 <= costs[i] <= 1000

        Args:
            days(list[int]):
            costs(list[int]):

        Returns:
            int:

        """
        return self.top_down(days, costs)
