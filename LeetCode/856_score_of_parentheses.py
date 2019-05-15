"""
Solution for 856. Score of Parentheses
https://leetcode.com/problems/score-of-parentheses/
"""


class Solution:
    """
    Runtime: 32 ms, faster than 99.15% of Python3 online submissions for Score of Parentheses.
    Memory Usage: 13.1 MB, less than 64.35% of Python3 online submissions for Score of Parentheses.
    """
    def scoreOfParentheses(self, S):
        """
        Given a balanced parentheses string S, compute the score of the string based on the
        following rule:

        () has score 1
        AB has score A + B, where A and B are balanced parentheses strings.
        (A) has score 2 * A, where A is a balanced parentheses string.


        Example 1:

        Input: "()"
        Output: 1
        Example 2:

        Input: "(())"
        Output: 2
        Example 3:

        Input: "()()"
        Output: 2
        Example 4:

        Input: "(()(()))"
        Output: 6
        Args:
            S: str value to calculate the score with

        Returns:
            int: score of the parentheses
        """
        def helper(i, j):
            answer, balance = 0, 0

            for k in range(i, j):
                balance += 1 if S[k] == '(' else -1

                # Balance is valid, now check for case A and B
                if balance == 0:
                    # Check if the pair is ()
                    if k - i == 1:
                        answer += 1

                    # Check if the pair is (...)
                    else:
                        # (()) -> it should be k - 1, but this works because of
                        # the range function (i, j) is actually [i, j)
                        answer += 2 * helper(i + 1, k)

                    i = k + 1

            return answer

        return helper(0, len(S))
