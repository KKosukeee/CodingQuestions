"""
Solution for 937. Reorder Data in Log Files
https://leetcode.com/problems/reorder-data-in-log-files/
"""
from typing import List

class Solution:
  """
  Runtime: 28 ms, faster than 99.54% of Python3 online submissions for Reorder Data in Log Files.
  Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Reorder Data in Log Files.
  """

  def first_solution(self, logs: List[str]) -> List[str]:
    """
    A first solution that runs in O(Nlog(N)) in time and O(N) in space

    Args:
      logs:

    Returns:

    """
    letter_logs, digit_logs = [], []
    for log in logs:
      if log[-1].isdigit():
        digit_logs.append(log)
      else:
        letter_logs.append(log)
    letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letter_logs + digit_logs

  def shorter_solution(self, logs: List[str]) -> List[str]:
    """
    A second solution that runs in same as the first solution

    Args:
      logs:

    Returns:

    """
    def key_func(log):
      id_, info = log.split(' ', 1)
      return (0, info, id_) if log[-1].isalpha() else (1,)

    return sorted(logs, key=key_func)

  def reorderLogFiles(self, logs: List[str]) -> List[str]:
    """
    You have an array of logs.  Each log is a space delimited string of words.

    For each log, the first word in each log is an alphanumeric identifier.  Then, either:

    Each word after the identifier will consist only of lowercase letters, or;
    Each word after the identifier will consist only of digits.
    We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

    Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

    Return the final order of the logs.



    Example 1:

    Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]


    Constraints:

    0 <= logs.length <= 100
    3 <= logs[i].length <= 100
    logs[i] is guaranteed to have an identifier, and a word after the identifier.

    Args:
      logs:

    Returns:

    """
    return self.shorter_solution(logs)
