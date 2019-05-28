"""
Solution for 890. Find and Replace Pattern
https://leetcode.com/problems/find-and-replace-pattern/
"""

class Solution:
    """
    Runtime: 36 ms, faster than 93.79% of Python3 online submissions for Find and Replace Pattern.
    Memory Usage: 13.3 MB, less than 11.87% of Python3 online submissions for Find and Replace
        Pattern.
    """
    def findAndReplacePattern(self, words, pattern):
        """
        You have a list of words and a pattern, and you want to know which words in words matches
        the pattern.

        A word matches the pattern if there exists a permutation of letters p so that after
        replacing every letter x in the pattern with p(x), we get the desired word.

        (Recall that a permutation of letters is a bijection from letters to letters: every letter
        maps to another letter, and no two letters map to the same letter.)

        Return a list of the words in words that match the given pattern.

        You may return the answer in any order.



        Example 1:

        Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
        Output: ["mee","aqq"]
        Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
        "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
        since a and b map to the same letter.
        Args:
            words: list of string
            pattern: string

        Returns:
            list<str>: all of them must match by the definition with pattern
        """
        def filter_fn(word):
            map1 = {}
            map2 = {}

            for c, p in zip(word, pattern):
                if c not in map1:
                    map1[c] = p

                if p not in map2:
                    map2[p] = c

                if (map1[c], map2[p]) != (p, c):
                    return False

            return True

        return list(filter(filter_fn, words))
