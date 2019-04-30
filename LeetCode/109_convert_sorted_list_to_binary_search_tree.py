"""
Solution for 109. Convert Sorted List to Binary Search Tree
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
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
            x: integer value for a node
        """
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    """
    Node object for BST
    """
    def __init__(self, x):
        """
        Initialization method
        Args:
            x: integer value for a node
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 136 ms, faster than 48.66% of Python3 online submissions for Convert Sorted List to
        Binary Search Tree.
    Memory Usage: 17 MB, less than 59.29% of Python3 online submissions for Convert Sorted List to
        Binary Search Tree.
    """
    def findMiddle(self, head):
        """
        Given a singly linked list where elements are sorted in ascending order, convert it to a
        height balanced BST.

        For this problem, a height-balanced binary tree is defined as a binary tree in which the
        depth of the two subtrees of every node never differ by more than 1.

        Example:

        Given the sorted linked list: [-10,-3,0,5,9],

        One possible answer is: [0,-3,9,-10,null,5], which represents the following height
        balanced BST:

              0
             / \
           -3   9
           /   /
         -10  5
        Args:
            head: ListNode object for linked-list to convert into BST

        Returns:
            TreeNode: root node for converted BST
        """

        # The pointer used to disconnect the left half from the mid node.
        prevPtr = None
        slowPtr = head
        fastPtr = head

        # Iterate until fastPr doesn't reach the end of the linked list.
        while fastPtr and fastPtr.next:
            prevPtr = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        # Handling the case when slowPtr was equal to head.
        if prevPtr:
            prevPtr.next = None

        return slowPtr


    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        # If the head doesn't exist, then the linked list is empty
        if not head:
            return None

        # Find the middle element for the list.
        mid = self.findMiddle(head)

        # The mid becomes the root of the BST.
        node = TreeNode(mid.val)

        # Base case when there is just one element in the linked list
        if head == mid:
            return node

        # Recursively form balanced BSTs using the left and right halves of the original list.
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node
