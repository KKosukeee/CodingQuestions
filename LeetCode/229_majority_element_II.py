"""
Solution for 229. Majority Element II
https://leetcode.com/problems/majority-element-ii/
"""
from collections import Counter
from collections import deque

class Solution:
    """
    Runtime: 136 ms, faster than 74.38% of Python3 online submissions for Majority Element II.
    Memory Usage: 14.8 MB, less than 5.88% of Python3 online submissions for Majority Element II.
    """
    def naive_solution(self, nums):
        """

        Args:
            nums(list[int]):

        Returns:
            int:

        """
        return [key for key, value in Counter(nums).items() if value > len(nums) // 3]

    # [2,3,3]
    def constant_solution(self, nums):
        """

        Args:
            nums(list[int]):

        Returns:
            int:

        """
        nums = deque(sorted(nums))
        gap = len(nums) // 3
        i, j = len(nums) - (gap + 1), len(nums) - 1
        low_thres = 0
        while j >= low_thres:
            if i < low_thres:
                while j >= low_thres:
                    _ = nums.pop()
                    j -= 1
                break
            numi, numj = nums[i], nums[j]
            while j >= low_thres and numj == nums[j]:
                _ = nums.pop()
                i, j = i - 1, j - 1
            if numi == numj:
                nums.appendleft(numj)
                i, j, low_thres = i + 1, j + 1, low_thres + 1
        return nums

    def optimal_solution(self, nums):
        """

        Args:
            nums(list[int]):

        Returns:
            int:

        """
        first, second = None, None
        count1, count2 = 0, 0
        for num in nums:
            if num == first:
                count1 += 1
            elif num == second:
                count2 += 1
            elif count1 == 0:
                first = num
                count1 += 1
            elif count2 == 0:
                second = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1, count2 = 0, 0
        for num in nums:
            if num == first:
                count1 += 1
            elif num == second:
                count2 += 1
        result = []
        if count1 > len(nums) // 3:
            result.append(first)
        if count2 > len(nums) // 3:
            result.append(second)
        return result

    # N = len(nums)
    # max_maj = N // 3
    #  *   *
    # [1,1,1,2,2,2,3,3] N = 8
    # nums[j] = 3, nums[i] = 2
    #

    # [1,1,1,2,2,3,3,3] N = 8
    # [2,3,3]

    def majorityElement(self, nums):
        """
        Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

        Note: The algorithm should run in linear time and in O(1) space.

        Example 1:

        Input: [3,2,3]
        Output: [3]
        Example 2:

        Input: [1,1,1,3,3,2,2,2]
        Output: [1,2]

        Args:
            nums(list[int]):

        Returns:
            int:

        """
        return self.optimal_solution(nums)
