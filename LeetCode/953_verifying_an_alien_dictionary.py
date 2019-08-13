"""
Solution for 953. Verifying an Alien Dictionary
https://leetcode.com/problems/verifying-an-alien-dictionary/
"""
class Solution:
    """
    Runtime: 44 ms, faster than 61.38% of Python3 online submissions for Verifying an Alien Dictionary.
    Memory Usage: 14 MB, less than 5.55% of Python3 online submissions for Verifying an Alien Dictionary.
    """
    def isAlienSorted(self, words, order):
        """
        In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

        Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.



        Example 1:

        Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
        Output: true
        Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
        Example 2:

        Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
        Output: false
        Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
        Example 3:

        Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
        Output: false
        Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


        Note:

        1 <= words.length <= 100
        1 <= words[i].length <= 20
        order.length == 26
        All characters in words[i] and order are english lowercase letters.
        Args:
            words(list[str]):
            order(str):

        Returns:
            bool:
        """
        word_dict = {char: i for i, char in enumerate(order)}
        for i in range(len(words)-1):
            first = words[i]
            second = words[i+1]
            j, k = 0, 0
            for j in range(min(len(first), len(second))):
                if first[j] != second[j]:
                    if word_dict[first[j]] > word_dict[second[j]]:
                        return False
                    break
            else:
                if len(first) > len(second):
                    return False
        return True
