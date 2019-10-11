"""
Solution for 792. Number of Matching Subsequences
https://leetcode.com/problems/number-of-matching-subsequences/
"""
from collections import defaultdict

class Solution(object):
    """
    Runtime: 476 ms, faster than 76.33% of Python online submissions for Number of Matching Subsequences.
    Memory Usage: 13.5 MB, less than 100.00% of Python online submissions for Number of Matching Subsequences.
    """
    def greedy_solution(self, S, words):
        """
        Simple solution that runs in O(len(S) * len(words)) in worst case, O(S) in space

        :type S: str
        :type words: List[str]
        :rtype: int
        """
        hash_map = defaultdict(list)
        for i, c in enumerate(S):
            hash_map[c].append(i)
        inv_count = 0
        for word in words:
            prev = -1
            pointers = defaultdict(int)
            for char in word:
                if not pointers[char] < len(hash_map[char]):
                    inv_count += 1
                    break
                indices = hash_map[char]
                if indices[pointers[char]] <= prev:
                    while pointers[char] < len(hash_map[char]) and indices[pointers[char]] <= prev:
                        pointers[char] += 1
                    if pointers[char] < len(hash_map[char]) and indices[pointers[char]] > prev:
                        prev = indices[pointers[char]]
                        pointers[char] += 1
                        continue
                    inv_count += 1
                    break
                prev = indices[pointers[char]]
                pointers[char] += 1
        return len(words) - inv_count

    def better_solution(self, S, words):
        """
        Better solution that runs in O(len(S) + sum(words[i])) in time and O(sum(words[i])) in space

        :type S: str
        :type words: List[str]
        :rtype: int
        """
        answer = 0
        bucket = defaultdict(list)
        for word in words:
            it = iter(word)
            bucket[next(it)].append(it)

        for char in S:
            old_bucket = bucket[char]
            bucket[char] = []
            while old_bucket:
                it = old_bucket.pop()
                c = next(it, None)
                if not c:
                    answer += 1
                else:
                    bucket[c].append(it)
        return answer

    def numMatchingSubseq(self, S, words):
        """
        Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

        Example :
        Input:
        S = "abcde"
        words = ["a", "bb", "acd", "ace"]
        Output: 3
        Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
        Note:

        All words in words and S will only consists of lowercase letters.
        The length of S will be in the range of [1, 50000].
        The length of words will be in the range of [1, 5000].
        The length of words[i] will be in the range of [1, 50].

        :type S: str
        :type words: List[str]
        :rtype: int
        """
        return self.better_solution(S, words)

    """
    Assumption
    1. # of words in words is always <= len(words)
    2. Any word in words need to be monotonically increasing index order

    Simple approach
    1. Create dictionary on S holding the last occurence of each char
    2. Loop through the words
        2.1 Loop through each char in word
            2.1.1 Look up the current char's index and store the in the var
            2.1.2 If the current char's index is less than the previous, increment the invalid count
            2.1.3 If the current char's index is greater than the previos, keep looping
    3. Return the len(words) - invalid

    abcb
    bc,cb
    """