"""
Solution for 141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
"""

# Definition for singly-linked list.
class ListNode(object):
    """
    Node object for linked-lists
    """
    def __init__(self, x):
        """
        Initialization method
        Args:
            x: int value for a node
        """
        self.val = x
        self.next = None

class Solution(object):
    """
    Runtime: 36 ms, faster than 99.79% of Python online submissions for Linked List Cycle.
    Memory Usage: 18.1 MB, less than 5.04% of Python online submissions for Linked List Cycle.
    """
    def naive_approach(self, head):
        """
        Naive approach which runs O(n) in runtime and O(n) in space where the n is the
        length of the list
        Args:
            head: head node for a linked-list to look for a cycle

        Returns:
            bool: representing if the linked-list has a cycle or not
        """
        # create a dict with Node: index
        hash_table = set()

        # loop through the list
        while head:

            # check if node is in the dict
            if head in hash_table:
                # if it is, then return the index
                return True

            else:
                # otherwise, keep adding to the dict
                hash_table.add(head)

            head = head.next

        return False

    def optimal_approach(self, head):
        """
        Optimal approach which runs O(n) in runtime and O(1) in space
        Args:
            head: head node for a linked-list to look for a cycle

        Returns:
            bool: representing if the list has a cycle or not
        """
        if not head or not head.next:
            return False

        slow_pointer = head
        fast_pointer = head.next

        while slow_pointer != fast_pointer:
            if not slow_pointer or not fast_pointer or not fast_pointer.next:
                return False

            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return True

    def hasCycle(self, head):
        """
        Given a linked list, determine if it has a cycle in it.

        To represent a cycle in the given linked list, we use an integer pos which represents
        the position (0-indexed) in the linked list where tail connects to. If pos is -1, then
        there is no cycle in the linked list.



        Example 1:

        Input: head = [3,2,0,-4], pos = 1
        Output: true
        Explanation: There is a cycle in the linked list, where tail connects to the second node.


        Example 2:

        Input: head = [1,2], pos = 0
        Output: true
        Explanation: There is a cycle in the linked list, where tail connects to the first node.


        Example 3:

        Input: head = [1], pos = -1
        Output: false
        Explanation: There is no cycle in the linked list.
        Args:
            head: head node for a linked-list to look for a cycle

        Returns:
            bool: representing if the list has a cycle or not
        """
        return self.optimal_approach(head)
