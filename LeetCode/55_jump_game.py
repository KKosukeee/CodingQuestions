"""
Solution for 55. Jump Game
https://leetcode.com/problems/jump-game/
"""

class Solution:
    """
    Runtime: 44 ms, faster than 91.67% of Python3 online submissions for Jump Game.
    Memory Usage: 14.5 MB, less than 5.28% of Python3 online submissions for Jump Game.
    """

    # Time: O(n^2), Space: O(n)
    def dp(self, nums):
        """
        DP solution for this question.
        Args:
            nums: list<int> to determine if there is a way to reach the goal from index of 0

        Returns:
            bool: True if you can reach to the goal from the start of the array, False otherwise
        """

        # Initialize dp array with the last element set to True
        dp = [False] * len(nums)
        dp[-1] = True

        # Loop through the array from the end to the start
        for i in range(len(nums) - 2, -1, -1):

            # Loop for a range of 1 to nums[i] + 1, and name it as step
            for step in range(1, nums[i] + 1):

                # Check if current index plus nums[i] >= len(nums) - 1
                if i + step >= len(nums) - 1:
                    # If so, then assign dp[index] as True and break
                    dp[i] = True
                    break

                # If dp[i + step] is True, then assign current as True, then break
                if dp[i + step]:
                    dp[i] = True
                    break

        # Return the dp[0]
        return dp[0]

    # Time: O(n), Space: O(1)
    def greedy(self, nums):
        """
        Greedy solution which runs in linear time
        Args:
            nums: list<int> to determine if there is a way to reach the goal from index of 0

        Returns:
            bool: True if you can reach to the goal from the start of the array, False otherwise
        """
        left_most = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= left_most:
                left_most = i

        return left_most == 0

    def canJump(self, nums):
        """
        Main function for this question
        Args:
            nums: list<int> to determine if there is a way to reach the goal from index of 0

        Returns:
            bool: True if you can reach to the goal from the start of the array, False otherwise
        """
        return self.greedy(nums)
