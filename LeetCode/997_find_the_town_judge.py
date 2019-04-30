"""
Solution for 997. Find the Town Judge
https://leetcode.com/problems/find-the-town-judge/
"""
from collections import defaultdict

class Solution:
    """
    Runtime: 108 ms, faster than 82.46% of Python3 online submissions for Find the Town Judge.
    Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Find the Town Judge
    """
    def findJudge(self, N, trust):
        """
        In a town, there are N people labelled from 1 to N.  There is a rumor that one of these
        people is secretly the town judge.

        If the town judge exists, then:

        The town judge trusts nobody.
        Everybody (except for the town judge) trusts the town judge.
        There is exactly one person that satisfies properties 1 and 2.
        You are given trust, an array of pairs trust[i] = [a, b] representing that the person
        labelled a trusts the person labelled b.

        If the town judge exists and can be identified, return the label of the town judge.
        Otherwise, return -1.

        Example 1:

        Input: N = 2, trust = [[1,2]]
        Output: 2
        Example 2:

        Input: N = 3, trust = [[1,3],[2,3]]
        Output: 3
        Example 3:

        Input: N = 3, trust = [[1,3],[2,3],[3,1]]
        Output: -1
        Example 4:

        Input: N = 3, trust = [[1,2],[2,3]]
        Output: -1
        Example 5:

        Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
        Output: 3
        Args:
            N: integer value indicating number of people in the town
            trust: trusted graph represented as adjacency list

        Returns:
            int: indicating which person is a town judge
        """
        # create trust dictionary {person: set(person who trusts)}
        trust_dict = defaultdict(set)

        for connection in trust:
            trust_dict[connection[0]].add(connection[1])

        for i in range(1, N + 1):
            if i not in trust_dict:
                trust_dict[i] = set()

        candidates = set()
        for person, trusted in trust_dict.items():
            if not trusted:
                candidates.add(person)

        # check if candidates is empty
        if len(candidates) == 0:
            return -1

        # check if candidates are more than two
        if len(candidates) >= 2:
            return -1

        candidate = list(candidates)[0]
        # re-evaluate the candidate by looping through trust dict
        for person, trusted in trust_dict.items():
            if person == candidate:
                continue

            # return -1 if the condition property 2 doesn't meet
            if not candidate in trusted:
                return -1

        # return candidate
        return candidate
