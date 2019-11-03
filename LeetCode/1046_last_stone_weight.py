"""
Solution for 1046. Last Stone Weight
https://leetcode.com/problems/last-stone-weight/
"""
import heapq
from typing import List

class Solution:
    """
    Runtime: 32 ms, faster than 95.89% of Python3 online submissions for Last Stone Weight.
    Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Last Stone Weight.
    """
    def heap_solution(self, stones: List[int]) -> int:
        """
        A heap solution that runs in O(Nlog(N)) in time and O(N) in space

        Args:
            stones:

        Returns:

        """
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            p, q = heapq.heappop(max_heap), heapq.heappop(max_heap)
            if p != q:
                heapq.heappush(max_heap, -abs((-p) - (-q)))
        return -heapq.heappop(max_heap) if max_heap else 0

    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        We have a collection of rocks, each rock has a positive integer weight.

        Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

        If x == y, both stones are totally destroyed;
        If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
        At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)



        Example 1:

        Input: [2,7,4,1,8,1]
        Output: 1
        Explanation:
        We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
        we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
        we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
        we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.


        Note:

        1 <= stones.length <= 30
        1 <= stones[i] <= 1000

        Args:
            stones:

        Returns:

        """
        return self.heap_solution(stones)

    """
    Heap solution
    T: O(Nlog(N)), S: O(1), if stones is modifiable
    1. Create a heap
    2. Loop while heap.length is > 1
        2.1 Pop two largest elements
        2.2 If both values are the same, do nothing
        2.3 If both values aren't the same, take the abs diff, put it back to the heap
    3. return the element if heap, otherwise 0

    Binary search

    """