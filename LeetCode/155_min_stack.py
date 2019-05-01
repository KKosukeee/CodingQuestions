"""
Solution for 155. Min Stack
https://leetcode.com/problems/min-stack/
"""
class MinStack:
    """
    Runtime: 60 ms, faster than 82.85% of Python3 online submissions for Min Stack.
    Memory Usage: 16.7 MB, less than 5.18% of Python3 online submissions for Min Stack.
    """

    def __init__(self):
        """
        Initialization method
        """
        self.stack = []
        self.min = None

    def push(self, x):
        """
        push operation for a stack
        Args:
            x: integer value for a stack

        Returns:

        """
        if self.min is None:
            self.min = x
        else:
            self.min = min(self.min, x)

        self.stack.append(x)

    def pop(self):
        """
        pops an element from a stack
        Returns:

        """
        _ = self.stack.pop()

        if self.stack:
            self.min = min(self.stack)
        else:
            self.min = None

    def top(self):
        """
        returns an element which will be popped by next call
        Returns:

        """
        return self.stack[-1]

    def getMin(self):
        """
        will get minimum number from the stack
        Returns:
            int: minimum number in the stack
        """
        return self.min
