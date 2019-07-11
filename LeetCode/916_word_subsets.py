"""
Solution for 916. Word Subsets
"""
from collections import Counter

class Solution:
    """
    Runtime: 1324 ms, faster than 12.43% of Python3 online submissions for Word Subsets.
    Memory Usage: 16 MB, less than 89.52% of Python3 online submissions for Word Subsets.
    """
    def wordSubsets(self, A, B):
        """
        We are given two arrays A and B of words.  Each word is a string of lowercase letters.

        Now, say that word b is a subset of word a if every letter in b occurs in a, including
        multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

        Now say a word a from A is universal if for every b in B, b is a subset of a.

        Return a list of all universal words in A.  You can return the words in any order.



        Example 1:

        Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
        Output: ["facebook","google","leetcode"]
        Example 2:

        Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
        Output: ["apple","google","leetcode"]
        Example 3:

        Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
        Output: ["facebook","google"]
        Example 4:

        Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
        Output: ["google","leetcode"]
        Example 5:

        Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
        Output: ["facebook","leetcode"]
        Args:
            A: list of str to find universal subsets from B
            B: list of str to find universal subsets with A

        Returns:
            list<str>: where each value is one of A as the universal subset
        """
        # Create the counter for b
        b_counter = Counter()

        # Take the maximum occureance for each char
        for b in B:
            b_counter = b_counter | Counter(b)

        # Placeholder for the result
        result = []

        # Check if the word a is the universal or not
        for a in A:
            a_counter = Counter(a)
            if all(a_counter[key] >= b_counter[key] for key in b_counter):
                result.append(a)

        return result