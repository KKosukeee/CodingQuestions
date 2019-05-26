"""
Solution for 338. Counting Bits
https://leetcode.com/problems/counting-bits/
"""

class Solution:
    """
    Runtime: 104 ms, faster than 96.70% of Python3 online submissions for Counting Bits.
    Memory Usage: 15.8 MB, less than 72.26% of Python3 online submissions for Counting Bits.
    """
    def countBits(self, num):
        """
        Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num
        calculate the number of 1's in their binary representation and return them as an array.

        Example 1:

        Input: 2
        Output: [0,1,1]
        Example 2:

        Input: 5
        Output: [0,1,1,2,1,2]
        Args:
            num: int value

        Returns:
            list<int>: representing for each location i, list[i] 1s are needed.
        """
        record = [0, 1]
        l = 2
        while l < num + 1:
            record = record + [i + 1 for i in record]
            l = l * 2

        return record[0:num + 1]
