"""
Solution for 294. Flip Game II
https://leetcode.com/problems/flip-game-ii/
"""

class Solution(object):
    """
    Runtime: 76 ms, faster than 56.79% of Python online submissions for Flip Game II.
    Memory Usage: 14.1 MB, less than 25.00% of Python online submissions for Flip Game II.
    """
    def brute_force(self, s):
        """
        A brute force solution that runs in O(N!!) in space and time

        :type s: str
        :rtype: bool
        """
        cand = [i for i in range(len(s) - 1) if s[i:i + 2] == '++']
        if not cand: return False
        return any(not self.canWin(s[:i] + '-' + s[i + 2:]) for i in cand)

    def dp(self, s, memo={}):
        """
        A DP solution that runs O(N!) in time and space perhaps ? :)

        :type s: str
        :rtype: bool
        """
        if s in memo:
            # print('MEMORY: {}'.format(s))
            return memo[s]
        cand = [i for i in range(len(s) - 1) if s[i:i + 2] == '++']
        if not cand:
            memo[s] = False
            return memo[s]
        memo[s] = any(not self.dp(s[:i] + '-' + s[i + 2:], memo) for i in cand)
        return memo[s]

    def canWin(self, s):
        """
        You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

        Write a function to determine if the starting player can guarantee a win.

        Example:

        Input: s = "++++"
        Output: true
        Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
        Follow up:
        Derive your algorithm's runtime complexity.

        :type s: str
        :rtype: bool
        """
        return self.dp(s)

    """
    Brute force
    1. Try to flip all consecutive signs.
    2. Call the function recursively after modifying the input
    3. If there is no move that you can make, then return False
    4. If the current player is you, and recursive one returns False, that means you can win


    """