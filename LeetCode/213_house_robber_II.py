"""
Solution for 213. House Robber II
https://leetcode.com/problems/house-robber-ii/
"""
from typing import List

class Solution:
    """
    Runtime: 36 ms, faster than 81.78% of Python3 online submissions for House Robber II.
    Memory Usage: 13.9 MB, less than 5.56% of Python3 online submissions for House Robber II.
    """
    def two_pass(self, nums: List[int]) -> int:
        """
        Solves a problem with two pass in O(N) and O(1) in runtime and space respectively

        Args:
            nums(list[int]):

        Returns:
            int:

        """
        def _rob(array):
            """
            DRY function

            Args:
                array(list[int]):

            Returns:
                int:

            """
            prev, curr = 0, array[0]
            for i in range(1, len(array)):
                new_value = max(prev + array[i], curr)
                prev, curr = curr, new_value
            return max(prev, curr)

        if len(nums) <= 2:
            return max(nums) if nums else 0
        return max(_rob(nums[1:]), _rob(nums[:-1]))

    def one_pass(self, nums: List[int]) -> int:
        """
        Solves a problem in two pass in O(N) and O(1) as two_pass, but only one pass required

        Args:
            nums(list[int]):

        Returns:
            int:

        """
        if len(nums) <= 1:
            return max(nums) if nums else 0
        prev1, curr1 = 0, 0
        prev2, curr2 = 0, 0
        for i in range(len(nums) - 1):
            prev1, curr1 = curr1, max(prev1 + nums[i], curr1)
            prev2, curr2 = curr2, max(prev2 + nums[i + 1], curr2)
        return max(prev1, curr1, prev2, curr2)

    def rob(self, nums: List[int]) -> int:
        """
        You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

        Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

        Example 1:

        Input: [2,3,2]
        Output: 3
        Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
                     because they are adjacent houses.
        Example 2:

        Input: [1,2,3,1]
        Output: 4
        Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
                     Total amount you can rob = 1 + 3 = 4.

        Args:
            nums(list[int]):

        Returns:
            int:

        """
        return self.one_pass(nums)
    #        *
    #   [2,3,2]
    # [0,2,3]
    #   [0,3,3]
    #     [3,2,0]
    #   []

    #      *
    #   [1,2,3,1]
    #        *
    # [0,1,2,3]
    # [0,1,2,4]
    #        *
    #   [0,2,3,1]
    #   [0,2,3,3]
    #      *-*
    # [1,2,3,2,1]
    # [1,2,3,2]
    #   [2,3,2,1]
    #