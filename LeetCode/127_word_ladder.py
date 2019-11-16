"""
Solution for 127. Word Ladder
https://leetcode.com/problems/word-ladder/
"""
from collections import defaultdict
from collections import deque
from typing import List

class Solution:
  """
  Runtime: 116 ms, faster than 91.10% of Python3 online submissions for Word Ladder.
  Memory Usage: 16.1 MB, less than 44.83% of Python3 online submissions for Word Ladder.
  """
  def bfs(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    A BFS solution that runs in O(MN) where M == len(wordList) and
    N == len(wordList[i]) in time and space

    Args:
      beginWord:
      endWord:
      wordList:

    Returns:

    """
    adjacent_words = defaultdict(list)
    for word in wordList:
      for i in range(len(word)):
        adjacent_words[word[:i] + '*' + word[i + 1:]].append(word)
    visited = set([beginWord])
    queue = deque([(beginWord, 1)])
    while queue:
      original, level = queue.popleft()
      for i in range(len(original)):
        word = original[:i] + '*' + original[i + 1:]
        for neighbour in adjacent_words[word]:
          if neighbour == endWord:
            return level + 1
          if neighbour not in visited:
            visited.add(neighbour)
            queue.append((neighbour, level + 1))
    return 0

  def bidirectional_bfs(self, beginWord: str, endWord: str,
                        wordList: List[str]) -> int:
    """
    A bi-directional BFS solution that runs same as the BFS in terms of time and
    space complexity

    Args:
      beginWord:
      endWord:
      wordList:

    Returns:

    """
    if endWord not in wordList or not endWord or not beginWord or not wordList:
      return 0
    adjacent_words = defaultdict(list)
    for word in wordList:
      for i in range(len(word)):
        adjacent_words[word[:i] + '*' + word[i + 1:]].append(word)

    def bfs(queue, visited, other_visited):
      original, level = queue.popleft()
      for i in range(len(original)):
        token = original[:i] + '*' + original[i + 1:]
        for word in adjacent_words[token]:
          if word in other_visited:
            return other_visited[word] + level
          if word not in visited:
            visited[word] = level + 1
            queue.append((word, level + 1))
      return None

    begin_queue, end_queue = deque([(beginWord, 1)]), deque([(endWord, 1)])
    begin_visited, end_visited = {beginWord: 1}, {endWord: 1}
    while begin_queue and end_queue:
      begin = bfs(begin_queue, begin_visited, end_visited)
      if begin:
        return begin
      end = bfs(end_queue, end_visited, begin_visited)
      if end:
        return end
    return 0

  def ladderLength(self, beginWord: str, endWord: str,
                   wordList: List[str]) -> int:
    """
        Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

        Only one letter can be changed at a time.
        Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
        Note:

        Return 0 if there is no such transformation sequence.
        All words have the same length.
        All words contain only lowercase alphabetic characters.
        You may assume no duplicates in the word list.
        You may assume beginWord and endWord are non-empty and are not the same.
        Example 1:

        Input:
        beginWord = "hit",
        endWord = "cog",
        wordList = ["hot","dot","dog","lot","log","cog"]

        Output: 5

        Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
        return its length 5.
        Example 2:

        Input:
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]

        Output: 0

        Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
        Args:
          beginWord:
          endWord:
          wordList:

        Returns:

        """
    return self.bfs(beginWord, endWord, wordList)

  """
  DP:
  1. Given the endWord, find the closest word in the wordList
  2. Do the 1 until the beginWord is reached

  Condition
  - If endWord doesn't exist in the wordList, return 0
  - If there isn't any word with difference of 1 with the given current word in wordList[i], return 0

  Adjacent approach

  """