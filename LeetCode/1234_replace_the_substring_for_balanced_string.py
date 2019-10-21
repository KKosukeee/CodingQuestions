"""
Solution for 1234. Replace the Substring for Balanced String
https://leetcode.com/problems/replace-the-substring-for-balanced-string/
"""
from collections import Counter

class Solution(object):
    """
    Runtime: 664 ms, faster than 100.00% of Python online submissions for Replace the Substring for Balanced String.
    Memory Usage: 15.7 MB, less than 100.00% of Python online submissions for Replace the Substring for Balanced String.
    """
    def first_solution(self, s):
        """
        A first solution that runs O(N) in time and O(1) in space

        :type s: str
        :rtype: int
        """
        counter = Counter(s)
        target = len(s) // 4
        j, res = 0, len(s)
        chars = ('Q', 'R', 'E', 'W')
        for i in range(len(s)):
            while j < len(s) and not all(counter[char] <= target for char in chars):
                counter[s[j]] -= 1
                j += 1
            if all(counter[char] <= target for char in chars):
                res = min(res, j - i)
            counter[s[i]] += 1
        return res

    def better_solution(self, s):
        """
        Slightly better solution that runs O(N) in time and O(1) in space

        :type s: str
        :rtype: int
        """
        counter = Counter(s)
        target = len(s) // 4
        i, res = 0, len(s)

        for j in range(len(s)):
            counter[s[j]] -= 1
            while i < len(s) and all(counter[char] <= target for char in 'QWER'):
                res = min(res, j - i + 1)
                counter[s[i]] += 1
                i += 1
        return res

    def balancedString(self, s):
        """
        You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.

        A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.

        Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.

        Return 0 if the string is already balanced.



        Example 1:

        Input: s = "QWER"
        Output: 0
        Explanation: s is already balanced.
        Example 2:

        Input: s = "QQWE"
        Output: 1
        Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
        Example 3:

        Input: s = "QQQW"
        Output: 2
        Explanation: We can replace the first "QQ" to "ER".
        Example 4:

        Input: s = "QQQQ"
        Output: 3
        Explanation: We can replace the last 3 'Q' to make s = "QWER".


        Constraints:

        1 <= s.length <= 10^5
        s.length is a multiple of 4
        s contains only 'Q', 'W', 'E' and 'R'.

        :type s: str
        :rtype: i
        """
        return self.better_solution(s)

    """
    ! Misunderstanding the problem!!!
    Simple solution
    T: O(N), S: O(1)
    1. Calculate the target length by len(s) // 4
    2. Then count the frequency for each char in Q, W, R and E
    3. Loop through the counter
        3.1 Subtract the count from the target length
        3.2 Increment the difference to the result count
    4. Return the result count

    First solution
    T: O(N), S: O(N)
    1. Get the target count and count the string
    2. Initialize two pointers both pointing the start
    3. Loop the s while j < len(s)
        3.1 Loop while not all chars have frequency less than or equal to the target
            3.1.1 Increment the end pointer j, then subtract 1 from the count
        3.2 Check if the condition checked in 3.1 meets.
            3.2.1 Take the minimum of the length with j - i + 1
    4. Return the minimum length

    """