"""
Solution for 1052. Grumpy Bookstore Owner
https://leetcode.com/problems/grumpy-bookstore-owner/
"""

class Solution:
    """
    Runtime: 336 ms, faster than 8.41% of Python3 online submissions for Grumpy Bookstore Owner.
    Memory Usage: 15.8 MB, less than 100.00% of Python3 online submissions for Grumpy Bookstore Owner.
    """
    def maxSatisfied(self, customers, grumpy, X):
        """
        Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.

        On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

        The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.

        Return the maximum number of customers that can be satisfied throughout the day.



        Example 1:

        Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
        Output: 16
        Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
        The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
        Args:
            customers: list<int> as the profit you can get from the cusomter
            grumpy: list<int> as the grumpy owner's temper
            X: size of the window

        Returns:
            int: as the max profit you can get with all inputs
        """
        secret = 0
        profit = 0

        for i in range(X):
            profit += customers[i] * (1 - grumpy[i])
            secret += customers[i] * grumpy[i]

        max_secret = secret
        for i in range(len(customers) - X):
            profit += customers[i + X] * (1 - grumpy[i + X])
            secret += customers[i + X] * grumpy[i + X]
            secret -= customers[i] * grumpy[i]
            max_secret = max(secret, max_secret)

        return profit + max_secret
