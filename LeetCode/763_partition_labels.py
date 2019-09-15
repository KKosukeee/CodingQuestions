"""
Solution for 763. Partition Labels
https://leetcode.com/problems/partition-labels/
"""
from typing import List

class Solution:
    """
    Runtime: 44 ms, faster than 82.43% of Python3 online submissions for Partition Labels.
    Memory Usage: 13.7 MB, less than 5.56% of Python3 online submissions for Partition Labels.
    """
    def partitionLabels(self, S: str) -> List[int]:
        """
        A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

        Example 1:
        Input: S = "ababcbacadefegdehijhklij"
        Output: [9,7,8]
        Explanation:
        The partition is "ababcbaca", "defegde", "hijhklij".
        This is a partition so that each letter appears in at most one part.
        A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
        Note:

        S will have length in range [1, 500].
        S will consist of lowercase letters ('a' to 'z') only.

        Args:
            S(str):

        Returns:
            list[int]:

        """
        word_indices = {char: i for i, char in enumerate(S)}
        result = []
        i, j = 0, word_indices[S[0]]
        while j < len(S):
            k = i
            while i <= j:
                j = max(j, word_indices[S[i]])
                i += 1
            result.append(j - k + 1)
            j = word_indices[S[j + 1]] if j + 1 < len(S) else j + 1
        return result

# *       **     *
# ababcbacadefegdehijhklij -> [9,7,8]
