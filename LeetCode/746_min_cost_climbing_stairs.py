"""
Solution for 746. Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/
"""

class Solution(object):
    """
    Runtime: 44 ms, faster than 89.58% of Python3 online submissions for Min Cost Climbing Stairs.
    Memory Usage: 13.3 MB, less than 7.01% of Python3 online submissions for Min Cost Climbing
    Stairs.
    """
    def minCostClimbingStairs(self, cost):
        """
        On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

        Once you pay the cost, you can either climb one or two steps. You need to find minimum
        cost to reach the top of the floor, and you can either start from the step with index 0,
        or the step with index 1.

        Example 1:
        Input: cost = [10, 15, 20]
        Output: 15
        Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
        Example 2:
        Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        Output: 6
        Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
        Args:
            cost: list of integers to look for min cost climbing stairs

        Returns:
            int: a number from cost array which if you start from the number, you can reach to
                the goal in minimum cost
        """
        i = 2

        while i < len(cost):
            cost[i] = cost[i] + min(cost[i-2:i])
            i += 1
        return min(cost[-2:])
