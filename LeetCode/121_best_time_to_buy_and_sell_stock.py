"""
Solution for 121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

class Solution:
    """
    Runtime: 32 ms, faster than 99.29% of Python3 online submissions for Best Time to Buy and Sell
        Stock.
    Memory Usage: 14 MB, less than 46.05% of Python3 online submissions for Best Time to Buy and
        Sell Stock.
    """
    def maxProfit(self, prices):
        """
        Say you have an array for which the ith element is the price of a given stock on day i.

        If you were only permitted to complete at most one transaction (i.e., buy one and sell one
        share of the stock), design an algorithm to find the maximum profit.

        Note that you cannot sell a stock before you buy one.

        Example 1:

        Input: [7,1,5,3,6,4]
        Output: 5
        Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                     Not 7-1 = 6, as selling price needs to be larger than buying price.
        Example 2:

        Input: [7,6,4,3,1]
        Output: 0
        Explanation: In this case, no transaction is done, i.e. max profit = 0.
        Args:
            prices: list of integers to find the maximum profit by selling a stock

        Returns:
            int: representing the maximum profit of selling the stock
        """
        if len(prices) < 2:
            return 0

        maximum_price = prices[-1]
        maximum_profit = 0

        for price in reversed(prices[:-1]):
            if price < maximum_price:
                maximum_profit = max(maximum_profit, maximum_price - price)
            else:
                maximum_price = price

        return maximum_profit
