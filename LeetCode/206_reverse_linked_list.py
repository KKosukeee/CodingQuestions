"""
Solution for 206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
"""

# Definition for singly-linked list.
class ListNode(object):
    """
    Node object for a linked-list
    """
    def __init__(self, x):
        """
        Initialization method
        Args:
            x: integer for a node
        """
        self.val = x
        self.next = None

class Solution(object):
    """
    Runtime: 40 ms, faster than 12.75% of Python online submissions for Reverse Linked List.
    Memory Usage: 13.6 MB, less than 25.52% of Python online submissions for Reverse Linked List.
    """
    def reverseList(self, head):
        """
        Reverse a singly linked list.

        Example:

        Input: 1->2->3->4->5->NULL
        Output: 5->4->3->2->1->NULL
        Args:
            head: ListNode object which is a head node for a linked-list to reverse

        Returns:
            ListNode: a head node for a reversed linked-list
        """
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head
