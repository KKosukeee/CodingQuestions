"""
Solution for 18. 4Sum
https://leetcode.com/problems/4sum/
"""

class Solution:
    """
    Runtime: 1420 ms, faster than 12.45% of Python3 online submissions for 4Sum.
    Memory Usage: 13.2 MB, less than 16.60% of Python3 online submissions for 4Sum.
    """
    # Time: O(n^3), Space: O(n)
    def fourSum(self, nums, target):
        """
        Given an array nums of n integers and an integer target, are there elements a, b, c, and
        d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which
        gives the sum of target.

        Note:

        The solution set must not contain duplicate quadruplets.

        Example:

        Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

        A solution set is:
        [
          [-1,  0, 0, 1],
          [-2, -1, 1, 2],
          [-2,  0, 0, 2]
        ]
        Args:
            nums: list of integers to look for four numbers which add up to the target value
            target: target value to look for with four numbers

        Returns:
            list<list<int>>: 2D matrix containing integers which add up to the target value
        """
        result = set()

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                comp = set()

                for k in range(j + 1, len(nums)):
                    if nums[k] in comp:
                        l_value = target - nums[i] - nums[j] - nums[k]
                        indices = [nums[i], nums[j], l_value, nums[k]]
                        indices.sort()
                        result.add(tuple(indices))
                    else:
                        comp.add(target - nums[i] - nums[j] - nums[k])

        return list(map(list, result))
