"""
Solution for 17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

class Solution:
    """
    Runtime: 36 ms, faster than 81.75% of Python3 online submissions for Letter Combinations of a
        Phone Number.
    Memory Usage: 13.2 MB, less than 5.86% of Python3 online submissions for Letter Combinations of
        a Phone Number.
    """
    def letterCombinations(self, digits):
        """
        Given a string containing digits from 2-9 inclusive, return all possible letter
        combinations that the number could represent.

        A mapping of digit to letters (just like on the telephone buttons) is given below. Note
        that 1 does not map to any letters.

        Example:

        Input: "23"
        Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
        Args:
            digits: string of integers to look for all combinations

        Returns:
            list<str>: containing all combinations for given digits
        """
        hash_table = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        result = []

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                result.append(combination)
            else:
                for char in hash_table[next_digits[0]]:
                    backtrack(combination + char, next_digits[1:])

        if digits:
            backtrack('', digits)

        return result
