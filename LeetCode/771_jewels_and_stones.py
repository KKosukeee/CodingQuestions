"""
Solution for 771. Jewels and Stones
https://leetcode.com/problems/jewels-and-stones/
"""
from collections import Counter

class Solution:
    """
    Runtime: 36 ms, faster than 96.62% of Python3 online submissions for Jewels and Stones.
    Memory Usage: 13.3 MB, less than 12.48% of Python3 online submissions for Jewels and Stones.
    """
    def numJewelsInStones(self, J, S):
        """
        You're given strings J representing the types of stones that are jewels, and S representing
        the stones you have.  Each character in S is a type of stone you have.  You want to know
        how many of the stones you have are also jewels.

        The letters in J are guaranteed distinct, and all characters in J and S are letters.
        Letters are case sensitive, so "a" is considered a different type of stone from "A".

        Example 1:

        Input: J = "aA", S = "aAAbbbb"
        Output: 3
        Example 2:

        Input: J = "z", S = "ZZ"
        Output: 0
        Args:
            J: str value where each char is represented as a jewel
            S: str value where each char is represented as a stone

        Returns:
            int: number of jewels in stones
        """
        # Create a counter
        counter = Counter(S)
        result = 0

        # Loop for each jewel
        for char in J:
            result += counter[char]

        return result
