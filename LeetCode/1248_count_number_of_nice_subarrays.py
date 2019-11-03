"""
Solution for 1248. Count Number of Nice Subarrays
https://leetcode.com/problems/count-number-of-nice-subarrays/
"""
from typing import List
from collections import defaultdict

class Solution:
    """
    Runtime: 920 ms, faster than 100.00% of Python3 online submissions for Count Number of Nice Subarrays.
    Memory Usage: 20.5 MB, less than 100.00% of Python3 online submissions for Count Number of Nice Subarrays.
    """
    def sliding_window(self, nums: List[int], k: int) -> int:
        """
        A sliding window solution that runs in O(N) in time and space

        Args:
            nums:
            k:

        Returns:

        """
        odds = [i for i in range(len(nums)) if nums[i] % 2 != 0]
        if len(odds) < k:
            return 0
        odds = [-1] + odds + [len(nums)]
        i, result = 1, 0
        for j in range(1, len(odds) - 1):
            if j - i + 1 == k:
                result += (odds[i] - odds[i - 1]) * (odds[j + 1] - odds[j])
                i += 1
        return result

    def prefix_sum(self, nums: List[int], k: int) -> int:
        """
        A prefix sum solution that runs in O(N) in time and space

        Args:
            nums:
            k:

        Returns:

        """
        prefix = [0]
        for num in nums:
            if num % 2 != 0:
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])
        counter, result = defaultdict(int), 0
        for i, v in enumerate(prefix):
            if v - k in counter:
                result += counter[v - k]
            counter[v] += 1
        return result

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.

        Return the number of nice sub-arrays.



        Example 1:

        Input: nums = [1,1,2,1,1], k = 3
        Output: 2
        Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
        Example 2:

        Input: nums = [2,4,6], k = 1
        Output: 0
        Explanation: There is no odd numbers in the array.
        Example 3:

        Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
        Output: 16


        Constraints:

        1 <= nums.length <= 50000
        1 <= nums[i] <= 10^5
        1 <= k <= nums.length

        Args:
            nums:
            k:

        Returns:

        """
        return self.prefix_sum(nums, k)