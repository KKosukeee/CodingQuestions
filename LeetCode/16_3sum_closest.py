"""
Solution for 16. 3Sum Closest
https://leetcode.com/problems/3sum-closest/
"""

class Solution:
    """
    Runtime: 132 ms, faster than 49.37% of Python3 online submissions for 3Sum Closest.
    Memory Usage: 13.1 MB, less than 5.29% of Python3 online submissions for 3Sum Closest.
    """
    def threeSumClosest(self, nums, target):
        """
        Given an array nums of n integers and an integer target, find three integers in nums such
        that the sum is closest to target. Return the sum of the three integers. You may assume
        that each input would have exactly one solution.

        Example:

        Given array nums = [-1, 2, 1, -4], and target = 1.

        The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
        Args:
            nums: list of integers to look for 3sum
            target: target number which 3 numbers add up to

        Returns:
            list<int>: list of integers which has the closest to the target
        """
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return sum

                if abs(sum - target) < abs(result - target):
                    result = sum

                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1

        return result
