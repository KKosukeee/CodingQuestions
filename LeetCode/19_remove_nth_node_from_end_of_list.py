"""
Solution for 19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

# Definition for singly-linked list.
class ListNode:
    """
    Node object for a linked-list
    """
    def __init__(self, x):
        """
        Initialization method for a Node
        Args:
            x: value
        """
        self.val = x
        self.next = None

class Solution:
    """
    Runtime: 40 ms, faster than 92.19% of Python3 online submissions for Remove Nth Node From End
        of List.
    Memory Usage: 13.2 MB, less than 5.60% of Python3 online submissions for Remove Nth Node From
        End of List.
    """
    def naive_approach(self, head, n):
        """
        Naive approach
        Args:
            head: head node for a linked-list to remove Nth node
            n: position of the node which you will remove

        Returns:
            ListNode: head node for a linked-list where nth node is removed
        """
        count = 0
        current = head

        while current:
            count += 1
            current = current.next

        target = count - n
        current = head
        index = 0

        if target == 0:
            return head.next
        else:
            while current:
                if index == target - 1:
                    current.next = current.next.next
                    break

                index += 1
                current = current.next

            return head

    def optimal_approach(self, head, n):
        """
        Optimal approach which does the job with one pass
        Args:
            head: head node for a linked-list to remove Nth node
            n: position of the node which you will remove

        Returns:
            ListNode: head node for a linked-list where nth node is removed
        """
        self.index = 1

        def helper(node):
            if not node:
                return None
            else:
                tmp = helper(node.next)

                if self.index == n + 1:
                    node.next = tmp.next
                else:
                    node.next = tmp

                self.index += 1
                return node

        node = helper(head)
        if self.index == n + 1:
            return node.next
        else:
            return node

    def removeNthFromEnd(self, head, n):
        """
        Given a linked list, remove the n-th node from the end of list and return its head.

        Example:

        Given linked list: 1->2->3->4->5, and n = 2.

        After removing the second node from the end, the linked list becomes 1->2->3->5.
        Note:

        Given n will always be valid.

        Args:
            head: head node for a linked-list to remove Nth node
            n: position of the node which you will remove

        Returns:
            ListNode: head node for a linked-list where nth node is removed
        """
        return self.optimal_approach(head, n)
