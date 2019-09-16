"""
Solution for 1190. Reverse Substrings Between Each Pair of Parentheses
https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
"""

class Solution:
    """
    Runtime: 32 ms, faster than 95.88% of Python3 online submissions for Reverse Substrings Between Each Pair of Parentheses.
    Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Reverse Substrings Between Each Pair of Parentheses.
    """
    def reverseParentheses(self, s: str) -> str:
        """
        Given a string s that consists of lower case English letters and brackets.

        Reverse the strings in each pair of matching parentheses, starting from the innermost one.

        Your result should not contain any bracket.





        Example 1:

        Input: s = "(abcd)"
        Output: "dcba"
        Example 2:

        Input: s = "(u(love)i)"
        Output: "iloveu"
        Example 3:

        Input: s = "(ed(et(oc))el)"
        Output: "leetcode"
        Example 4:

        Input: s = "a(bcdefghijkl(mno)p)q"
        Output: "apmnolkjihgfedcbq"


        Constraints:

        0 <= s.length <= 2000
        s only contains lower case English characters and parentheses.
        It's guaranteed that all parentheses are balanced.

        Args:
            s(str):

        Returns:
            str:

        """
        stack = ['']
        for char in s:
            if char == '(':
                stack.append('')
            elif char == ')':
                rev = stack.pop()[::-1]
                stack[-1] += rev
            else:
                stack[-1] += char
        return stack.pop()
    # "(u(love)i)"
    # ['', 'u', 'love', ]

    # "(abcd)"
    # " dcba"
    # "(u(love)i)"
    #  "i love y"
    #
    # "(ed(et(oc))el)"
    #         co
    #      oc te
    #   le et co  de