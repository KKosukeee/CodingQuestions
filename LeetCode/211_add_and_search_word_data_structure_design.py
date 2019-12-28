"""
Solution for 211. Add and Search Word - Data structure design
https://leetcode.com/problems/add-and-search-word-data-structure-design/
"""
class WordDictionary:
  """
  Runtime: 344 ms, faster than 59.04% of Python3 online submissions for Add and Search Word - Data structure design.
  Memory Usage: 23.6 MB, less than 73.91% of Python3 online submissions for Add and Search Word - Data structure design.
  """
  def __init__(self):
    """
    Design a data structure that supports the following two operations:

    void addWord(word)
    bool search(word)
    search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

    Example:

    addWord("bad")
    addWord("dad")
    addWord("mad")
    search("pad") -> false
    search("bad") -> true
    search(".ad") -> true
    search("b..") -> true
    Note:
    You may assume that all words are consist of lowercase letters a-z.

    Initialize your data structure here.
    """
    self.trie = {}
    self.end = '*'

  def addWord(self, word: str) -> None:
    """
    Adds a word into the data structure.
    """
    root = self.trie
    for char in word:
      if char not in root:
        root[char] = {}
      root = root[char]
    root[self.end] = {}

  def search(self, word: str) -> bool:
    """
    Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
    """
    def dfs(i, root):
      if i >= len(word):
        return self.end in root
      if word[i] != '.' and word[i] not in root:
        return False
      if word[i] == '.':
        return any(dfs(i+1, root[k]) for k in root)
      return dfs(i+1, root[word[i]])
    return dfs(0, self.trie)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)