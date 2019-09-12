"""
Solution for 1186. Maximum Subarray Sum with One Deletion1186. Maximum Subarray Sum with One Deletion
https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/
"""
from typing import List

class Solution:
    """
    Runtime: 368 ms, faster than 22.87% of Python3 online submissions for Maximum Subarray Sum with One Deletion.
    Memory Usage: 25.6 MB, less than 100.00% of Python3 online submissions for Maximum Subarray Sum with One Deletion.
    """
    def maximumSum(self, arr: List[int]) -> int:
        """
        Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

        Note that the subarray needs to be non-empty after deleting one element.



        Example 1:

        Input: arr = [1,-2,0,3]
        Output: 4
        Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
        Example 2:

        Input: arr = [1,-2,-2,3]
        Output: 3
        Explanation: We just choose [3] and it's the maximum sum.
        Example 3:

        Input: arr = [-1,-1,-1,-1]
        Output: -1
        Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.


        Constraints:

        1 <= arr.length <= 10^5
        -10^4 <= arr[i] <= 10^4

        Args:
            arr(list[int]):

        Returns:
            int:

        """
        ending_at, starting_at = [0] * len(arr), [0] * len(arr)
        ending_at[0], starting_at[-1] = arr[0], arr[-1]
        global_max = arr[0]

        for i in range(1, len(arr)):
            ending_at[i] = max(ending_at[i - 1] + arr[i], arr[i])
            global_max = max(ending_at[i], global_max)

        for i in reversed(range(len(arr) - 1)):
            starting_at[i] = max(starting_at[i + 1] + arr[i], arr[i])
            global_max = max(starting_at[i], global_max)

        for i in range(1, len(arr) - 1):
            global_max = max(global_max, ending_at[i - 1] + starting_at[i + 1])

        return global_max

    #     *
    # [1,-2,0,3]
    #  *
    # [1,-1,0,3] -> end
    # [2, 1,3,3] -> start

    #     *
    # [1,-2,-2,3]