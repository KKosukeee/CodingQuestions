"""
Solution for 203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/
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
            x: integer value for a node
        """
        self.val = x
        self.next = None

class Solution(object):
    """
    Runtime: 76 ms, faster than 23.77% of Python online submissions for Remove Linked List
        Elements.
    Memory Usage: 22.3 MB, less than 5.17% of Python online submissions for Remove Linked List
        Elements.
    """
    def removeElements(self, head, val):
        """
        Remove all elements from a linked list of integers that have value val.

        Example:

        Input:  1->2->6->3->4->5->6, val = 6
        Output: 1->2->3->4->5
        Args:
            head: Node object indicating the head node for a linked-list
            val: integer value to remove from the linked-list

        Returns:
            ListNode: head node for the linked-list where teh val is removed
        """
        # create dummy node
        dummy = ListNode(0)

        # assign head as dummy'next
        new = dummy

        # traverse the node
        while head:
            if head.val != val:
                new.next = ListNode(head.val)
                new = new.next
            head = head.next

        return dummy.next
