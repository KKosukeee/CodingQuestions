"""
Solution for 225. Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/
"""
from collections import deque

class MyStack:
    """
    Runtime: 36 ms, faster than 80.47% of Python3 online submissions for Implement Stack using
        Queues.
    Memory Usage: 13.1 MB, less than 5.45% of Python3 online submissions for Implement Stack using
        Queues.
    """
    def __init__(self):
        """
        Initialization method for a stack
        """
        self.stack = deque()

    def push(self, x):
        """
        push operation for a stack
        Args:
            x: integer value to put into the stack

        Returns:

        """
        self.stack.append(x)

    def pop(self):
        """
        pop operation for a stack
        Returns:
            int: integer value returned by a stack in LIFO manner
        """
        return self.stack.pop()

    def top(self):
        """
        return top element from a stack
        Returns:
            int: the last element in stack data structure
        """
        return self.stack[-1]

    def empty(self):
        """
        determine if the stack is empty or not
        Returns:
            bool: True if stack is empty, otherwise False
        """
        return len(self.stack) == 0
