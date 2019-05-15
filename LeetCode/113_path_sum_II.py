"""
Solution for 113. Path Sum II
https://leetcode.com/problems/path-sum-ii/
"""

# Definition for a binary tree node.
class TreeNode:
    """
    Node object for a BT
    """
    def __init__(self, x):
        """
        Initialization method for a BT
        Args:
            x: int value for a node
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 48 ms, faster than 99.55% of Python3 online submissions for Path Sum II.
    Memory Usage: 18.7 MB, less than 24.44% of Python3 online submissions for Path Sum II.
    """
    def pathSum(self, root, sum):
        """
        Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals
        the given sum.

        Note: A leaf is a node with no children.

        Example:

        Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
        Return:

        [
           [5,4,11,2],
           [5,8,4,5]
        ]
        Args:
            root: TreeNode for a BT to find path sum from
            sum: The values you want to add up

        Returns:
            list<list<int>>: All paths that add up to sum
        """
        # Create result array
        result = []

        # Create dfs function with root, remain and path array as inputs
        def dfs(root, path, remain):
            # Check if root it None
            if not root:
                return
            elif not root.left and not root.right:
                if remain == root.val:
                    result.append(path + [root.val])
            # Otherwise recursive case will be the one
            else:

                # Call recursive function for left child
                dfs(root.left, path + [root.val], remain - root.val)

                # Call recursive function for right child
                dfs(root.right, path + [root.val], remain - root.val)

        # Call and return dfs function
        dfs(root, [], sum)
        return result
