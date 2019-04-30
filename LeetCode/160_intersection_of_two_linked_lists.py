"""
Solution for 160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/
"""

# Definition for singly-linked list.
class ListNode(object):
    """
    Node object for linked-list
    """
    def __init__(self, x):
        """
        Initialization method
        Args:
            x: integer value for a node
        """
        self.val = x
        self.next = None

class Solution(object):
    """
    Runtime: 212 ms, faster than 53.53% of Python online submissions for Intersection of Two
        Linked Lists.
    Memory Usage: 41.7 MB, less than 5.17% of Python online submissions for Intersection of Two
        Linked Lists.
    """
    def getIntersectionNode(self, headA, headB):
        """
        Write a program to find the node at which the intersection of two singly linked lists
        begins.

        For example, the following two linked lists:


        begin to intersect at node c1.



        Example 1:


        Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
        Output: Reference of the node with value = 8
        Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the
        two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it
        reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3
        nodes before the intersected node in B.


        Example 2:


        Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
        Output: Reference of the node with value = 2
        Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the
        two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it
        reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node
        before the intersected node in B.


        Example 3:


        Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
        Output: null
        Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads
        as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and
        skipB can be arbitrary values.
        Explanation: The two lists do not intersect, so return null.
        Args:
            headA: ListNode object as a head node for a linked-list
            headB: ListNode object as a head node for the other linked-list

        Returns:
            ListNode: ListNode object if there exists an intersection, None otherwise
        """
        # count for both lists
        count_a, count_b = 0, 0

        # current nodes for both lists
        current_a, current_b = headA, headB

        # count the length with loop
        while current_a or current_b:
            if current_a:
                count_a += 1
                current_a = current_a.next

            if current_b:
                count_b += 1
                current_b = current_b.next

        # if one of them is longer, then make it to the same length
        current_a, current_b = headA, headB
        while count_a != count_b:
            if count_a > count_b:
                current_a = current_a.next
                count_a -= 1
            else:
                current_b = current_b.next
                count_b -= 1

        # if the length are the same, then start loop
        while (current_a and current_b) and current_a != current_b:
            current_a = current_a.next
            current_b = current_b.next

        # return None
        return current_a
