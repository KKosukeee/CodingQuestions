"""
Solution for 1176. Diet Plan Performance
https://leetcode.com/problems/diet-plan-performance/
"""

class Solution:
    """
    Runtime: 236 ms, faster than 100.00% of Python3 online submissions for Diet Plan Performance.
    Memory Usage: 23.5 MB, less than 100.00% of Python3 online submissions for Diet Plan Performance.
    """
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        A dieter consumes calories[i] calories on the i-th day.  For every consecutive sequence of k days, they look at T, the total calories consumed during that sequence of k days:

        If T < lower, they performed poorly on their diet and lose 1 point;
        If T > upper, they performed well on their diet and gain 1 point;
        Otherwise, they performed normally and there is no change in points.
        Return the total number of points the dieter has after all calories.length days.

        Note that: The total points could be negative.



        Example 1:

        Input: calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3
        Output: 0
        Explaination: calories[0], calories[1] < lower and calories[3], calories[4] > upper, total points = 0.
        Example 2:

        Input: calories = [3,2], k = 2, lower = 0, upper = 1
        Output: 1
        Explaination: calories[0] + calories[1] > upper, total points = 1.
        Example 3:

        Input: calories = [6,5,0,0], k = 2, lower = 1, upper = 5
        Output: 0
        Explaination: calories[0] + calories[1] > upper, calories[2] + calories[3] < lower, total points = 0.


        Constraints:

        1 <= k <= calories.length <= 10^5
        0 <= calories[i] <= 20000
        0 <= lower <= upper

        Args:
            calories(list[int]):
            k(int):
            lower(int):
            upper(int):

        Returns:
            None:

        """
        current_sum = sum(calories[:k])
        point = (current_sum > upper) - (current_sum < lower)
        for i in range(len(calories) - k):
            current_sum += calories[i + k] - calories[i]
            point += (current_sum > upper) - (current_sum < lower)
        return point

#   [6,13,8,7,10,1,12,11]
#                   *
# [0,6,19,27,34,44,45,57,68]