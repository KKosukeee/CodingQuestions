"""
Solution for 814. Binary Tree Pruning
"""

# Definition for a binary tree node.
class TreeNode:
    """
    TreeNode object for a BT
    """
    def __init__(self, x):
        """
        Initialization method
        Args:
            x: int value
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 36 ms, faster than 72.44% of Python3 online submissions for Binary Tree Pruning.
    Memory Usage: 13.2 MB, less than 37.56% of Python3 online submissions for Binary Tree Pruning.
    """
    def pruneTree(self, root):
        """
        We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

        Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

        (Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

        Example 1:
        Input: [1,null,0,0,1]
        Output: [1,null,0,null,1]

        Explanation:
        Only the red nodes satisfy the property "every subtree not containing a 1".
        The diagram on the right represents the answer.


        Example 2:
        Input: [1,0,1,0,0,0,1]
        Output: [1,null,1,null,1]



        Example 3:
        Input: [1,1,0,1,1,0,1,0]
        Output: [1,1,0,1,1,null,1]




        Args:
            root: TreeNode object for pruning the BT

        Returns:
            TreeNode: where the all subtrees with non 1 is pruned
        """
        # Recursion comes here
        self.prune(root)
        return root

    def prune(self, node):
        """
        Helper recursive method
        Args:
            node: TreeNode

        Returns:
            bool: whether the node should be pruned or not
        """
        if not node:
            return False

        if self.prune(node.left):
            node.left = None

        if self.prune(node.right):
            node.right = None

        if self.is_leaf(node) and node.val == 0:
            return True

        return self.is_leaf(node) and node.val == 0

    def is_leaf(self, node):
        """
        Helper method
        Args:
            node: TreeNode object

        Returns:
            bool: True if the node is a leaf, False otherwise
        """
        return not node.left and not node.right
