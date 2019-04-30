"""
Solution for 82. Remove Duplicates from Sorted List II
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
"""

# Definition for singly-linked list.
class ListNode:
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

class Solution:
    """
    Runtime: 64 ms, faster than 15.58% of Python3 online submissions for Remove Duplicates from
        Sorted List II.
    Memory Usage: 13.3 MB, less than 5.75% of Python3 online submissions for Remove Duplicates from
        Sorted List II.
    """
    def deleteDuplicates(self, head):
        """
        Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only
        distinct numbers from the original list.

        Example 1:

        Input: 1->2->3->3->4->4->5
        Output: 1->2->5
        Example 2:

        Input: 1->1->1->2->3
        Output: 2->3
        Args:
            head: head node to remove duplicates from

        Returns:
            ListNode: head node for a newly created linked-list
        """
        dummy = ListNode(0)
        new_list = dummy

        while head:
            skip = head.next

            while skip and skip.val == head.val:
                skip = skip.next

            if head.next == skip:
                new_list.next = ListNode(head.val)
                new_list = new_list.next

            head = skip
        return dummy.next
