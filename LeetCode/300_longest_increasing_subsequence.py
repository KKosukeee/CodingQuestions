"""
Solution for 300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/
"""

class Solution(object):
    """
    Runtime: 1400 ms, faster than 5.02% of Python online submissions for Longest Increasing Subsequence.
    Memory Usage: 12.1 MB, less than 9.09% of Python online submissions for Longest Increasing Subsequence.
    """
    def brute_force(self, nums):
        """
        A brute force solution that runs in O(N^N) in time and O(N) in space

        :type nums: List[int]
        :rtype: int
        """

        def rec(i):
            longest = 0
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    longest = max(longest, rec(j))
            return longest + 1

        longest = 0
        for i in range(len(nums)):
            longest = max(longest, rec(i))
        return longest

    def dp(self, nums):
        """
        DP solution that runs in O(N^2) in time and space

        :type nums: List[int]
        :rtype: int
        """
        memo = {}

        def rec(i):
            if i in memo:
                return memo[i]
            longest = 0
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    longest = max(longest, rec(j) if j not in memo else memo[j])
            memo[i] = longest + 1
            return memo[i]

        longest = 0
        for i in range(len(nums)):
            longest = max(longest, rec(i))
        return longest

    def top_down(self, nums):
        """
        A top-down solution that runs in O(N^2) in time and O(N) in space

        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        for i in reversed(range(len(nums))):
            larger = list(filter(lambda j: nums[i] < nums[j], range(i, len(nums))))
            dp[i] += max([dp[j] for j in larger]) if len(larger) > 0 else 0
        return max(dp)

    def bottom_up(self, nums):
        """
        A bottom-up solution that runs in O(N^2) in time and O(N) in space

        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            smaller = list(filter(lambda j: nums[j] < nums[i], range(i)))
            dp[i] += max([dp[j] for j in smaller]) if len(smaller) > 0 else 0
        return max(dp)

    def follow_up(self, nums):
        """
        TBA

        :type nums: List[int]
        :rtype: int
        """

    def lengthOfLIS(self, nums):
        """
        Given an unsorted array of integers, find the length of longest increasing subsequence.

        Example:

        Input: [10,9,2,5,3,7,101,18]
        Output: 4
        Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
        Note:

        There may be more than one LIS combination, it is only necessary for you to return the length.
        Your algorithm should run in O(n2) complexity.
        Follow up: Could you improve it to O(n log n) time complexity?

        :type nums: List[int]
        :rtype: int
        """
        return self.bottom_up(nums)