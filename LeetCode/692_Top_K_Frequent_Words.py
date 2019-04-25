"""
Solution for 692. Top K Frequent Words
https://leetcode.com/problems/top-k-frequent-words/
"""

from collections import Counter
import heapq


class Solution:
    """
    Runtime: 44 ms, faster than 93.95% of Python3 online submissions for Top K Frequent Words.
    Memory Usage: 13.2 MB, less than 5.82% of Python3 online submissions for Top K Frequent Words.
    """
    def topKFrequent(self, words, k):
        """
        Given a non-empty list of words, return the k most frequent elements.

        Your answer should be sorted by frequency from highest to lowest. If two words have the
        same frequency, then the word with the lower alphabetical order comes first.

        Example 1:
        Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
        Output: ["i", "love"]
        Explanation: "i" and "love" are the two most frequent words.
            Note that "i" comes before "love" due to a lower alphabetical order.
        Example 2:
        Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
        Output: ["the", "is", "sunny", "day"]
        Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
            with the number of occurrence being 4, 3, 2 and 1 respectively.
        Args:
            words: an array contained words which you get kth most frequent word from
            k: get kth most frequent word according to it's value

        Returns:
            list: containing kth most frequent words in the array
        """
        # Create a counter -> O(n)
        counter = Counter(words)

        # Create a counter where the frequency flipped
        heap = [(-frequency, word) for word, frequency in counter.items()]

        # Creare a min-heap
        heapq.heapify(heap)

        # Return k most word in the heap
        return [heapq.heappop(heap)[1] for _ in range(k)]
