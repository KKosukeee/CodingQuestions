"""
Solution for 83. Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""

# Definition for singly-linked list.
class ListNode:
    """
    Node for a linked-list
    """
    def __init__(self, x):
        """
        Initialization method
        Args:
            x: integer value for a node
        """
        self.val = x
        self.next = None

class Solution:
    """
    Runtime: 64 ms, faster than 15.06% of Python3 online submissions for Remove Duplicates from
        Sorted List.
    Memory Usage: 13.2 MB, less than 5.26% of Python3 online submissions for Remove Duplicates from
        Sorted List.
    """
    def deleteDuplicates(self, head):
        """
        Given a sorted linked list, delete all duplicates such that each element appear only once.

        Example 1:

        Input: 1->1->2
        Output: 1->2
        Example 2:

        Input: 1->1->2->3->3
        Output: 1->2->3
        Args:
            head: head node for a linked-list to remove duplicates from

        Returns:
            ListNode: head node for newly created linked-list where the duplicates are removed
        """
        # create dummy node
        dummy = ListNode(0)
        dummy.next = head
        current = dummy.next

        # loop while current is valid
        while current:

            # create a variable called skip
            skip = current.next

            # loop while skip.val == current.val
            while skip and skip.val == current.val:
                skip = skip.next

            # update current.next to be skip
            current.next = skip
            current = skip

        return dummy.next
