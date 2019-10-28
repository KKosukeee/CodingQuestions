"""
Solution for 1239. Maximum Length of a Concatenated String with Unique Characters
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
"""
from typing import List

class Solution:
    """
    Runtime: 84 ms, faster than 75.00% of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.
    Memory Usage: 54.5 MB, less than 100.00% of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.
    """
    def brute_force(self, arr: List[str]) -> int:
        """
        A brute force solution that is accepted

        Args:
            arr:

        Returns:

        """
        combos = [set()]
        for word in arr:
            unique = set(word)
            if len(unique) != len(word):
                continue
            new_combos = []
            for combo in combos:
                if combo.intersection(unique):
                    continue
                new_combos.append(combo.union(unique))
            combos.extend(new_combos)
        return max([len(combo) for combo in combos], default=0)

    def maxLength(self, arr: List[str]) -> int:
        """
        Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

        Return the maximum possible length of s.



        Example 1:

        Input: arr = ["un","iq","ue"]
        Output: 4
        Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
        Maximum length is 4.
        Example 2:

        Input: arr = ["cha","r","act","ers"]
        Output: 6
        Explanation: Possible solutions are "chaers" and "acters".
        Example 3:

        Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
        Output: 26


        Constraints:

        1 <= arr.length <= 16
        1 <= arr[i].length <= 26
        arr[i] contains only lower case English letters.

        Args:
            arr:

        Returns:

        """
        return self.brute_force(arr)

    """
    Backtrack (Brute Force)
    T: O(N^N), S: O(N)
    1. Give current word i, find the all combinations by looping through
    2. Try the add the current word j, if it's not yet used, and can form unique words

    Combination solution
    1. Store all combinations at time t
    2. At given word i, check if you can form new unique word in comb array
    3. Return the maximum length of the string in the combo
    """
