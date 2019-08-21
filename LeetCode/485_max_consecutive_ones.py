"""
Solution for 485. Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/
"""
class Solution:
    """
    Runtime: 396 ms, faster than 90.44% of Python3 online submissions for Max Consecutive Ones.
    Memory Usage: 14.1 MB, less than 7.69% of Python3 online submissions for Max Consecutive Ones.
    """
    def findMaxConsecutiveOnes(self, nums):
        """
        Given a binary array, find the maximum number of consecutive 1s in this array.

        Example 1:
        Input: [1,1,0,1,1,1]
        Output: 3
        Explanation: The first two digits or the last three digits are consecutive 1s.
            The maximum number of consecutive 1s is 3.
        Note:

        The input array will only contain 0 and 1.
        The length of input array is a positive integer and will not exceed 10,000
        Args:
            nums(list[int]):

        Returns:
            int:
        """
        current, count = 0, 0
        for num in nums:
            if num == 1:
                current += 1
            else:
                count = max(count, current)
                current = 0
        return max(count, current)
