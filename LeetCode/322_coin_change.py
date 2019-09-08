"""
Solution for 322. Coin Change
https://leetcode.com/problems/coin-change/
"""
from typing import List

class Solution:
    """
    Runtime: 1428 ms, faster than 45.76% of Python3 online submissions for Coin Change.
    Memory Usage: 13.8 MB, less than 30.56% of Python3 online submissions for Coin Change.
    """
    def top_down(self, coins: List[int], amount: int) -> int:
        """
        Top-down DP solution that runs in O(N*M) in time and space where N = len(coins) and M = amount

        Args:
            coins(list[int]):
            amount(int):

        Returns:
            int:

        """
        dp = {c: 1 for c in coins}

        def backtrack(target):
            if target == 0:
                return 0
            if target in dp:
                return dp[target]
            min_coin = float('inf')
            for coin in coins:
                if target - coin >= 0:
                    min_coin = min(min_coin, backtrack(target - coin) + 1)
            dp[target] = min_coin
            return dp[target]

        min_coin = backtrack(amount)
        return min_coin if min_coin != float('inf') else -1

    def bottom_up(self, coins: List[int], amount: int) -> int:
        """
        Bottom-up DP solution that runs in O(NM)

        Args:
            coins(list[int]):
            amount(int):

        Returns:
            int:

        """
        dp = [0] + [float('inf')] * (amount)
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1

        # {1,2,3}, 5
        #          *
        # [0,1,1,1,2,2]
        # 1+1+3 | 2+3 | 3+2

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

        Example 1:

        Input: coins = [1, 2, 5], amount = 11
        Output: 3
        Explanation: 11 = 5 + 5 + 1
        Example 2:

        Input: coins = [2], amount = 3
        Output: -1
        Note:
        You may assume that you have an infinite number of each kind of coin.

        Args:
            coins(list[int]):
            amount(int):

        Returns:
            int:

        """
        return self.bottom_up(coins, amount)

    # Backtracking: O(amount^len(coins))
    # Top-down DP : O(amount*len(coins))
    #