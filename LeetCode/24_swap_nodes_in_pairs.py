"""
Solution for 24. Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs/
"""

# Definition for singly-linked list.
class ListNode:
    """
    Node object for linked-list object
    """
    def __init__(self, x):
        """
        Initialization method
        Args:
            x: a value for a node
        """
        self.val = x
        self.next = None

class Solution:
    def recursive_approach(self, head):
        """
        Recursive approach
        Args:
            head: ListNode object for the head of a linked-list

        Returns:
            ListNode: head of the swapped linked-list
        """
        if not head:
            return None

        if not head.next:
            return self.helper(head, None)
        else:
            return self.helper(head, head.next)

    def clean_recursive_approach(self, head):
        """
        Clean recursive approach
        Args:
            head: ListNode object for the head of a linked-list

        Returns:
            ListNode: head of the swapped linked-list
        """
        if head and head.next:
            tmp = head.next
            head.next = self.clean_recursive_approach(tmp.next)
            tmp.next = head
            return tmp
        return head

    def helper(self, node1, node2):
        """
        Helper function for recursive_approach function
        Args:
            node1: first node in the linked-list
            node2: second node in the linked-list

        Returns:
            ListNode: head node for a swapped node
        """
        if not node1 and not node2:
            return None
        elif not node1 or not node2:
            return node1
        else:
            dummy = ListNode(0)
            dummy.next = node2

            if node2.next:
                next_node = node2.next
                next_next_node = next_node.next
            else:
                next_node = None
                next_next_node = None

            node2.next = node1
            node1.next = self.helper(next_node, next_next_node)
            return dummy.next

    def swapPairs(self, head):
        """
        Given a linked list, swap every two adjacent nodes and return its head.

        You may not modify the values in the list's nodes, only nodes itself may be changed.

        Example:

        Given 1->2->3->4, you should return the list as 2->1->4->3.
        Args:
            head: ListNode object for the head of a linked-list

        Returns:
            ListNode: head of the swapped linked-list
        """
        return self.clean_recursive_approach(head)
