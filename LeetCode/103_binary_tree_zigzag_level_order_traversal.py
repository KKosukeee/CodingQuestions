"""
Solution for 103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""

# Definition for a binary tree node.
class TreeNode:
    """
    Node for a BST
    """
    def __init__(self, x):
        """
        Initialization method for a node
        Args:
            x: integer value
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 40 ms, faster than 81.74% of Python3 online submissions for Binary Tree Zigzag Level
        Order Traversal.
    Memory Usage: 13.2 MB, less than 5.36% of Python3 online submissions for Binary Tree Zigzag
        Level Order Traversal.
    """
    def zigzagLevelOrder(self, root):
        """
        Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie,
        from left to right, then right to left for the next level and alternate between).

        For example:
        Given binary tree [3,9,20,null,null,15,7],
            3
           / \
          9  20
            /  \
           15   7
        return its zigzag level order traversal as:
        [
          [3],
          [20,9],
          [15,7]
        ]
        Args:
            root: TreeNode as a root node for given BST

        Returns:
            list<list<int>>: containing the values as zigzag traversal goes
        """
        if not root:
            return []

        # create direction variable
        going_right = False

        # initialize a level stack
        level_stack = [root]

        # initialize a result array
        result = []

        # loop while level stack is not empry
        while level_stack:

            # create tmp array
            tmp = []

            res_tmp = []

            # do the BFS by looping through each element
            while level_stack:

                # pop an element from the stack
                node = level_stack.pop()

                res_tmp.append(node.val)

                # if direction is 1 or going right, take left node first
                if going_right == 1:
                    if node.left:
                        tmp.append(node.left)

                    if node.right:
                        tmp.append(node.right)

                # otherwise take right node first, append to the temp list
                else:
                    if node.right:
                        tmp.append(node.right)

                    if node.left:
                        tmp.append(node.left)

            # append temp list to the result list
            result.append(res_tmp[::-1])

            # update level stack
            level_stack = tmp

            # change the direction
            going_right = not going_right

        return result
