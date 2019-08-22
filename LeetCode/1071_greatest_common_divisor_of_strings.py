"""
Solution for 1071. Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/
"""
class Solution:
    """
    Runtime: 28 ms, faster than 98.74% of Python3 online submissions for Greatest Common Divisor of Strings.
    Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Greatest Common Divisor of Strings.
    """
    def gcdOfStrings(self, str1, str2):
        """
        For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

        Return the largest string X such that X divides str1 and X divides str2.



        Example 1:

        Input: str1 = "ABCABC", str2 = "ABC"
        Output: "ABC"
        Example 2:

        Input: str1 = "ABABAB", str2 = "ABAB"
        Output: "AB"
        Example 3:

        Input: str1 = "LEET", str2 = "CODE"
        Output: ""


        Note:

        1 <= str1.length <= 1000
        1 <= str2.length <= 1000
        str1[i] and str2[i] are English uppercase letters.
        Args:
            str1(str):
            str2(str):

        Returns:
            str:
        """
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        for i in range(1, len(str2)):
            sub = str2[:len(str2)//i]
            if not str1.replace(sub, '') and not str2.replace(sub, ''):
                return sub
        return ''
    