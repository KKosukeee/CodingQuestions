"""
Solution for 520. Detect Capital
https://leetcode.com/problems/detect-capital/
"""

class Solution:
    """
    Runtime: 28 ms, faster than 99.69% of Python3 online submissions for Detect Capital.
    Memory Usage: 13.1 MB, less than 81.31% of Python3 online submissions for Detect Capital.
    """
    def detectCapitalUse(self, word):
        """
        Given a word, you need to judge whether the usage of capitals in it is right or not.

        We define the usage of capitals in a word to be right when one of the following cases holds:

        All letters in this word are capitals, like "USA".
        All letters in this word are not capitals, like "leetcode".
        Only the first letter in this word is capital, like "Google".
        Otherwise, we define that this word doesn't use capitals in a right way.


        Example 1:

        Input: "USA"
        Output: True


        Example 2:

        Input: "FlaG"
        Output: False
        Args:
            word: str value to detect CaptalUse with

        Returns:
            bool: True if it's valid, False otherwise
        """
        upper_counter = 0
        lower_counter = 0
        upper_index = None

        for i, char in enumerate(word):
            if char.islower():
                lower_counter += 1
            else:
                upper_counter += 1
                if not upper_index:
                    upper_index = i

        if len(word) == upper_counter:
            return True
        elif len(word) == lower_counter:
            return True
        elif upper_counter > 1:
            return False

        if upper_index == 0:
            return True
        else:
            return False
