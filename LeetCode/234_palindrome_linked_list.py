"""
Solution for 234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/
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
            x: integer value for a node
        """
        self.val = x
        self.next = None

class Solution:
    """
    Runtime: 84 ms, faster than 47.65% of Python3 online submissions for Palindrome Linked List.
    Memory Usage: 27.7 MB, less than 5.02% of Python3 online submissions for Palindrome Linked List.
    """
    def isPalindrome(self, head):
        """
        Given a singly linked list, determine if it is a palindrome.

        Example 1:

        Input: 1->2
        Output: false
        Example 2:

        Input: 1->2->2->1
        Output: true
        Args:
            head: ListNode object for a linked-list

        Returns:
            bool: representing if the list is a palindrome or not
        """
        if not head or not head.next:
            return True

        slow_ptr = head
        fast_ptr = head
        reversed_head = None
        prev_node = None

        # Loop the half of the list
        while slow_ptr and fast_ptr and fast_ptr.next:
            # Create reversed list
            reversed_head = ListNode(slow_ptr.val)

            reversed_head.next = prev_node
            prev_node = reversed_head

            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        # Then the length must be odd number
        if fast_ptr:
            slow_ptr = slow_ptr.next

        # Traverse the list and compare the values
        while slow_ptr and reversed_head:

            # If the values differ, then return False
            if slow_ptr.val != reversed_head.val:
                return False

            slow_ptr = slow_ptr.next
            reversed_head = reversed_head.next

        # Otherwise return True
        return True
