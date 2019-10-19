"""
Solution for 724. Find Pivot Index
https://leetcode.com/problems/find-pivot-index/
"""

class Solution(object):
    """
    Runtime: 124 ms, faster than 91.29% of Python online submissions for Find Pivot Index.
    Memory Usage: 12.5 MB, less than 80.00% of Python online submissions for Find Pivot Index.
    """
    def prefix_sums(self, nums):
        """
        An initial solution that runs in O(N) in time and space

        :type nums: List[int]
        :rtype: int
        """
        start_sum, end_sum = [0], [0]
        for i in range(len(nums)):
            j = len(nums) - i - 1
            start_sum.append(start_sum[-1] + nums[i])
            end_sum.append(end_sum[-1] + nums[j])
        for i in range(len(nums)):
            j = len(nums) - i - 1
            if start_sum[i] == end_sum[j]:
                return i
        return -1

    def in_place(self, nums):
        """
        In place that runs in O(N) in time and O(1) in space

        :type nums: List[int]
        :rtype: int
        """
        total, prefix = sum(nums), 0
        for i, num in enumerate(nums):
            if prefix == total - prefix - num:
                return i
            prefix += nums[i]
        return -1

    def pivotIndex(self, nums):
        """
        Given an array of integers nums, write a method that returns the "pivot" index of this array.

        We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

        If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

        Example 1:

        Input:
        nums = [1, 7, 3, 6, 5, 6]
        Output: 3
        Explanation:
        The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
        Also, 3 is the first index where this occurs.


        Example 2:

        Input:
        nums = [1, 2, 3]
        Output: -1
        Explanation:
        There is no index that satisfies the conditions in the problem statement.


        Note:

        The length of nums will be in the range [0, 10000].
        Each element nums[i] will be an integer in the range [-1000, 1000].

        :type nums: List[int]
        :rtype: int
        """
        return self.in_place(nums)

    """
    ! It only works for the case where all # are positives!!!
    Two pointer approach
    T: O(N), S: O(1)
    1. Initialize two poitners, one pointing to the begining, the one pointing the end
    2. Try to shorten the range by comparing the prefix_sum starting from the being, and the end
    3. If i == j and cum_sum[i] == cum_sum[j], then return the index
    4. If i exceeds the j, then return -1

    Two prefix sum approach
    T: O(N), S: O(N)
    1. Try to take the prefix sum from the left
    2. Try to take the prefix sum from the right
    3. Loop through the prefix sum array
        3.1 At any point i, if the start_sum[i] == end_sum[i], then return the i
    4. Return -1 in case the index isn't found

    In-place approach
    T: O(N), S: O(1)
    1. Calculate the sum of nums
    2. Loop through the nums
        2.1 At any point of i, take the prefix sum
        2.2 If the prefix sum == sum(nums) - prefix sum
            2.3 Return the index
    3. Return -1

    [1, 7, 3, 6, 5, 6]
    S: [1,8 ,11,17,22,28]
    E: [6,11,17,20,27,28]
    """