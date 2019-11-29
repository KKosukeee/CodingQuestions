"""
Solution for 186. Reverse Words in a String II
https://leetcode.com/problems/reverse-words-in-a-string-ii/
"""
from typing import List

class Solution:
  def linear_solution(self, s: List[str]) -> None:
    """
    A solution that runs in linear in time and space
    """
    i, j = 0, len(s) - 1
    o1, o2 = 0, 0
    hash_map = {}

    while i <= j:
      start, end = [], []
      while i < len(s) and s[i] != ' ':
        start.append(i)
        i += 1
      while j >= 0 and s[j] != ' ':
        end.append(j)
        j -= 1
      # if i <= j:
      while start:
        hash_map[start.pop()] = (len(s) - 1) + o2
        o2 -= 1
      while end:
        hash_map[end.pop()] = o1
        o1 += 1
      hash_map[i] = (len(s) - 1) + o2
      hash_map[j] = o1
      o1, o2 = o1 + 1, o2 - 1
      i, j = i + 1, j - 1
    test = [''] * len(s)
    for i in range(len(s)):
      test[hash_map[i]] = s[i]
    s[:] = test

  def reverse_solution(self, s: List[str]) -> None:
    """
    A solution that runs in linear in time and constant in space

    Args:
      s:

    Returns:

    """
    s.reverse()
    i = 0
    for j in range(len(s)):
      if s[j] == ' ':
        self.reverse(s, i, j - 1)
        i = j + 1
    self.reverse(s, i, len(s) - 1)

  def reverse(self, s, i, j):
    while i <= j:
      s[i], s[j] = s[j], s[i]
      i, j = i + 1, j - 1

  def reverseWords(self, s: List[str]) -> None:
    """
    Given an input string , reverse the string word by word.

    Example:

    Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
    Note:

    A word is defined as a sequence of non-space characters.
    The input string does not contain leading or trailing spaces.
    The words are always separated by a single space.
    Follow up: Could you do it in-place without allocating extra space?

    Args:
      s:

    Returns:

    """
    self.reverse_solution(s)

  """
   *       * 
  The sky is

  Initial solution
  T: O(N^2), S: O(N)
  1. Initialize two stacks
  2. Loop while the current char isn't empty
    2.1 Increment the pointer by one
  3. Loop while the current char isn't empty
    3.1 Decrement the pointer by one
  4. Check if i didn't exceed the j
    4.1 If it's valid, pop the element from stacks
    4.2 Compare the length of two elements
    4.3 Shift the list by the difference in length
    4.4 Swap the word in place

  Second solution
  Index mapping
  T: O(N), S: O(N)
  1. Initialize a variable for recording offset
  2. Loop while the current char isn't empty
    2.1 Increment the pointer by one
    2.2 Create a map with the current i and calculate new index
  3. Loop while the current char isn't empty
    3.1 Decrement the pointer by one
    3.2 Create a map with the current j and calculate new index
  4. Add and subtract the offset for a space
  5. Loop through input string
    5.1 Assign s[map[i]] = s[i]
  """
