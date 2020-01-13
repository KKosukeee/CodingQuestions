"""
Solution for 721. Accounts Merge
https://leetcode.com/problems/accounts-merge/
"""
from collections import defaultdict
from typing import List

class Solution:
  """
  Runtime: 244 ms, faster than 44.73% of Python3 online submissions for Accounts Merge.
  Memory Usage: 27.5 MB, less than 11.11% of Python3 online submissions for Accounts Merge.
  """
  def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
    """
    Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

    Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

    After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

    Example 1:
    Input:
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
    Explanation:
    The first and third John's are the same person as they have the common email "johnsmith@mail.com".
    The second John and Mary are different people as none of their email addresses are used by other accounts.
    We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
    ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
    Note:

    The length of accounts will be in the range [1, 1000].
    The length of accounts[i] will be in the range [1, 10].
    The length of accounts[i][j] will be in the range [1, 30].

    Args:
      accounts:

    Returns:

    """
    return self.union_find(accounts)

  def dfs(self, accounts: List[List[str]]) -> List[List[str]]:
    """
    A DFS solution that runs in O(NM) in time and O(N+M) in space where N = #
    of accounts and M = # of emails

    Args:
      accounts:

    Returns:

    """
    name_map = {}
    graph = defaultdict(list)
    for account in accounts:
      for email in account[1:]:
        graph[account[1]].append(email)
        graph[email].append(account[1])
        name_map[email] = account[0]

    seen = set()
    res = []

    for email in graph:
      if email not in seen:
        seen.add(email)
        stack = [email]
        emails = []

        while stack:
          node = stack.pop()
          emails.append(node)

          for neigh in graph[node]:
            if neigh not in seen:
              seen.add(neigh)
              stack.append(neigh)
        res.append([name_map[email]] + sorted(emails))
    return res

  def union_find(self, accounts: List[List[str]]) -> List[List[str]]:
    """
    

    Args:
      accounts:

    Returns:

    """
    parents, rank = list(range(10001)), [0] * 10001

    def find(p):
      if parents[p] != p:
        parents[p] = find(parents[p])
      return parents[p]

    def union(p, q):
      p1, p2 = find(p), find(q)
      if p1 == p2:
        return
      if rank[p1] > rank[p2]:
        parents[p2] = p1
      elif rank[p1] < rank[p2]:
        parents[p1] = p2
      else:
        parents[p1] = p2
        rank[p2] += 1

    email_to_name = {}
    email_to_id = {}
    i = 0

    for account in accounts:
      for email in account[1:]:
        email_to_name[email] = account[0]
        if email not in email_to_id:
          email_to_id[email] = i
          i += 1
        union(email_to_id[account[1]], email_to_id[email])

    id_to_emails = defaultdict(list)
    for email in email_to_name:
      id_to_emails[find(email_to_id[email])].append(email)

    return [[email_to_name[v[0]]] + sorted(v) for v in id_to_emails.values()]
