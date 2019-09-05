"""
Solution for 875. Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas/
"""
from typing import List
import math

class Solution:
    """
    Runtime: 624 ms, faster than 16.87% of Python3 online submissions for Koko Eating Bananas.
    Memory Usage: 15.2 MB, less than 11.11% of Python3 online submissions for Koko Eating Bananas.
    """
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        """
        Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  The guards have gone and will come back in H hours.

        Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.

        Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

        Return the minimum integer K such that she can eat all the bananas within H hours.



        Example 1:

        Input: piles = [3,6,7,11], H = 8
        Output: 4
        Example 2:

        Input: piles = [30,11,23,4,20], H = 5
        Output: 30
        Example 3:

        Input: piles = [30,11,23,4,20], H = 6
        Output: 23


        Note:

        1 <= piles.length <= 10^4
        piles.length <= H <= 10^9
        1 <= piles[i] <= 10^9

        Args:
            piles(list[int]):
            H(int):

        Returns:
            int

        """
        def is_possible(guessing):
            """
            Determine if it's possible to eas all banana given guessing

            Args:
                guessing(int):

            Returns:
                bool:

            """
            return H >= sum(math.ceil(p / guessing) for p in piles)

        low, high = 1, max(piles)
        while low <= high:
            middle = (low + high) // 2
            if is_possible(middle):
                high = middle - 1
            else:
                low = middle + 1
        return low

    # [30, 11, 23, 4, 20], 5
    # 31 // 2 = 15
    # [2,1,2,1,2] -> increment
    # l = 16, h = 30
    # 46 // 2 = 23
    # [2,1,1,1,1] -> increment
    # l = 24, h = 30
    # 54 // 2 = 27
    # [2,1,1,1,1] -> increment
    # l = 28, h = 30
    # 58 // 2 = 29
    # [2,1,1,1,1] -> increment
    # l = 30

    # piles = [3,6,7,11], H = 8, K = 4
    # low, high = 1, 11
    # middle = 6
    # [1,1,2,2] -> decrement
    # low, high = 1, 5
    # [1,2,2,3] -> decrement
    # low, high = 1, 4
    # [1,2,2,3] -> decrement
    # low, high = 1, 3
    # [1,2,2,4] -> increment
    # low,
    # [3,6,7,11]
    # [1,2,2,3] sum = 8
    # 1: [6,7,11]
    # 2: [2,7,11]
    # 3: [7,11]
    # 4: [3,11]
    # 5: [11]
    # 6: [7]
    # 7: [3]
    # 8: []

    # [30,11,23,4,20], H = 5, K = 30
    # [1,1,1,1,1], sum = 5
    # [30,11,23,4,20]
    # [4,11,20,23,30]
    # 1: [11,23,4,20]
    # 2: [23,4,20]
    # 3: [4,20]
    # 4: [20]
    # 5: []

    # [30,11,23,4,20], H = 6, K = 23
    # [2,1,1,1,1], sum = 6
    #
    # 1: [7,11,23,4,20]
    # 2: [11,23,4,20]
    # 3: [23,4,20]
    # 4: [4,20]
    # 5: [20]
    # 6: []

    # [30,11,23,4,20], H = 7, K = 20
    # [2,1,2,1,1], sum = 7

