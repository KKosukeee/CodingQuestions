"""
Solution for 5207. Get Equal Substrings Within Budget
https://leetcode.com/contest/weekly-contest-156/problems/get-equal-substrings-within-budget/
"""

class Solution(object):
    """
    Runtime: 100 ms, faster than 100.00% of Python online submissions for Get Equal Substrings Within Budget.
    Memory Usage: 19.9 MB, less than 100.00% of Python online submissions for Get Equal Substrings Within Budget.
    """
    def initial_solution(self, s, t, maxCost):
        """
        Initial solution that runs in O(N) in time and O(1) in space

        Args:
            s(str):
            t(str):
            maxCost(int):

        Returns:
            int:

        """
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        cum_sum = [0]
        for i in range(len(costs)):
            cum_sum.append(cum_sum[-1] + costs[i])
        start, end, max_len = 0, 1, 0
        while end < len(cum_sum):
            if not maxCost - (cum_sum[end] - cum_sum[start]) >= 0:
                while start <= end and maxCost - (cum_sum[end] - cum_sum[start]) < 0:
                    start += 1
            if maxCost - (cum_sum[end] - cum_sum[start]) >= 0:
                max_len = max(max_len, end - start)
            end += 1
        return max_len

    def cleaner_solution(self, s, t, maxCost):
        """
        Slightly cleaner solution that runs in O(N) in time and O(1) in space

        Args:
            s(str):
            t(str):
            maxCost(int):

        Returns:
            int:

        """
        i, max_len = 0, 0
        for j in range(len(s)):
            maxCost -= abs(ord(s[j]) - ord(t[j]))
            if maxCost < 0:
                maxCost += abs(ord(s[i]) - ord(t[i]))
                i += 1
            if maxCost >= 0:
                max_len = max(max_len, j - i + 1)
        return max_len

    def equalSubstring(self, s, t, maxCost):
        """
        You are given two strings s and t of the same length. You want to change s to t. Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is, the absolute difference between the ASCII values of the characters.

        You are also given an integer maxCost.

        Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of twith a cost less than or equal to maxCost.

        If there is no substring from s that can be changed to its corresponding substring from t, return 0.



        Example 1:

        Input: s = "abcd", t = "bcdf", cost = 3
        Output: 3
        Explanation: "abc" of s can change to "bcd". That costs 3, so the maximum length is 3.
        Example 2:

        Input: s = "abcd", t = "cdef", cost = 3
        Output: 1
        Explanation: Each charactor in s costs 2 to change to charactor in t, so the maximum length is 1.
        Example 3:

        Input: s = "abcd", t = "acde", cost = 0
        Output: 1
        Explanation: You can't make any change, so the maximum length is 1.


        Constraints:

        1 <= s.length, t.length <= 10^5
        0 <= maxCost <= 10^6
        s and t only contain lower case English letters.

        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        return self.initial_solution(s, t, maxCost)

    """
           *
    s = "abcd"
    t = "bcdf"
    cost = 3
         *
    [1,1,1,2]
  [0,1,2,3,5]
   |-----|
    """
