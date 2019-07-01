"""
Solution for 769. Max Chunks To Make Sorted
"""

class Solution:
    """
    Runtime: 32 ms, faster than 89.96% of Python3 online submissions for Max Chunks To Make Sorted.
    Memory Usage: 12.9 MB, less than 97.00% of Python3 online submissions for Max Chunks To Make Sorted.
    """
    def maxChunksToSorted(self, arr):
        """
        Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array
        into some number of "chunks" (partitions), and individually sort each chunk.  After
        concatenating them, the result equals the sorted array.

        What is the most number of chunks we could have made?

        Example 1:

        Input: arr = [4,3,2,1,0]
        Output: 1
        Explanation:
        Splitting into two or more chunks will not return the required result.
        For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't
        sorted.
        Example 2:

        Input: arr = [1,0,2,3,4]
        Output: 4
        Explanation:
        We can split into two chunks, such as [1, 0], [2, 3, 4].
        However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
        Args:
            arr: list of integers to find max chunks to make sorted array

        Returns:
            int: integer number indicating the max chunks to make sorted array
        """
        num_chunks = 0
        i = 0

        while i < len(arr):
            if arr[i] > i:
                j = i
                k = arr[i]

                while j <= k and j < len(arr):
                    k = max(k, arr[j])
                    j += 1

                num_chunks += 1
                i = j
            else:
                num_chunks += 1
                i += 1

        return num_chunks
