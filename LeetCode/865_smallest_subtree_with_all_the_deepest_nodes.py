"""
Solution for 865. Smallest Subtree with all the Deepest Nodes
https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
"""

# Definition for a binary tree node.
class TreeNode:
    """
    Node object for a BT
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
    Runtime: 40 ms, faster than 88.27% of Python3 online submissions for Smallest Subtree with all
        the Deepest Nodes.
    Memory Usage: 13.1 MB, less than 20.00% of Python3 online submissions for Smallest Subtree with
        all the Deepest Nodes.
    """
    def subtreeWithAllDeepest(self, root):
        """
        Given a binary tree rooted at root, the depth of each node is the shortest distance to the
        root.

        A node is deepest if it has the largest depth possible among any node in the entire tree.

        The subtree of a node is that node, plus the set of all descendants of that node.

        Return the node with the largest depth such that it contains all the deepest nodes in its
        subtree.



        Example 1:

        Input: [3,5,1,6,2,0,8,null,null,7,4]
        Output: [2,7,4]
        Explanation:



        We return the node with value 2, colored in yellow in the diagram.
        The nodes colored in blue are the deepest nodes of the tree.
        The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
        The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
        Both the input and output have TreeNode type.
        Args:
            root: TreeNode object representing a root node for a BT

        Returns:
            TreeNode:
        """
        return_node, _ = self.recursive_call(root, 0)
        return return_node

    def recursive_call(self, root, level):
        """
        Recursive function
        Args:
            root: TreeNode representing a root node of a sub-tree
            level: integer representing a level for current root node

        Returns:
            tuple<TreeNode, int>: TreeNode and int
        """
        if not root:
            return None, level

        left_node, left_level = self.recursive_call(root.left, level + 1)
        right_node, right_level = self.recursive_call(root.right, level + 1)

        if left_level == right_level:
            return root, left_level
        elif left_level > right_level:
            return left_node, left_level
        else:
            return right_node, right_level
