"""
Solution for 1171. Remove Zero Sum Consecutive Nodes from Linked List
https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
"""
# Definition for singly-linked list.
class ListNode:
    """
    ListNode object
    """
    def __init__(self, x):
        """
        Initialization
        Args:
            x(int):
        """
        self.val = x
        self.next = None

class Solution:
    """
    Runtime: 52 ms, faster than 83.33% of Python3 online submissions for Remove Zero Sum Consecutive Nodes from Linked List.
    Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Remove Zero Sum Consecutive Nodes from Linked List.
    """
    def removeZeroSumSublists(self, head):
        """
        Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

        After doing so, return the head of the final linked list.  You may return any such answer.



        (Note that in the examples below, all sequences are serializations of ListNode objects.)

        Example 1:

        Input: head = [1,2,-3,3,1]
        Output: [3,1]
        Note: The answer [1,2,1] would also be accepted.
        Example 2:

        Input: head = [1,2,3,-3,4]
        Output: [1,2,4]
        Example 3:

        Input: head = [1,2,3,-3,-2]
        Output: [1]


        Constraints:

        The given linked list will contain between 1 and 1000 nodes.
        Each node in the linked list has -1000 <= node.val <= 1000.
        Args:
            head(ListNode):

        Returns:
            ListNode:
        """
        cum_sum = 0
        dummy = ListNode(-1)
        dummy.next = head
        hash_map = {0: dummy}
        while head:
            cum_sum += head.val
            if cum_sum in hash_map:
                hash_map[cum_sum].next = head.next
                head = hash_map[cum_sum].next
            else:
                hash_map[cum_sum] = head
                head = head.next
        return dummy.next
