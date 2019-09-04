"""
Solution for 946. Validate Stack Sequences
https://leetcode.com/problems/validate-stack-sequences/
"""
from typing import List
class Solution:
    """
    Runtime: 88 ms, faster than 43.41% of Python3 online submissions for Validate Stack Sequences.
    Memory Usage: 14 MB, less than 20.00% of Python3 online submissions for Validate Stack Sequences.
    """
    def constant_space(self, pushed, popped):
        """
        Constant memory solution which runs in O(M*N) where M = len(pushed), N = len(popped)

        Args:
            pushed(list[int]):
            popped(list[int]):

        Returns:
            bool

        """
        if not pushed or not popped:
            return True
        index = 0
        for i in range(len(popped)):
            temp = pushed.index(popped[i])
            if index and not index - temp <= 1:
                return False
            pushed.pop(temp)
            index = temp
        return True

    def linear_time(self, pushed: List[int], popped: List[int]) -> bool:
        """
        Linear time solution which runs in O(N+M)

        Args:
            pushed(list[int]):
            popped(list[int]):

        Returns:
            bool

        """
        j = 0
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                _ = stack.pop()
                j += 1
        return not stack

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.



        Example 1:

        Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
        Output: true
        Explanation: We might do the following sequence:
        push(1), push(2), push(3), push(4), pop() -> 4,
        push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
        Example 2:

        Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
        Output: false
        Explanation: 1 cannot be popped before 2.


        Note:

        0 <= pushed.length == popped.length <= 1000
        0 <= pushed[i], popped[i] < 1000
        pushed is a permutation of popped.
        pushed and popped have distinct values.

        Args:
            pushed(list[int]):
            popped(list[int]):

        Returns:
            bool:

        """
        return self.linear_time(pushed, popped)

    #      *
    # [4,5,3,2,1]
    #          *
    # [1,2,3,4,5]