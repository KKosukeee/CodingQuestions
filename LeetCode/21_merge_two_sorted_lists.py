"""
Solution for 21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
"""

# Definition for singly-linked list.
class ListNode:
    """
    Node object for linked-list
    """
    def __init__(self, x):
        """
        Initialization method
        Args:
            x: integer value
        """
        self.val = x
        self.next = None

class Solution:
    """
    Runtime: 60 ms, faster than 13.58% of Python3 online submissions for Merge Two Sorted Lists.
    Memory Usage: 13.1 MB, less than 5.06% of Python3 online submissions for Merge Two Sorted Lists.
    """
    # approach1
    def naive_approach(self, l1, l2):
        """
        naive solution
        Args:
            l1: head node for the first linked-list to merge with
            l2: head node for the second linked-list to merge with

        Returns:
            ListNode: head node for a merged linked-list
        """
        current = ListNode(0)
        head = current

        while l1 or l2:
            if l1 and l2:
                if l1.val > l2.val:
                    current.next = ListNode(l2.val)
                    l2 = l2.next
                else:
                    current.next = ListNode(l1.val)
                    l1 = l1.next
            elif l1:
                current.next = ListNode(l1.val)
                l1 = l1.next
            elif l2:
                current.next = ListNode(l2.val)
                l2 = l2.next

            current = current.next

        return head.next

    def optimal_approach(self, l1, l2):
        """
        Optimal approach
        Args:
            l1: head node for the first linked-list to merge with
            l2: head node for the second linked-list to merge with

        Returns:
            ListNode: head node for a merged linked-list
        """
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        else:
            if l1.val > l2.val:
                merged = ListNode(l2.val)
                merged.next = self.mergeTwoLists(l1, l2.next)
            else:
                merged = ListNode(l1.val)
                merged.next = self.mergeTwoLists(l1.next, l2)

            return merged

    def mergeTwoLists(self, l1, l2):
        """
        Merge two sorted linked lists and return it as a new list. The new list should be made by
        splicing together the nodes of the first two lists.

        Example:

        Input: 1->2->4, 1->3->4
        Output: 1->1->2->3->4->4
        Args:
            l1: head node for the first linked-list to merge with
            l2: head node for the second linked-list to merge with

        Returns:
            ListNode: head node for a merged linked-list
        """
        return self.optimal_approach(l1, l2)
