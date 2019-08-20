"""
Solution for 884. Uncommon Words from Two Sentence
https://leetcode.com/problems/uncommon-words-from-two-sentences/
"""
from collections import Counter
class Solution:
    """
    Runtime: 32 ms, faster than 94.79% of Python3 online submissions for Uncommon Words from Two Sentences.
    Memory Usage: 14 MB, less than 9.09% of Python3 online submissions for Uncommon Words from Two Sentences.
    """
    def uncommonFromSentences(self, A, B):
        """
        We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

        A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

        Return a list of all uncommon words.

        You may return the list in any order.



        Example 1:

        Input: A = "this apple is sweet", B = "this apple is sour"
        Output: ["sweet","sour"]
        Example 2:

        Input: A = "apple apple", B = "banana"
        Output: ["banana"]


        Note:

        0 <= A.length <= 200
        0 <= B.length <= 200
        A and B both contain only spaces and lowercase letters.
        Args:
            A(str):
            B(str):

        Returns:
            list[str]:
        """
        counter = Counter(A.split()) + Counter(B.split())
        return filter(lambda x: counter[x] == 1, counter)
