"""
Solution for 373. Find K Pairs with Smallest Sums
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
"""
import heapq

class Solution(object):
    """
    Runtime: 32 ms, faster than 91.99% of Python online submissions for Find K Pairs with Smallest Sums.
    Memory Usage: 12.3 MB, less than 40.00% of Python online submissions for Find K Pairs with Smallest Sums.
    """
    def brute_force(self, nums1, nums2, k):
        """
        A brute-force that runs O(MN) in time and space

        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        comb = [[a, b] for a in nums1 for b in nums2]
        comb.sort(key=lambda x: sum(x))
        return comb[:k]

    def heap(self, nums1, nums2, k):
        """
        A heap solution that runs in O(MN log(mn)) in time and O(MN) in space

        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        queue = [(nums1[0] + nums2[0], (0, 0))]
        result, visited = [], set()
        while len(result) < k and queue:
            p, (i, j) = heapq.heappop(queue)
            result.append([nums1[i], nums2[j]])
            # Down followed by the right
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                heapq.heappush(queue, (nums1[i + 1] + nums2[j], (i + 1, j)))
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                heapq.heappush(queue, (nums1[i] + nums2[j + 1], (i, j + 1)))
        return result

    def kSmallestPairs(self, nums1, nums2, k):
        """
        You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

        Define a pair (u,v) which consists of one element from the first array and one element from the second array.

        Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

        Example 1:

        Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
        Output: [[1,2],[1,4],[1,6]]
        Explanation: The first 3 pairs are returned from the sequence:
                     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
        Example 2:

        Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
        Output: [1,1],[1,1]
        Explanation: The first 2 pairs are returned from the sequence:
                     [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
        Example 3:

        Input: nums1 = [1,2], nums2 = [3], k = 3
        Output: [1,3],[2,3]
        Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        return self.heap(nums1, nums2, k)

    """
    Brute force:
    T: O(NM), S: O(NM)
    1. Get all comb by looping through two arrays
    2. Append all combinations to an array
    3. Sort the array by the sum of the inner arrays
    4. Take the first k by slicing the array, and return it

    Two pointers:
    T: O(N+M), S: O(1) # ignoring the returning array
    1. Have two pointeres pointing the smallest available element for array1, arry2

    [1,7,11]
    [2,4, 6]
    (1, 2)
    (1, 4) | (2, 7) => (1, 4)
    (1, 6) | (2, 7) => (1, 6)
    (7, 2)
    (7, 4) | (2,11) => (7, 4)
    (7, 6) | (2,11) => (2,11)
    (7, 6) | (4,11) => (7, 6)
    (4,11)
    (6,11)
    """