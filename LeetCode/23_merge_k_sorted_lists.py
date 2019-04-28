"""
Solution for 23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/
"""

# Definition for singly-linked list.
class ListNode:
    """
    Node object for linked-lists
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
    Runtime: 6900 ms, faster than 6.28% of Python3 online submissions for Merge k Sorted Lists.
    Memory Usage: 17.2 MB, less than 15.94% of Python3 online submissions for Merge k Sorted Lists.
    """
    def mergeKLists(self, lists):
        """
        Merge k sorted linked lists and return it as one sorted list. Analyze and describe its
        complexity.

        Example:

        Input:
        [
          1->4->5,
          1->3->4,
          2->6
        ]
        Output: 1->1->2->3->4->4->5->6
        Args:
            lists: list of linked-lists to merge from

        Returns:
            ListNode: head node for a merged linked-list
        """
        pointers = [lists[i] for i in range(len(lists))]
        dummy = ListNode(0)
        current = dummy

        while self.is_valid(pointers):
            current.next = self.get_min(pointers)
            current = current.next

        return dummy.next

    def is_valid(self, pointers):
        """
        Check if the linked-list is valid or not
        Args:
            pointers: ListNode object

        Returns:
            bool: True if it's valid False otherwise
        """
        for pt in pointers:
            if pt:
                return True

        return False

    def get_min(self, pointers):
        """
        Get minimum node given a linked-list
        Args:
            pointers: ListNode object

        Returns:
            ListNode: object from the pointers linked-list
        """
        min_value = float('inf')
        min_index = 0
        min_node = None

        for i, pt in enumerate(pointers):
            if pt and pt.val < min_value:
                min_index = i
                min_value = pt.val
                min_node = ListNode(pt.val)

        pointers[min_index] = pointers[min_index].next
        return min_node
