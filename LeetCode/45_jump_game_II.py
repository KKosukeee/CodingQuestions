"""
Solution for 45. Jump Game II
https://leetcode.com/problems/jump-game-ii/
"""

class Solution:
    """
    Runtime: 60 ms, faster than 51.45% of Python3 online submissions for Jump Game II.
    Memory Usage: 14.4 MB, less than 7.50% of Python3 online submissions for Jump Game II.
    """
    def jump(self, nums):
        """
        Given an array of non-negative integers, you are initially positioned at the first index of
        the array.

        Each element in the array represents your maximum jump length at that position.

        Your goal is to reach the last index in the minimum number of jumps.

        Example:

        Input: [2,3,1,1,4]
        Output: 2
        Explanation: The minimum number of jumps to reach the last index is 2.
            Jump 1 step from index 0 to 1, then 3 steps to the last index.
        Args:
            nums: list of integers where for each value indicates the steps you can take from the
                given cell

        Returns:
            int: minimum number of steps it takes to get the last index number
        """
        i = 0
        counter = 0

        while i < len(nums) - 1:  # O(n)
            best_index = 0
            best_number = 0

            for j in range(1, nums[i] + 1):
                if i + j == len(nums) - 1:
                    return counter + 1
                if j + nums[i + j] >= best_number:
                    best_number = j + nums[i + j]
                    best_index = i + j

            counter += 1
            i = best_index
        return counter
