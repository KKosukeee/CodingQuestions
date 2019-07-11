"""
Solution for 917. Reverse Only Letters
"""

class Solution:
    """
    Runtime: 32 ms, faster than 91.10% of Python3 online submissions for Reverse Only Letters.
    Memory Usage: 13.1 MB, less than 82.16% of Python3 online submissions for Reverse Only Letters.
    """
    def reverseOnlyLetters(self, S):
        """
        Given a string S, return the "reversed" string where all characters that are not a letter
        stay in the same place, and all letters reverse their positions.



        Example 1:

        Input: "ab-cd"
        Output: "dc-ba"
        Example 2:

        Input: "a-bC-dEf-ghIj"
        Output: "j-Ih-gfE-dCba"
        Example 3:

        Input: "Test1ng-Leet=code-Q!"
        Output: "Qedo1ct-eeLg=ntse-T!"
        Args:
            S: str value to reverse only letters

        Returns:
            str: where all the letters from S are reversed
        """
        i, j = 0, len(S) - 1
        S = list(S)

        while i <= j:
            while i < len(S) and not S[i].isalpha():
                i += 1

            if i <= j:
                while j >= 0 and not S[j].isalpha():
                    j -= 1

                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1
            else:
                break

        return ''.join(S)
