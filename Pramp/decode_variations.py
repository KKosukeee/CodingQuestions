"""
Solution for Decode Variations
https://www.pramp.com/challenge/r1Kw0vwG6OhK9AEGAy6L
"""
from collections import defaultdict

def brute_force(S):
    """
    A brute-force solution that runs in O(2^N) in tome and space

    Args:
        S(str):

    Returns:
        int:

    """
    if len(S) <= 0:
        return 0
    if S[0] == '0':
        return 0
    if int(S) <= 26:
        return 1 if int(S) <= 10 or S[-1] == '0' else 2
    if int(S[:2]) <= 26:
        return decodeVariations(S[1:]) + decodeVariations(S[2:])
    else:
        return decodeVariations(S[1:])


def top_down(S):
    """
    A top-down solution that runs in O(N) in time and space

    Args:
        S(str):

    Returns:
        int:

    """
    memo = defaultdict(int)

    def rec(s):
        if len(s) <= 0:
            return 0
        if s[0] == '0':
            return 0
        if int(s) <= 26:
            return 1 if int(s) <= 10 or s[-1] == '0' else 2
        if s in memo:
            return memo[s]
        if int(s[:2]) <= 26:
            memo[s] = rec(s[1:]) + rec(s[2:])
            return memo[s]
        else:
            memo[s] = rec(s[1:])
            return memo[s]

    return rec(S)


def bottom_up(S):
    """
    A bottom-up solution that runs in O(N) in time and space

    Args:
        S(str):

    Returns:
        int:

    """
    dp = [1 if S[0] != '0' else 0]
    for i in range(1, len(S)):
        ways = dp[-1] if S[i] != '0' else 0
        if S[i - 1] == '1' or (S[i - 1] == '2' and S[i] <= '6'):
            ways += dp[i - 2] if i - 2 >= 0 else 1
        dp.append(ways)
    return dp[-1]


def optimal(S):
    """
    An optimal solution that runs in O(N) in time and O(1) in space

    Args:
        S(str):

    Returns:
        int:

    """
    pprev, prev = 0, 1 if S[0] != '0' else 0
    for i in range(1, len(S)):
        ways = prev if S[i] != '0' else 0
        if S[i - 1] == '1' or (S[i - 1] == '2' and S[i] <= '6'):
            ways += dp[i - 2] if i - 2 >= 0 else 1
        pprev, prev = prev, ways
    return prev


def decodeVariations(S):
    """
    A letter can be encoded to a number in the following way:

    'A' -> '1', 'B' -> '2', 'C' -> '3', ..., 'Z' -> '26'
    A message is a string of uppercase letters, and it is encoded first using this scheme. For example, 'AZB' -> '1262'

    Given a string of digits S from 0-9 representing an encoded message, return the number of ways to decode it.

    Examples:

    input:  S = '1262'
    output: 3
    explanation: There are 3 messages that encode to '1262': 'AZB', 'ABFB', and 'LFB'.
    Constraints:

    [time limit] 5000ms

    [input] string S

    1 ≤ S.length ≤ 12
    [output] integer

    Args:
        S(str):

    Returns:
        int:

    """
    return bottom_up(S)
