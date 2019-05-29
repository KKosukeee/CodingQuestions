"""
Solution for 86. Partition List
https://leetcode.com/problems/partition-list/
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
            x: int value for a node
        """
        self.val = x
        self.next = None

class Solution:
    """
    Runtime: 40 ms, faster than 89.42% of Python3 online submissions for Partition List.
    Memory Usage: 13.1 MB, less than 77.86% of Python3 online submissions for Partition List.
    """
    def partition(self, head, x):
        """
        Given a linked list and a value x, partition it such that all nodes less than x come before
        nodes greater than or equal to x.

        You should preserve the original relative order of the nodes in each of the two partitions.

        Example:

        Input: head = 1->4->3->2->5->2, x = 3
        Output: 1->2->2->4->3->5
        Args:
            head: ListNode object as a head of the linked-list
            x: int value to partition with

        Returns:
            ListNode: as the new head of the linked-list
        """
        # Initialize less and more array
        less = less_head = ListNode(0)
        more = more_head = ListNode(0)

        # Traverse the linked-list
        current = head
        while current:

            # If the current node has value < x, then append to less
            if current.val < x:
                less.next = current
                less = less.next

            # Otherwise append the current node to more array
            else:
                more.next = current
                more = more.next

            current = current.next

        # Now connect less and more list
        more.next = None
        less.next = more_head.next
        return less_head.next
