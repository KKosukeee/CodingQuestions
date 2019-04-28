"""
Solution for 3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    """
    Runtime: 92 ms, faster than 52.52% of Python3 online submissions for Longest Substring Without
        Repeating Characters.
    Memory Usage: 12.9 MB, less than 6.24% of Python3 online submissions for Longest Substring
        Without Repeating Characters.
    """
    def lengthOfLongestSubstring(self, s):
        """
        Given a string, find the length of the longest substring without repeating characters.

        Example 1:

        Input: "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.
        Example 2:

        Input: "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.
        Example 3:

        Input: "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
                     Note that the answer must be a substring, "pwke" is a subsequence and
                     not a substring
        Args:
            s: String to find the longest substring from

        Returns:
            int: length of the longest substring without the repeats
        """
        # Initialize hash_table
        hash_table = set()

        # Initialize maximum
        maximum = 0
        i, j = 0, 0

        # Loop, while i and j < len(s)
        while i < len(s) and j < len(s):
            # If hash_table contains s[j], then move i one to the right
            if s[j] in hash_table:

                # Remove s[i] from hash_table
                hash_table.remove(s[i])

                i += 1

            # Otherwise, move j one to the right
            else:

                # Add s[j] to hash_table
                hash_table.add(s[j])

                j += 1

                # Assign maximum with max(maximum, j - i)
                maximum = max(maximum, j - i)

        # Return maximum
        return maximum
