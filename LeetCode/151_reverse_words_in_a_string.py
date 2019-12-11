"""
Solution for 151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/
"""
from collections import deque

class Solution:
  """
  Runtime: 16 ms, faster than 99.88% of Python3 online submissions for Reverse Words in a String.
  Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Reverse Words in a String.
  """
  def initial_solution(self, s: str) -> str:
    """
    An initial solutio that runs in O(N) in time and space

    Args:
      s:

    Returns:

    """
    return ' '.join(s.split()[::-1])

  def readable_solution(self, s: str) -> str:
    """
    A readable solution that runs O(N) in time and space

    Args:
      s:

    Returns:

    """
    words = s.split()
    for i in range(len(words) // 2):
      j = len(words) - i - 1
      words[i], words[j] = words[j], words[i]
    return ' '.join(words)

  def reverse_reversed_string(self, s: str) -> str:
    """
    A reverse reversed string solution that runs in O(N) in time and space

    Args:
      s:

    Returns:

    """
    reversed_words = s[::-1].split()
    return ' '.join(word[::-1] for word in reversed_words)

  def deque_solution(self, s: str) -> str:
    """
    A deque solution that runs in O(N) in time and space

    Args:
      s:

    Returns:

    """
    q = deque()
    for word in s.split():
      q.appendleft(word)
    return ' '.join(q)

  def reverseWords(self, s: str) -> str:
    """
    Given an input string, reverse the string word by word.



    Example 1:

    Input: "the sky is blue"
    Output: "blue is sky the"
    Example 2:

    Input: "  hello world!  "
    Output: "world! hello"
    Explanation: Your reversed string should not contain leading or trailing spaces.
    Example 3:

    Input: "a good   example"
    Output: "example good a"
    Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


    Note:

    A word is defined as a sequence of non-space characters.
    Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
    You need to reduce multiple spaces between two words to a single space in the reversed string.


    Follow up:

    For C programmers, try to solve it in-place in O(1) extra space.

    Args:
      s:

    Returns:

    """
    return self.deque_solution(s)
