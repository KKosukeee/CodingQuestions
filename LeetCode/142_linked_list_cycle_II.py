"""
Solution for 142. Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/
"""

# Definition for singly-linked list.
class ListNode:
    """
    Node object for a linkedlist
    """
    def __init__(self, x):
        """
        Initialization method for a node
        Args:
            x: int value for a node
        """
        self.val = x
        self.next = None

class Solution:
    """
    Runtime: 40 ms, faster than 96.04% of Python online submissions for Linked List Cycle II.
    Memory Usage: 18 MB, less than 91.44% of Python online submissions for Linked List Cycle II.
    """
    def detectCycle(self, head):
        """
        Given a linked list, return the node where the cycle begins. If there is no cycle, return
        null.

        To represent a cycle in the given linked list, we use an integer pos which represents the
        position (0-indexed) in the linked list where tail connects to. If pos is -1, then there
        is no cycle in the linked list.

        Note: Do not modify the linked list.



        Example 1:

        Input: head = [3,2,0,-4], pos = 1
        Output: tail connects to node index 1
        Explanation: There is a cycle in the linked list, where tail connects to the second node.


        Example 2:

        Input: head = [1,2], pos = 0
        Output: tail connects to node index 0
        Explanation: There is a cycle in the linked list, where tail connects to the first node.


        Example 3:

        Input: head = [1], pos = -1
        Output: no cycle
        Explanation: There is no cycle in the linked list.
        Args:
            head: ListNode as the head of the linked-list to look for a cycle

        Returns:
            ListNode: where the cycle begins
        """
        if not head:
            return None
        if not head.next:
            return head if head.next == head else None

        slow, fast = head, head
        meet_node = None

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                meet_node = slow
                break

        if meet_node:
            slow = head
            while slow and fast:
                if slow == fast:
                    return slow

                slow = slow.next
                fast = fast.next

        return None
