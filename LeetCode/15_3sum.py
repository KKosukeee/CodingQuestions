"""
Solution for 15. 3Sum
https://leetcode.com/problems/3sum/
"""

class Solution:
    """
    Runtime: 1252 ms, faster than 37.22% of Python3 online submissions for 3Sum.
    Memory Usage: 17.9 MB, less than 7.17% of Python3 online submissions for 3Sum.
    """
    def threeSum(self, nums):
        """
        Given an array nums of n integers, are there elements a, b, c in nums such that
        a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

        Note:

        The solution set must not contain duplicate triplets.

        Example:

        Given array nums = [-1, 0, 1, 2, -1, -4],

        A solution set is:
        [
          [-1, 0, 1],
          [-1, -1, 2]
        ]
        Args:
            nums: list of integers to look for 3-sum

        Returns:
            list<int>: containing 3 integers from nums which add up to zero
        """
        # Sort array: [-4,-1,-1,0,1,2]
        nums.sort()

        # Create result set
        result = set()

        # Loop through nums
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[-1]:
                continue

            d = set()

            # Loop through i + 1:
            for j, x in enumerate(nums[i + 1:]):

                # Express x = -x -v
                comp = -x - v

                # If x is in the dict, then you found the result
                if x in d:
                    result.add((v, comp, x))
                # Otherwise, store the complement into dict
                else:
                    d.add(comp)

        # Return the result in list
        return list(map(list, result))
