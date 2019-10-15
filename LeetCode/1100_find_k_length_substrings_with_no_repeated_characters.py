"""
Solution for 1100. Find K-Length Substrings With No Repeated Characters
https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/
"""

class Solution(object):
    """
    Runtime: 32 ms, faster than 87.31% of Python online submissions for Find K-Length Substrings With No Repeated Characters.
    Memory Usage: 12 MB, less than 33.33% of Python online submissions for Find K-Length Substrings With No Repeated Characters.
    """
    def while_loop(self, S, K):
        """
        A solution using a while-loop which runs in O(N) in time and O(K) in space

        :type S: str
        :type K: int
        :rtype: int
        """
        if len(S) < K:
            return 0
        window_set = set()
        i, j, count = 0, 0, 0
        while i < len(S) and j < len(S):
            if S[j] in window_set:
                while i < j and S[j] in window_set:
                    window_set.remove(S[i])
                    i += 1
            window_set.add(S[j])
            if j - i + 1 == K and len(window_set) == K:
                window_set.remove(S[i])
                i, count = i + 1, count + 1
            j += 1
        return count

    def for_loop(self, S, K):
        """
        A solution using a for-loop which runs in O(N) in time and O(K) in space

        :type S: str
        :type K: int
        :rtype: int
        """
        if len(S) < K:
            return 0
        i, count = 0, 0
        window_set = set()
        for j in range(len(S)):
            if S[j] in window_set:
                while i < j and S[j] in window_set:
                    window_set.remove(S[i])
                    i += 1
            window_set.add(S[j])
            if len(window_set) == K and j - i + 1 == K:
                window_set.remove(S[i])
                i, count = i + 1, count + 1
            j += 1
        return count

    def numKLenSubstrNoRepeats(self, S, K):
        """
        Given a string S, return the number of substrings of length K with no repeated characters.



        Example 1:

        Input: S = "havefunonleetcode", K = 5
        Output: 6
        Explanation:
        There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.
        Example 2:

        Input: S = "home", K = 5
        Output: 0
        Explanation:
        Notice K can be larger than the length of S. In this case is not possible to find any substring.


        Note:

        1 <= S.length <= 10^4
        All characters of S are lowercase English letters.
        1 <= K <= 10^4

        :type S: str
        :type K: int
        :rtype: int
        """
        return self.for_loop(S, K)

    """
    Sliding window approach
    1. Initialize a set
    2. Initialize two pointers, one pointing
    3. While the j - i + 1 < increment the end pointer j
        3.1 Add the char pointed by j into the set
        3.2 If the length of the set == K
            3.2.1 Increment the returning counter
            3.2.2 Increment the starting pointer, i
        3.3 If the length of the set != j - i + 1, try incrementing the start pointer i
            3.3.1 Loop while set != j - i + 1 and keep incrementing i
            3.3.2 Remove char pointed by i
        3.4 Keep incrementing the j by 1. 
    """