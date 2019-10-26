"""
Solution for 143. Reorder List
https://leetcode.com/problems/reorder-list/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Runtime: 100 ms, faster than 56.30% of Python3 online submissions for Reorder List.
    Memory Usage: 22.5 MB, less than 7.69% of Python3 online submissions for Reorder List.
    """
    def first_solution(self, head: ListNode) -> None:
        """
        The first solution that runs in O(N) in time and O(1) in space

        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = head
        while curr.next != slow:
            curr = curr.next

        curr.next = None
        curr, prev = slow, None
        while curr:
            tmp = curr.next
            curr.next = prev
            curr, prev = tmp, curr

        first, middle = head, prev
        count = 0
        while first or middle:
            if count % 2 == 0:
                # Use first
                tmp = first.next
                first.next = middle
                first = tmp
            else:
                # User middle
                tmp = middle.next
                middle.next = first
                if first:
                    middle = tmp
                else:
                    first = middle
                    middle = tmp
            count += 1

    def second_solution(self, head: ListNode) -> None:
        """
        The second solution that runs in O(N) in time and O(1) in space

        Args:
            head:

        Returns:

        """
        if not head or not head.next:
            return

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow.next
        slow.next = None
        curr, prev = middle, None
        while curr:
            tmp = curr.next
            curr.next = prev
            curr, prev = tmp, curr

        first, second = head, prev
        while first and second:
            first_tmp = first.next
            second_tmp = second.next
            first.next = second
            second.next = first_tmp
            first, second = first_tmp, second_tmp

    def reorderList(self, head: ListNode) -> None:
        """
        Given a singly linked list L: L0→L1→…→Ln-1→Ln,
        reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

        You may not modify the values in the list's nodes, only nodes itself may be changed.

        Example 1:

        Given 1->2->3->4, reorder it to 1->4->2->3.
        Example 2:

        Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

        Args:
            head:

        Returns:

        """
        self.second_solution(head)

    """
    1, 2  |  4, 3
    1, 4, 
    List manipulation
    T: O(N), S: O(1)
    1. Find the middle of the list
    2. Reverse the last half list
    3. Traverse the list with two pointers
    4. Assign the second node as the next of the first
    """
