"""
Solution for 648. Replace Words
https://leetcode.com/problems/replace-words/
"""
from typing import List
from collections import defaultdict

class Solution:
    """
    Runtime: 84 ms, faster than 79.35% of Python3 online submissions for Replace Words.
    Memory Usage: 28.6 MB, less than 50.00% of Python3 online submissions for Replace Words.
    """
    def brute_force(self, dict: List[str], sentence: str) -> str:
        """
        Brute force solution that I come up with

        Args:
            dict(list[str]):
            sentence(str):

        Returns:
            str:

        """
        words = sentence.split()
        dict.sort(key=lambda x: (x, len(x)))
        for i, word in enumerate(words):
            new_word = list(filter(lambda x: word.startswith(x), dict))
            if len(new_word) > 0:
                words[i] = new_word[0]
        return ' '.join(words)

    def sub_optimal(self, dict: List[str], sentence: str) -> str:
        """
        Slightly better solution which runs in O(M + W^2) where M = len(dict) W = max(len(word)in sentence)

        Args:
            dict(list[str]):
            sentence(str):

        Returns:
            str:

        """
        dict_set = set(dict)

        def replace(word):
            """
            Replace the word which runs in O(W^2)

            Args:
                word(str):

            Returns:
                str:

            """
            for i in range(1, len(word) + 1):
                if word[:i] in dict_set:
                    return word[:i]
            return word

        return ' '.join(map(replace, sentence.split()))

    def optimal(self, roots, sentence):
        """
        Optimal solution which runs in O(Mm + Nn) where M = len(roots), m = len(roots[i])
                                                        N = len(sentence), n = len(word)

        Args:
            roots(list[str]):
            sentence(str):

        Returns:
            str:

        """
        TRIE = lambda: defaultdict(TRIE)
        END = True
        trie = TRIE()

        for root in roots:
            current = trie
            for char in root:
                current = current[char]
            current[END] = root

        def replace(word):
            """
            Replace the string. This runs in O(n)

            Args:
                word:

            Returns:

            """
            current = trie
            for char in word:
                if char not in current:
                    break
                current = current[char]
                if END in current:
                    return current[END]
            return word

        return ' '.join(map(replace, sentence.split()))

    # M, N = len(dict), len(words in sentence)
    # O(M) + O(N^2)
    # dict = ['cat', 'can', 'cum', 'fat']
    # 1:      |-----------------|
    # 2:      |----------|
    # 3:             |---|
    # sort = ['can', 'cat', 'cum', 'fat']
    #             *
    # sent = 'the cat can fly like cum'

    # dict = ["cat", "bat", "rat"]
    # sort = ["bat", "cat", "rat"]
    # sent = "the cattle was rattled by the battery"
    # word = ["the", "cattle", "was", "rattled", "by", "the", "battery"]from functools import reduce