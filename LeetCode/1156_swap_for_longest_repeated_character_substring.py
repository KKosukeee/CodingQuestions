"""
Solution for 1156. Swap For Longest Repeated Character Substring
https://leetcode.com/problems/swap-for-longest-repeated-character-substring/
"""
import itertools
from collections import Counter

class Solution:
    """
    Runtime: 68 ms, faster than 86.98% of Python3 online submissions for Swap For Longest Repeated Character Substring.
    Memory Usage: 15.1 MB, less than 100.00% of Python3 online submissions for Swap For Longest Repeated Character Substring.
    """
    def maxRepOpt1(self, text):
        """
        Given a string text, we are allowed to swap two of the characters in the string. Find the length of the longest substring with repeated characters.



        Example 1:

        Input: text = "ababa"
        Output: 3
        Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa", which its length is 3.
        Example 2:

        Input: text = "aaabaaa"
        Output: 6
        Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa", which its length is 6.
        Example 3:

        Input: text = "aaabbaaa"
        Output: 4
        Example 4:

        Input: text = "aaaaa"
        Output: 5
        Explanation: No need to swap, longest repeated character substring is "aaaaa", length is 5.
        Example 5:

        Input: text = "abcdef"
        Output: 1


        Constraints:

        1 <= text.length <= 20000
        text consist of lowercase English characters only.
        Args:
            text(str):

        Returns:
            int:
        """
        group = [(k, len(list(g))) for k, g in itertools.groupby(text)]
        counter = Counter(text)
        count = max(min(g+1, counter[k]) for k, g in group)
        for i in range(1, len(group)-1):
            if group[i-1][0] == group[i+1][0] and group[i][1] == 1:
                count = max(count, min(group[i-1][1] + group[i+1][1]+1, counter[group[i+1][0]]))
        return count
