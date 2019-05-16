"""
Solution for 462. Minimum Moves to Equal Array Elements II
https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
"""

class Solution:
    """
    Runtime: 48 ms, faster than 54.52% of Python3 online submissions for Minimum Moves to Equal
        Array Elements II.
    Memory Usage: 14.1 MB, less than 54.90% of Python3 online submissions for Minimum Moves to
        Equal Array Elements II.
    """
    def minMoves2(self, nums):
        """
        Given a non-empty integer array, find the minimum number of moves required to make all
        array elements equal, where a move is incrementing a selected element by 1 or decrementing
        a selected element by 1.

        You may assume the array's length is at most 10,000.

        Example:

        Input:
        [1,2,3]

        Output:
        2

        Explanation:
        Only two moves are needed (remember each move increments or decrements one element):

        [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
        Args:
            nums: list of int where you find the minimum moves from

        Returns:
            int: moves that you have to take to get uni-val array
        """
        nums.sort()
        middle = (len(nums) - 1) // 2
        value = nums[middle]
        moves = 0

        for i in range(len(nums)):
            if i != middle:
                moves += abs(nums[i] - value)

        return moves
