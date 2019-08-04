"""
Solution for 1144. Decrease Elements To Make Array Zigzag
https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/
"""

class Solution:
    """
    Runtime: 44 ms, faster than 50.00% of Python3 online submissions for Decrease Elements To Make Array Zigzag.
    Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Decrease Elements To Make Array Zigzag.
    """
    def movesToMakeZigzag(self, nums):
        """
        Given an array nums of integers, a move consists of choosing any element and decreasing it by 1.

        An array A is a zigzag array if either:

        Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
        OR, every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...
        Return the minimum number of moves to transform the given array nums into a zigzag array.



        Example 1:

        Input: nums = [1,2,3]
        Output: 2
        Explanation: We can decrease 2 to 0 or 3 to 1.
        Example 2:

        Input: nums = [9,6,1,6,2]
        Output: 4


        Constraints:

        1 <= nums.length <= 1000
        1 <= nums[i] <= 1000
        Args:
            nums: list<int>

        Returns:
            int:
        """
        def helper(prev, i, increasing, count):
            """
            Helper function
            Args:
                prev: int
                i: int
                increasing: bool
                count: int

            Returns:
                int:
            """
            if not i + 1 < len(nums):
                return count
            if increasing:
                diff = max(0, prev - nums[i + 1] + 1)
                return helper(nums[i + 1], i + 1, not increasing, count + diff)
            else:
                diff = max(0, nums[i + 1] - prev + 1)
                return helper(nums[i + 1] - diff, i + 1, not increasing, count + diff)

        return min(helper(nums[0], 0, True, 0), helper(nums[0], 0, False, 0))
