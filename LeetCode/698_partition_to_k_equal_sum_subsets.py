"""
Solution for 698. Partition to K Equal Sum Subsets
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
"""

class Solution(object):
    """
    Runtime: 24 ms, faster than 95.35% of Python online submissions for Partition to K Equal Sum Subsets.
    Memory Usage: 11.8 MB, less than 60.00% of Python online submissions for Partition to K Equal Sum Subsets.
    """
    def backtrack(self, nums, k):
        """
        A brute force backtrack solution that runs out TLE.

        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        target = sum(nums) / k
        if target % 1 != 0:
            return False
        nums.sort(reverse=True)

        def backtrack(used, current, count):
            if count > k:
                return False
            if len(used) == len(nums) and count == k:
                return True
            return any(
                backtrack(used.union(set([i])), current + num if current + num < target else 0,
                          count if current + num < target else count + 1) for i, num in
                enumerate(nums) if i not in used and current + num <= target)

        return backtrack(set(), 0, 0)

    def better_backtrack(self, nums, k):
        """
        Better backtrack solution that runs in O(N*K!) in space and time

        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        target = sum(nums) // k
        if target % 1 != 0:
            return False
        bucket = [0] * k
        nums.sort(reverse=True)

        def dfs(index):
            if index == len(nums) and len(set(bucket)) == 1:
                return True
            for i in range(k):
                bucket[i] += nums[index]
                if bucket[i] <= target and dfs(index + 1):
                    return True
                bucket[i] -= nums[index]
                if bucket[i] == 0:
                    return False
            return False

        return dfs(0)

    def canPartitionKSubsets(self, nums, k):
        """
        Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.



        Example 1:

        Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
        Output: True
        Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.


        Note:

        1 <= k <= len(nums) <= 16.
        0 < nums[i] < 10000.

        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        return self.better_backtrack(nums, k)

    """
    Brute force
    1. Find the target sum by summing all elements up, then divide by the k
    2. Backtrack the array to find any combination that add up the target sum


    """