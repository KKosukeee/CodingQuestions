"""
Solution for 116. Populating Next Right Pointers in Each Node
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""

# Definition for a Node.
class Node:
    """
    Node object for a BT
    """
    def __init__(self, val, left, right, next):
        """
        Initialization method
        Args:
            val: int
            left: Node
            right: Node
            next: Node
        """
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    """
    Runtime: 56 ms, faster than 77.42% of Python3 online submissions for Populating Next Right
        Pointers in Each Node.
    Memory Usage: 15.2 MB, less than 86.27% of Python3 online submissions for Populating Next Right
        Pointers in Each Node.
    """
    def connect(self, root):
        """
        You are given a perfect binary tree where all leaves are on the same level, and every
        parent has two children. The binary tree has the following definition:

        struct Node {
          int val;
          Node *left;
          Node *right;
          Node *next;
        }
        Populate each next pointer to point to its next right node. If there is no next right
        node, the next pointer should be set to NULL.

        Initially, all next pointers are set to NULL.
        Args:
            root: Node object representing the root node of the input BT

        Returns:
            Node: root node of the BT where the next pointer is assined properly
        """

        # Initialize starting node
        starting_node = root

        # Loop until starting node is None
        while starting_node and starting_node.left:
            curr_node = starting_node

            # Loop until current node is None
            while curr_node:

                # Update for the left child
                curr_node.left.next = curr_node.right

                # Update for the right child
                if curr_node.next:
                    curr_node.right.next = curr_node.next.left
                else:
                    curr_node.right.next = None

                curr_node = curr_node.next

            # Update for the starting node ONLY ONCE
            starting_node = starting_node.left

        # Return the root
        return root
