"""
Solution for 205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/
"""
class Solution:
  """
  Runtime: 44 ms, faster than 74.22% of Python3 online submissions for Isomorphic Strings.
  Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Isomorphic Strings.
  """
  def simple_solution(self, s: str, t: str) -> bool:
    """
    A simple solution that runs in O(N) in time and O(N) in space

    Args:
      s:
      t:

    Returns:

    """
    hash_map, used = {}, set()
    for i in range(len(s)):
      if s[i] not in hash_map:
        if t[i] not in used:
          hash_map[s[i]] = t[i]
          used.add(t[i])
        else:
          return False
      elif hash_map[s[i]] != t[i]:
        return False
    return True

  def better_solution(self, s: str, t: str) -> bool:
    """
    A better solution that runs in O(N) in time and space

    Args:
      s:
      t:

    Returns:

    """
    s_to_t, t_to_s = {}, {}
    for i in range(len(s)):
      if s[i] not in s_to_t:
        s_to_t[s[i]] = t[i]
      elif s_to_t[s[i]] != t[i]:
        return False

      if t[i] not in t_to_s:
        t_to_s[t[i]] = s[i]
      elif t_to_s[t[i]] != s[i]:
        return False
    return True

  def isIsomorphic(self, s: str, t: str) -> bool:
    return self.better_solution(s, t)

  """
  Hash map solution
  1. Loop through s
    1.1 Map s[i] to t[i] if s[i] not exists in hash map
    1.2 Check if s[i] maps to t[i], if it exists, keep,looping if so, otherwise return false
  2. Return false
  """
