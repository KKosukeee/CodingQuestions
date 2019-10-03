"""
Solution for 848. Shifting Letters
https://leetcode.com/problems/shifting-letters/
"""

class Solution(object):
    """
    Runtime: 168 ms, faster than 85.39% of Python online submissions for Shifting Letters.
    Memory Usage: 14.5 MB, less than 33.33% of Python online submissions for Shifting Letters.
    """
    def two_pass(self, S, shifts):
        """
        Two-pass solution that runs in O(N) in time and space

        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        prefix = [shifts[-1]]
        for shift in reversed(shifts[:-1]):
            prefix.append(prefix[-1] + shift)

        S = list(S)
        for i in range(len(prefix)):
            j = len(prefix) - (i + 1)
            S[i] = chr((ord(S[i]) + prefix[j] - ord('a')) % 26 + ord('a'))
        return ''.join(S)

    def one_pass(self, S, shifts):
        """
        One-pass solution that runs in O(N) in time and space

        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        cum_shift, S = 0, list(S)
        for i in reversed(range(len(S))):
            cum_shift += shifts[i]
            S[i] = chr((ord(S[i]) + cum_shift - ord('a')) % 26 + ord('a'))
        return ''.join(S)

    def shiftingLetters(self, S, shifts):
        """
        We have a string S of lowercase letters, and an integer array shifts.

        Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

        For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

        Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

        Return the final string after all such shifts to S are applied.

        Example 1:

        Input: S = "abc", shifts = [3,5,9]
        Output: "rpl"
        Explanation:
        We start with "abc".
        After shifting the first 1 letters of S by 3, we have "dbc".
        After shifting the first 2 letters of S by 5, we have "igc".
        After shifting the first 3 letters of S by 9, we have "rpl", the answer.
        Note:

        1 <= S.length = shifts.length <= 20000
        0 <= shifts[i] <= 10 ^ 9

        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        return self.one_pass(S, shifts)

    """
    Brute force:
    Time: O(N^2), Space: O(1)
    1. Loop through shifts array
        1.1 Given index i, shift first i+1 characters in S by the shift number
    2. Return the characters 

    Inverse prefix-sum:
    Time: O(N), Space: O(N)
    1. Take the prefix-sum starting from the end to the start
    2. Loop through the prefix sum array one by one from the start
        2.1 Given an index i, change the S[i] in prefix[i] times using modulo operation
    3. Return the characters

    One-pass prefix-sum:
    Time: O(N), Space: O(N)
    1. Loop through the character in S
        1.1 Keep count the cumulative shifts to the i-th index
        1.2 Shift the current character by the cumulative shift value
    2. Return the S

    [ 3, 5,9]
    [17,14,9]

    """
