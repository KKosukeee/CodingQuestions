"""
Solution for 821. Shortest Distance to a Character
https://leetcode.com/problems/shortest-distance-to-a-character/
"""
class Solution:
    """
    Runtime: 40 ms, faster than 98.87% of Python3 online submissions for Shortest Distance to a Character.
    Memory Usage: 13.8 MB, less than 7.69% of Python3 online submissions for Shortest Distance to a Character.
    """
    def shortestToChar(self, S, C):
        """
        Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

        Example 1:

        Input: S = "loveleetcode", C = 'e'
        Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


        Note:

        S string length is in [1, 10000].
        C is a single character, and guaranteed to be in string S.
        All letters in S and C are lowercase.
        Args:
            S(str):
            C(str):

        Returns:
            list[int]:
        """
        indices = [float('inf')]
        for i in range(len(S)):
            if S[i] == C:
                indices.append(i)
        distances = []
        j = 1
        print(indices)
        for i in range(len(S)):
            distances.append(min(abs(indices[j] - i), abs(indices[j - 1] - i)))
            if i >= indices[j]:
                j = min(j + 1, len(indices) - 1)
        return distances
