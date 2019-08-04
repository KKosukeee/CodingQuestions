"""
Solution for 378. Kth Smallest Element in a Sorted Matrix
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
"""
import heapq

class Solution:
    """
    Runtime: 240 ms, faster than 51.62% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
    Memory Usage: 20.1 MB, less than 6.06% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
    """
    def kthSmallest(self, matrix, k):
        """
        Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

        Note that it is the kth smallest element in the sorted order, not the kth distinct element.

        Example:

        matrix = [
           [ 1,  5,  9],
           [10, 11, 13],
           [12, 13, 15]
        ],
        k = 8,

        return 13.
        Note:
        You may assume k is always valid, 1 ≤ k ≤ n2.
        Args:
            matrix: list<list<int>> representing the matrix
            k: int value

        Returns:
            int: as the kth smallest element in the matrix
        """
        nums = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                nums.append(matrix[i][j])

        nums.sort()
        return nums[k - 1]

    def kthSmallest(self, matrix, k):
        """
        Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

        Note that it is the kth smallest element in the sorted order, not the kth distinct element.

        Example:

        matrix = [
           [ 1,  5,  9],
           [10, 11, 13],
           [12, 13, 15]
        ],
        k = 8,

        return 13.
        Note:
        You may assume k is always valid, 1 ≤ k ≤ n2.
        Args:
            matrix: list<list<int>> representing the matrix
            k: int value

        Returns:
            int: as the kth smallest element in the matrix
        """
        nums = [val for row in matrix for val in row]
        heapq.heapify(nums)

        while k > 0:
            kth_smallest = heapq.heappop(nums)
            k -= 1

        return kth_smallest
