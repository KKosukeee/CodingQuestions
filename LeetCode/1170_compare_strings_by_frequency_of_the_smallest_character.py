"""
Solution for 1170. Compare Strings by Frequency of the Smallest Character
https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/
"""
from collections import Counter
import bisect

class Solution:
    """
    Runtime: 120 ms, faster than 62.50% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.
    Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.
    """
    def numSmallerByFrequency(self, queries, words):
        """
        Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

        Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.



        Example 1:

        Input: queries = ["cbd"], words = ["zaaaz"]
        Output: [1]
        Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
        Example 2:

        Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
        Output: [1,2]
        Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").


        Constraints:

        1 <= queries.length <= 2000
        1 <= words.length <= 2000
        1 <= queries[i].length, words[i].length <= 10
        queries[i][j], words[i][j] are English lowercase letters.
        Args:
            queries(list[str]):
            words(list[str]):

        Returns:
            list[int]:
        """
        result, freq = [], []
        for word in words:
            freq.append(Counter(word)[min(word)])
        freq.sort()
        for query in queries:
            count = Counter(query)[min(query)]
            result.append(len(freq) - bisect.bisect(freq, count))
        return result
