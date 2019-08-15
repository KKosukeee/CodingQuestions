"""
Solution for 876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/
"""
# Definition for singly-linked list.
class ListNode:
    """
    ListNode object
    """
    def __init__(self, x):
        """
        Initialization method
        Args:
            x(int): int value
        """
        self.val = x
        self.next = None


class Solution:
    """
    Runtime: 32 ms, faster than 90.00% of Python3 online submissions for Middle of the Linked List.
    Memory Usage: 13.8 MB, less than 7.14% of Python3 online submissions for Middle of the Linked List.
    """
    def middleNode(self, head):
        """
        Given a non-empty, singly linked list with head node head, return a middle node of linked list.

        If there are two middle nodes, return the second middle node.



        Example 1:

        Input: [1,2,3,4,5]
        Output: Node 3 from this list (Serialization: [3,4,5])
        The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
        Note that we returned a ListNode object ans, such that:
        ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
        Example 2:

        Input: [1,2,3,4,5,6]
        Output: Node 4 from this list (Serialization: [4,5,6])
        Since the list has two middle nodes with values 3 and 4, we return the second one.


        Note:

        The number of nodes in the given list will be between 1 and 100.
        Args:
            head(ListNode):

        Returns:
            ListNode:
        """
        if not head.next:
            return head
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
