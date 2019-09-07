"""
Solution for 198. House Robber
https://leetcode.com/problems/house-robber/
"""
from typing import List

class Solution:
    """
    Runtime: 36 ms, faster than 80.68% of Python3 online submissions for House Robber.
    Memory Usage: 13.7 MB, less than 9.09% of Python3 online submissions for House Robber.
    """
    def dp(self, nums: List[int]) -> int:
        """
        Solving the question via DP. The runtime is O(N) where N is len(nums) and the space is O(N)
        too

        Args:
            nums(list[int]):

        Returns:
            int:

        """
        if not nums:
            return 0
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        for i in range(1, len(nums)):
            dp[i + 1] = max(dp[i - 1] + nums[i], dp[i])
        return max(dp[-1], dp[-2])

    def constant(self, nums: List[int]) -> int:
        """
        Similar to the dp solution, but it uses constant space.

        Args:
            nums(list[int]):

        Returns:
            int:

        """
        if not nums:
            return 0
        prev, curr = 0, nums[0]
        for i in range(1, len(nums)):
            new_value = max(prev + nums[i], curr)
            prev = curr
            curr = new_value
        return max(prev, curr)

    def rob(self, nums: List[int]) -> int:
        """
        You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

        Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

        Example 1:

        Input: [1,2,3,1]
        Output: 4
        Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
                     Total amount you can rob = 1 + 3 = 4.
        Example 2:

        Input: [2,7,9,3,1]
        Output: 12
        Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
                     Total amount you can rob = 2 + 9 + 1 = 12.

        Args:
            nums(list[int]):

        Returns:
            int:

        """
        return self.constant(nums)

    # [1,2]
    #        *
    #   [1,2,3,1]
    # [0,1,2,4,1]
    #          *
    #   [2,1,1,2]
    # [0,2,2,3,4]
    # max(arr[i-2]+cur, arr[i-1])
    # 0->2->3->1->3->2
    