"""
Solution for 230. Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""

# Definition for a binary tree node.
class TreeNode:
    """
    Node object for a BST
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
    Runtime: 56 ms, faster than 95.51% of Python3 online submissions for Kth Smallest Element in
        a BST.
    Memory Usage: 17.2 MB, less than 5.88% of Python3 online submissions for Kth Smallest Element
        in a BST.
    """
    def recursive_approach(self, root, k):
        """
        Naive approach
        Args:
            root: Node object which is a root node for given BST
            k: integer to indicate kth smallest element

        Returns:
            Node: kth smallest Node in the BST
        """
        def sort_array(root):
            # base cases
            if not root:
                return []
            elif not root.left and not root.right:
                return [root.val]
            # recursive cases
            else:
                merged = sort_array(root.left) + [root.val]
                merged = merged + sort_array(root.right)
                return merged

        sorted_array = sort_array(root)
        return sorted_array[k - 1]

    def iterative_approach(self, root, k):
        """
        Optimal approach
        Args:
            root: Node object which is a root node for given BST
            k: integer to indicate kth smallest element

        Returns:
            Node: kth smallest Node in the BST
        """
        count = 0
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            curr = stack.pop()
            k -= 1
            if not k:
                return curr.val
            root = curr.right

    def kthSmallest(self, root, k):
        """
        Given a binary search tree, write a function kthSmallest to find the kth smallest element
        in it.

        Note:
        You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

        Example 1:

        Input: root = [3,1,4,null,2], k = 1
           3
          / \
         1   4
          \
           2
        Output: 1
        Example 2:

        Input: root = [5,3,6,2,4,null,null,1], k = 3
               5
              / \
             3   6
            / \
           2   4
          /
         1
        Output: 3
        Args:
            root: Node object which is a root node for given BST
            k: integer to indicate kth smallest element

        Returns:
            Node: kth smallest Node in the BST
        """
        return self.iterative_approach(root, k)
