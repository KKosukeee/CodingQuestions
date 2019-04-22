"""
Solution for 1. Two Sum
https://leetcode.com/problems/two-sum/
"""

class Solution:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    """

    # Brute force approach: O(n^2)
    def naive_approach(self, nums, target):
        """
        solves two sum problem

        Args:
            nums: list of numbers to search from
            target: target number to add up to

        Returns:
            list: containing indices for numbers which add up to target
        """
        # Loop through nums,
        for i in range(len(nums)):

            # Loop through nums AGAIN
            for j in range(len(nums)):

                # If target == nums[i] + nums[j], then return indices
                if target == nums[i] + nums[j] and i != j:
                    return [i, j]

        return []

    # Optimal solution: O(n)
    def optimal_approach(self, nums, target):
        """
        solves two sum problem

        Args:
            nums: list of numbers to search from
            target: target number to add up to

        Returns:
            list: containing indices for numbers which add up to target
        """

        # Create complement_dictionary being complement as key, and index as value
        complement_dictionary = {}  # O(1)

        # Loop through nums
        for i in range(len(nums)):  # O(n)

            # If target - num[i] exists in the complement_dictionary, then return indices
            if target - nums[i] in complement_dictionary:  # O(1)
                return [complement_dictionary[target - nums[i]], i]  # O(1)

            # Store index value with key of target - nums[i]
            complement_dictionary[nums[i]] = i  # O(1)

        return []

    def twoSum(self, nums, target):
        """
        solves two sum problem

        Args:
            nums: list of numbers to search from
            target: target number to add up to

        Returns:
            list: containing indices for numbers which add up to target
        """

        return self.optimal_approach(nums, target)
