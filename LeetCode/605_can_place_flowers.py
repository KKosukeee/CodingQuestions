"""
Solution for 605. Can Place Flowers
https://leetcode.com/problems/can-place-flowers/
"""

class Solution:
    """
    Runtime: 68 ms, faster than 40.29% of Python3 online submissions for Can Place Flowers.
    Memory Usage: 13.4 MB, less than 21.44% of Python3 online submissions for Can Place Flowers.
    """
    def canPlaceFlowers(self, flowerbed, n):
        """
        Suppose you have a long flowerbed in which some of the plots are planted and some are not.
        However, flowers cannot be planted in adjacent plots - they would compete for water and
        both would die.

        Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1
        means not empty), and a number n, return if n new flowers can be planted in it without
        violating the no-adjacent-flowers rule.

        Example 1:
        Input: flowerbed = [1,0,0,0,1], n = 1
        Output: True
        Example 2:
        Input: flowerbed = [1,0,0,0,1], n = 2
        Output: False
        Args:
            flowerbed: list of integer where the value is {0, 1} indicating the flower can be
                planted at ith bed or not
            n: number of flowers to plan

        Returns:
            bool: indicating if all the flowers can be planted or not
        """
        N = len(flowerbed)

        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue

            if (i - 1) >= 0 and flowerbed[i - 1] == 1:
                continue

            if (i + 1) < N and flowerbed[i + 1] == 1:
                continue

            flowerbed[i] = 1
            n -= 1

        return n <= 0
