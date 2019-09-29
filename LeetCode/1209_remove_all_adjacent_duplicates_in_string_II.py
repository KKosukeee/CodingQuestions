"""
Solution for 1209. Remove All Adjacent Duplicates in String II
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
"""
class Solution(object):
    """
    Runtime: 148 ms, faster than 100.00% of Python online submissions for Remove All Adjacent Duplicates in String II.
    Memory Usage: 13.3 MB, less than 100.00% of Python online submissions for Remove All Adjacent Duplicates in String II.
    """
    def simple_solution(self, s, k):
        """
        A simple solution that runs in O(N) in time and the space

        Args:
            s(str):
            k(int):

        Returns:
            str:

        """
        stack = [s[0]]
        for char in s[1:]:
            if not stack or stack[-1][0] != char:
                stack.append(char)
            elif stack[-1][0] == char:
                stack[-1] += char
            if len(stack[-1]) == k:
                _ = stack.pop()
        return ''.join(stack)

    def removeDuplicates(self, s, k):
        """
        Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.

        We repeatedly make k duplicate removals on s until we no longer can.

        Return the final string after all such duplicate removals have been made.

        It is guaranteed that the answer is unique.



        Example 1:

        Input: s = "abcd", k = 2
        Output: "abcd"
        Explanation: There's nothing to delete.
        Example 2:

        Input: s = "deeedbbcccbdaa", k = 3
        Output: "aa"
        Explanation:
        First delete "eee" and "ccc", get "ddbbbdaa"
        Then delete "bbb", get "dddaa"
        Finally delete "ddd", get "aa"
        Example 3:

        Input: s = "pbbcggttciiippooaais", k = 2
        Output: "ps"

        :type s: str
        :type k: int
        :rtype: str
        """
        return self.simple_solution(s, k)
