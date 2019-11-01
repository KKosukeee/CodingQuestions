"""
Solution for 267. Palindrome Permutation II
https://leetcode.com/problems/palindrome-permutation-ii/
"""
from collections import Counter
from typing import List

class Solution:
    """
    Runtime: 36 ms, faster than 91.77% of Python3 online submissions for Palindrome Permutation II.
    Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Palindrome Permutation II.
    """
    def backtracking(self, s: str) -> List[str]:
        """
        A backtracking solution that runs in O((N/2)!) in time and O(N) in space

        Args:
            s:

        Returns:

        """
        counter = Counter(s)
        if len([char for char in counter.keys() if counter[char] % 2 != 0]) > 1:
            return []
        results = set()

        def rec(chars):
            if len(chars) == len(s):
                results.add(chars)
                return
            for key, val in counter.items():
                if val > 0:
                    counter[key] -= 2
                    rec(key + chars + key)
                    counter[key] += 2

        odd = ''
        for key, val in counter.items():
            if val % 2 != 0:
                counter[key] -= 1
                odd = key
        rec(odd)
        return results

    def generatePalindromes(self, s: str) -> List[str]:
        """
        Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

        Example 1:

        Input: "aabb"
        Output: ["abba", "baab"]
        Example 2:

        Input: "abc"
        Output: []

        Args:
            s:

        Returns:

        """
        return self.backtracking(s)

    """
    aaaabb
    aabbaa
    abaaba
    baaaab

    Simple solution
    1. Create counter
    2. Find if palindrome permutation exists
    3. Given the half palindrome permutation, try every possible combination

    """