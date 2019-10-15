"""
Solution for 473. Matchsticks to Square
https://leetcode.com/problems/matchsticks-to-square/
"""

class Solution(object):
    """
    Runtime: 724 ms, faster than 66.18% of Python online submissions for Matchsticks to Square.
    Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Matchsticks to Square.
    """
    def backtrack(self, nums):
        """
        Backtracking solution that runs in O(4^N) in time and O(N) in space

        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        length = sum(nums) / 4
        if length % 1 != 0:
            return False
        bucket = [0] * 4
        nums.sort(reverse=True)

        def dfs(index):
            if index == len(nums) and bucket[0] == bucket[1] == bucket[2] == bucket[3]:
                return True
            for i in range(4):
                bucket[i] += nums[index]
                if bucket[i] <= length and dfs(index + 1):
                    return True
                bucket[i] -= nums[index]
                if bucket[i] == 0:
                    return False
            return False

        return dfs(0)

    # TODO: Learn bitmask, then implement it
    def dp(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

    def makesquare(self, nums):
        """
        Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

        Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

        Example 1:
        Input: [1,1,2,2,2]
        Output: true

        Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
        Example 2:
        Input: [3,3,3,3,4]
        Output: false

        Explanation: You cannot find a way to form a square with all the matchsticks.
        Note:
        The length sum of the given matchsticks is in the range of 0 to 10^9.
        The length of the given matchstick array will not exceed 15.

        :type nums: List[int]
        :rtype: bool
        """
        return self.backtrack(nums)

    """
    Throughts
    1. sum(nums) % 4 != 0, then False
    2. all(nums[i] <= sum(nums)) == False, then False

    Intuition
    1. If there are four numbers exactly the same, then you can form a square
    2. If there are N numbers with the same value where N % 4 == 0, then you can form a square

    Simple solution:
    1. Try to find any combination of nums, such that the values are the same and the length of the array is 4


    """