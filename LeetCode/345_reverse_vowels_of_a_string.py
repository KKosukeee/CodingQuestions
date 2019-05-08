"""
Solution for 345. Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/
"""

class Solution:
    """
    Runtime: 60 ms, faster than 85.57% of Python3 online submissions for Reverse Vowels of a
        String.
    Memory Usage: 14.1 MB, less than 22.88% of Python3 online submissions for Reverse Vowels of a
        String.
    """
    def reverseVowels(self, s):
        """
        Write a function that takes a string as input and reverse only the vowels of a string.

        Example 1:

        Input: "hello"
        Output: "holle"
        Example 2:

        Input: "leetcode"
        Output: "leotcede"
        Args:
            s: string to flip vowel chars

        Returns:
            str: string where all the vowel chars are flipped
        """
        i, j = 0, len(s) - 1
        vowels = {
            'a', 'e', 'i', 'o', 'u',
            'A', 'E', 'I', 'O', 'U',
        }

        s = list(s)
        while i <= j and i < len(s):
            if s[i] in vowels:
                while i <= j and j >= 0:
                    if s[j] in vowels:
                        s[i], s[j] = s[j], s[i]
                        j -= 1
                        break
                    else:
                        j -= 1

            i += 1

        return ''.join(s)
