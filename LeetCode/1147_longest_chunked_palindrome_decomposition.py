"""
Solution for 1147. Longest Chunked Palindrome Decomposition
https://leetcode.com/problems/longest-chunked-palindrome-decomposition/
"""

class Solution:
    """
    Runtime: 40 ms, faster than 100.00% of Python3 online submissions for Longest Chunked Palindrome Decomposition.
    Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Longest Chunked Palindrome Decomposition.
    """
    def longestDecomposition(self, text):
        """
        Return the largest possible k such that there exists a_1, a_2, ..., a_k such that:

        Each a_i is a non-empty string;
        Their concatenation a_1 + a_2 + ... + a_k is equal to text;
        For all 1 <= i <= k,  a_i = a_{k+1 - i}.


        Example 1:

        Input: text = "ghiabcdefhelloadamhelloabcdefghi"
        Output: 7
        Explanation: We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
        Example 2:

        Input: text = "merchant"
        Output: 1
        Explanation: We can split the string on "(merchant)".
        Example 3:

        Input: text = "antaprezatepzapreanta"
        Output: 11
        Explanation: We can split the string on "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)".
        Example 4:

        Input: text = "aaa"
        Output: 3
        Explanation: We can split the string on "(a)(a)(a)".


        Constraints:

        text consists only of lowercase English characters.
        1 <= text.length <= 1000
        Args:
            text: str

        Returns:
            int
        """
        stack = []
        k = 0
        i, j = 0, len(text) - 1

        while i <= j:
            stack.append(text[i])
            if text[i] == text[j]:
                # stack operation
                while stack and stack[-1] == text[j] and i < j:
                    _ = stack.pop()
                    j -= 1
                k += 2 if not stack else 0
            i += 1
        return k if not stack else k + 1
