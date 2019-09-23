"""
Solution for 938. Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/
"""

# Definition for a binary tree node.
class TreeNode:
    """
    TreeNode
    """
    def __init__(self, x):
        """
        Init

        Args:
            x(int):
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 224 ms, faster than 89.80% of Python3 online submissions for Range Sum of BST.
    Memory Usage: 22.1 MB, less than 5.94% of Python3 online submissions for Range Sum of BST.
    """
    def simple_solution(self, root: TreeNode, L: int, R: int) -> int:
        """
        A simple solution that yet runs in optimal linear time in both time and space

        Args:
            root(TreeNode):
            L(int):
            R(int):

        Returns:
            int:

        """
        nums = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)

        dfs(root)
        return sum([num for num in nums if L <= num <= R])

    def better_solution(self, root: TreeNode, L: int, R: int) -> int:
        """
        Slightly optimized solution that runs in linear in time and space

        Args:
            root(TreeNode):
            L(int):
            R(int):

        Returns:
            int:

        """
        result, stack = 0, [root]
        while stack:
            node = stack.pop()
            if L <= node.val <= R:
                result += node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result

    def optimal_solution(self, root: TreeNode, L: int, R: int) -> int:
        """
        An optimal solution that runs in linear in time and space

        Args:
            root(TreeNode):
            L(int):
            R(int):

        Returns:
            int:

        """
        result, stack = 0, [root]
        while stack:
            node = stack.pop()
            if L <= node.val <= R:
                result += node.val
            if L <= node.val and node.left:
                stack.append(node.left)
            if R >= node.val and node.right:
                stack.append(node.right)
        return result

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        """
        Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

        The binary search tree is guaranteed to have unique values.



        Example 1:

        Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
        Output: 32
        Example 2:

        Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
        Output: 23


        Note:

        The number of nodes in the tree is at most 10000.
        The final answer is guaranteed to be less than 2^31.

        Args:
            root(TreeNode):
            L(int):
            R(int):

        Returns:
            int:

        """
        return self.optimal_solution(root, L, R)

    """
    Simple solution: T -> O(n), S -> O(n)
    1. Traversing the BST and create an array in ascending order
    2. Loop through the array and find the value of left first
    3. Continue looping, and find the right value
    4. Sum the range of nodes up and return

    Better solution: T -> O(n), S -> O(n)
    1. Traverse the BST in DFS manner
    2. Find a node with the value of left
    3. Keep incrementing the number, until the node with a value of right is found

    Optiaml solution: T -> O(n), S -> O(n)
    1. Traverse the BST in DFS manner
    2. If the current val is less than left, no need to seek the left part
    3. If the current val falls into the range between L and R, increment the counter
    4. If the current val is larger than the right, stop traversing
    """
