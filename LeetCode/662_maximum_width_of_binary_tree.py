"""
Solution for 662. Maximum Width of Binary Tree
https://leetcode.com/problems/maximum-width-of-binary-tree/
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
    Runtime: 40 ms, faster than 99.88% of Python3 online submissions for Maximum Width of Binary
        Tree.
    Memory Usage: 13.7 MB, less than 29.09% of Python3 online submissions for Maximum Width of
        Binary Tree.
    """
    def widthOfBinaryTree(self, root):
        """
        Given a binary tree, write a function to get the maximum width of the given tree. The
        width of a tree is the maximum width among all levels. The binary tree has the same
        structure as a full binary tree, but some nodes are null.

        The width of one level is defined as the length between the end-nodes (the leftmost and
        right most non-null nodes in the level, where the null nodes between the end-nodes are
        also counted into the length calculation.

        Example 1:

        Input:

                   1
                 /   \
                3     2
               / \     \
              5   3     9

        Output: 4
        Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
        Example 2:

        Input:

                  1
                 /
                3
               / \
              5   3

        Output: 2
        Explanation: The maximum width existing in the third level with the length 2 (5,3).
        Example 3:

        Input:

                  1
                 / \
                3   2
               /
              5

        Output: 2
        Explanation: The maximum width existing in the second level with the length 2 (3,2).
        Example 4:

        Input:

                  1
                 / \
                3   2
               /     \
              5       9
             /         \
            6           7
        Output: 8
        Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
        Args:
            root: TreeNode object as a root node for a BT

        Returns:
            int: value for a maximum width
        """
        queue = [(root, 0, 0)]
        cur_depth = left = ans = 0
        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth + 1, pos * 2))
                queue.append((node.right, depth + 1, pos * 2 + 1))
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                ans = max(pos - left + 1, ans)

        return ans
