"""
Solution for 494. Target Sum
https://leetcode.com/problems/target-sum/
"""
from collections import defaultdict
from typing import List

class Solution:
    """
    Runtime: 216 ms, faster than 72.39% of Python3 online submissions for Target Sum.
    Memory Usage: 13.9 MB, less than 58.33% of Python3 online submissions for Target Sum.
    """
    def brute_force(self, nums: List[int], S: int) -> int:
        """
        Brute force that runs in O(2^(N)) where N = len(nums)

        Args:
            nums(list[int]):
            S(int):

        Returns:
            int:

        """
        def dfs(curr, s):
            """
            DFS

            Args:
                curr(int):
                s(int):

            Returns:
                int:

            """
            if curr >= len(nums):
                return 1 if s == 0 else 0
            return dfs(curr + 1, s - nums[curr]) + dfs(curr + 1, s + nums[curr])

        return dfs(0, S)

    def top_down(self, nums: List[int], S: int) -> int:
        """
        Top-down DP approach that runs in O(NS)

        Args:
            nums(list[int]):
            S(int):

        Returns:
            int:

        """
        dp = defaultdict(lambda: defaultdict(dict))

        def dfs(curr, s):
            """
            DFS

            Args:
                curr(int):
                s(int):

            Returns:
                int:

            """
            if curr >= len(nums):
                return 1 if s == S else 0
            if curr in dp and s in dp[curr]:
                return dp[curr][s]
            dp[curr][s] = dfs(curr + 1, s - nums[curr]) + dfs(curr + 1, s + nums[curr])
            return dp[curr][s]

        return dfs(0, 0)

    def bottom_up(self, nums: List[int], S: int) -> int:
        """
        Bottom-up DP solution that runs in O(NS)

        Args:
            nums(list[int]):
            S(int):

        Returns:
            int:

        """
        dp = defaultdict(int)
        dp[nums[0]] += 1
        dp[-nums[0]] += 1
        for i in range(1, len(nums)):
            temp = defaultdict(int)
            for d in dp:
                temp[d + nums[i]] += dp[d]
                temp[d - nums[i]] += dp[d]
            dp = temp
        return dp[S]

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

        Find out how many ways to assign symbols to make sum of integers equal to target S.

        Example 1:
        Input: nums is [1, 1, 1, 1, 1], S is 3.
        Output: 5
        Explanation:

        -1+1+1+1+1 = 3
        +1-1+1+1+1 = 3
        +1+1-1+1+1 = 3
        +1+1+1-1+1 = 3
        +1+1+1+1-1 = 3

        There are 5 ways to assign symbols to make the sum of nums be target 3.
        Note:
        The length of the given array is positive and will not exceed 20.
        The sum of elements in the given array will not exceed 1000.
        Your output answer is guaranteed to be fitted in a 32-bit integer.

        Args:
            nums(list[int]):
            S(int):

        Returns:
            int:

        """
        return self.bottom_up(nums, S)

    #  *
    # [1,1,1,1,1], 3
    #