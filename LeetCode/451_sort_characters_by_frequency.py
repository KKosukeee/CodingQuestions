"""
Solution for 451. Sort Characters By Frequency
https://leetcode.com/problems/sort-characters-by-frequency/submissions/
"""

import heapq
from collections import Counter

class Solution:
    """
    Runtime: 76 ms, faster than 22.69% of Python3 online submissions for Sort Characters By
        Frequency.


    Memory Usage: 14 MB, less than 12.80% of Python3 online submissions for Sort Characters By
        Frequency.
    """
    # Time: O(nlog(n)), Space: O(n)
    def frequencySort(self, s):
        """
        Given a string, sort it in decreasing order based on the frequency of characters.

        Example 1:

        Input:
        "tree"

        Output:
        "eert"

        Explanation:
        'e' appears twice while 'r' and 't' both appear once.
        So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
        Example 2:

        Input:
        "cccaaa"

        Output:
        "cccaaa"

        Explanation:
        Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
        Note that "cacaca" is incorrect, as the same characters must be together.
        Example 3:

        Input:
        "Aabb"

        Output:
        "bbAa"

        Explanation:
        "bbaA" is also a valid answer, but "Aabb" is incorrect.
        Note that 'A' and 'a' are treated as two different characters.

        Args:
            s: string to work on

        Returns:
            str: string which is flipped according to the frequency
        """
        # Create a counter
        counter = Counter(s)
        heap = []
        new_string = ''

        # Create a min-heap
        for key, val in counter.items():
            heapq.heappush(heap, (val, key))

        # Pop an element from the heap, until it gets empty
        while heap:
            count, char = heapq.heappop(heap)

            # Repeat the char N times
            while count:
                new_string += char
                count -= 1

        # Flip the string
        return new_string[::-1]
