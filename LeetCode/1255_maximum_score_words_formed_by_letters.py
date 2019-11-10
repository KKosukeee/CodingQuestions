"""
Solution for 1255. Maximum Score Words Formed by Letters
https://leetcode.com/problems/maximum-score-words-formed-by-letters/
"""
from collections import Counter
from copy import deepcopy
from typing import List

class Solution:
    """
    Runtime: 124 ms, faster than 50.00% of Python3 online submissions for Maximum Score Words Formed by Letters.
    Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Maximum Score Words Formed by Letters.
    """
    def backtrack(self, words: List[str], letters: List[str], score: List[int]) -> int:
        """

        Args:
            words:
            letters:
            score:

        Returns:

        """
        letter_count = Counter(letters)
        word_score, word_count = {}, {}
        for word in words:
            word_score[word] = sum(
                [score[ord(char) - ord('a')] for char in word])
            word_count[word] = Counter(word)

        def rec(i, letter):
            delta = deepcopy(letter)
            for char in words[i]:
                if char not in delta:
                    return 0
                delta[char] -= 1
            if any(value < 0 for value in delta.values()):
                return 0
            max_score = 0
            for j in range(i + 1, len(words)):
                max_score = max(max_score, rec(j, delta))
            return max_score + word_score[words[i]]

        return max(rec(i, letter_count) for i in range(len(words)))

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        """
        Given a list of words, list of  single letters (might be repeating) and score of every character.

        Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

        It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.



        Example 1:

        Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
        Output: 23
        Explanation:
        Score  a=1, c=9, d=5, g=3, o=2
        Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
        Words "dad" and "dog" only get a score of 21.
        Example 2:

        Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
        Output: 27
        Explanation:
        Score  a=4, b=4, c=4, x=5, z=10
        Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
        Word "xxxz" only get a score of 25.
        Example 3:

        Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
        Output: 0
        Explanation:
        Letter "e" can only be used once.


        Constraints:

        1 <= words.length <= 14
        1 <= words[i].length <= 15
        1 <= letters.length <= 100
        letters[i].length == 1
        score.length == 26
        0 <= score[i] <= 10
        words[i], letters[i] contains only lower case English letters.

        Args:
            words:
            letters:
            score:

        Returns:

        """
        return self.backtrack(words, letters, score)