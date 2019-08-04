"""
Solution for 1023. Camelcase Matching
https://leetcode.com/problems/camelcase-matching/
"""
class Solution:
    """
    Runtime: 36 ms, faster than 80.25% of Python3 online submissions for Camelcase Matching.
    Memory Usage: 13.8 MB, less than 7.14% of Python3 online submissions for Camelcase Matching.
    """
    def camelMatch(self, queries, pattern):
        """
        A query word matches a given pattern if we can insert lowercase letters to the pattern word so that it equals the query. (We may insert each character at any position, and may insert 0 characters.)

        Given a list of queries, and a pattern, return an answer list of booleans, where answer[i] is true if and only if queries[i] matches the pattern.



        Example 1:

        Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
        Output: [true,false,true,true,false]
        Explanation:
        "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
        "FootBall" can be generated like this "F" + "oot" + "B" + "all".
        "FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
        Example 2:

        Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
        Output: [true,false,true,false,false]
        Explanation:
        "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
        "FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
        Example 3:

        Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
        Output: [false,true,false,false,false]
        Explanation:
        "FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".


        Note:

        1 <= queries.length <= 100
        1 <= queries[i].length <= 100
        1 <= pattern.length <= 100
        All strings consists only of lower and upper case English letters.
        Args:
            queries: list<str>
            pattern: str

        Returns:
            list<bool>:
        """
        matches = []
        for query in queries:
            i = 0
            is_match = True
            for char in query:
                if i < len(pattern) and pattern[i] == char:
                    i += 1
                elif char.isupper():
                    is_match = False
                    break
            matches.append(is_match and not i < len(pattern))
        return matches
