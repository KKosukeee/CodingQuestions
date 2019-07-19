"""
Solution for 464. Can I Win
"""

class Solution:
    """
    Runtime: 404 ms, faster than 87.90% of Python3 online submissions for Can I Win.
    Memory Usage: 28.1 MB, less than 38.32% of Python3 online submissions for Can I Win.
    """
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

        What if we change the game so that players cannot re-use integers?

        For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

        Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

        You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

        Example

        Input:
        maxChoosableInteger = 10
        desiredTotal = 11

        Output:
        false

        Explanation:
        No matter which integer the first player choose, the first player will lose.
        The first player can choose an integer from 1 up to 10.
        If the first player choose 1, the second player can only choose integers from 2 up to 10.
        The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
        Same with other integers chosen by the first player, the second player will always win.
        Args:
            maxChoosableInteger: int value to represent a value range that you can take
            desiredTotal: int value to count up to

        Returns:
            bool: True if you can force a win, False otherwise
        """
        seen = {}

        def can_win(choices, remainder):
            """
            Recursive function
            Args:
                choices: tuple<int> as choices that you can take
                remainder: int value after counting some value

            Returns:
                bool: True if this turn can force a win, False otherwise
            """
            if choices[-1] >= remainder:
                return True

            if choices in seen:
                return seen[choices]

            for i in range(len(choices)):
                if not can_win(choices[:i] + choices[i + 1:], remainder - choices[i]):
                    seen[choices] = True
                    return True

            seen[choices] = False
            return seen[choices]

        choices = tuple(range(1, maxChoosableInteger + 1))

        if sum(choices) < desiredTotal:
            return False

        if choices[-1] >= desiredTotal:
            return True

        return can_win(choices, desiredTotal)
