"""
Solution for 1177. Can Make Palindrome from Substring
https://leetcode.com/problems/can-make-palindrome-from-substring/submissions/
"""
from typing import List
class Solution:
    """
    Runtime: 1340 ms, faster than 65.81% of Python3 online submissions for Can Make Palindrome from Substring.
    Memory Usage: 67.9 MB, less than 100.00% of Python3 online submissions for Can Make Palindrome from Substring.
    """
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        """
        Given a string s, we make queries on substrings of s.

        For each query queries[i] = [left, right, k], we may rearrange the substring s[left], ..., s[right], and then choose up to k of them to replace with any lowercase English letter.

        If the substring is possible to be a palindrome string after the operations above, the result of the query is true. Otherwise, the result is false.

        Return an array answer[], where answer[i] is the result of the i-th query queries[i].

        Note that: Each letter is counted individually for replacement so if for example s[left..right] = "aaa", and k = 2, we can only replace two of the letters.  (Also, note that the initial string s is never modified by any query.)



        Example :

        Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
        Output: [true,false,false,true,true]
        Explanation:
        queries[0] : substring = "d", is palidrome.
        queries[1] : substring = "bc", is not palidrome.
        queries[2] : substring = "abcd", is not palidrome after replacing only 1 character.
        queries[3] : substring = "abcd", could be changed to "abba" which is palidrome. Also this can be changed to "baab" first rearrange it "bacd" then replace "cd" with "ab".
        queries[4] : substring = "abcda", could be changed to "abcba" which is palidrome.


        Constraints:

        1 <= s.length, queries.length <= 10^5
        0 <= queries[i][0] <= queries[i][1] < s.length
        0 <= queries[i][2] <= s.length
        s only contains lowercase English letters.

        Args:
            s(str):
            queries(list[list[str]]):

        Returns:
            list[bool:

        """
        dp = [[0] * 26]
        for i in range(1, len(s) + 1):
            prev = dp[i - 1][:]
            prev[ord(s[i - 1]) - ord('a')] += 1
            dp.append(prev)
        result = []
        for i, j, k in queries:
            if i == j or j - i <= k:
                result.append(True)
                continue
            left, right = dp[i], dp[j + 1]
            total_count = sum((right[i] - left[i]) & 1 for i in range(26))
            result.append(k >= total_count // 2)
        return result

# if left == right -> palindrome
# if right - left == 2 and k = 1 -> palindrome
# if right - left == 3 and k = 2 -> palindrome
# if right - left == N and k = N-1 -> palindrome

# 'aaaacdefg' -> 'cdefg' if k == 2
# 'aaacdefg' -> 'acdefg' if k == 3

# 'aabb' -> 'abba' if k == 0 o
# 'aaab' -> 'aaaa' if k == 1 o
# 'aabc' -> 'baab' if k == 1 o
# 'abcd' -> 'abba' if k == 2 o
# 'abcd' -> 'abbd' if k == 1 x

# If len(s) // 2 == k, then it's a palindrome
# len(unique_chars) is more important than the len(s)
# from collections import Counter
#