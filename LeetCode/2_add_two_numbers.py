"""
Solution for 2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
"""
# Definition for singly-linked list.
class ListNode:
    """
    ListNode object for LinkedList
    """
    def __init__(self, x):
        """
        Initialization method
        Args:
            x: a value for the particular node
        """
        self.val = x
        self.next = None

class Solution:
    """
    Runtime: 80 ms, faster than 94.73% of Python3 online submissions for Add Two Numbers.
    Memory Usage: 13.2 MB, less than 5.21% of Python3 online submissions for Add Two Numbers.
    """
    # Optimal, yet not beautiful solution: O(n)
    def addTwoNumbers(self, l1, l2):
        """
        You are given two non-empty linked lists representing two non-negative integers.
        The digits are stored in reverse order and each of their nodes contain a single digit.
        Add the two numbers and return it as a linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.

        Example:

        Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 0 -> 8
        Explanation: 342 + 465 = 807.
        Args:
            l1: first linked-list containing integers
            l2: second linked-list containing integers

        Returns:
            ListNode: output linked-list where the values are l1 + l2
        """
        carry = 0
        dummy = answer = ListNode(0)

        while l1 or l2:
            val1 = 0 if not l1 else l1.val
            val2 = 0 if not l2 else l2.val
            added = val1 + val2 + carry

            if added >= 10:
                carry = 1
                added %= 10
            else:
                carry = 0

            answer.next = ListNode(added)
            answer = answer.next
            l1 = None if not l1 else l1.next
            l2 = None if not l2 else l2.next

        if carry == 1:
            answer.next = ListNode(1)

        return dummy.next
