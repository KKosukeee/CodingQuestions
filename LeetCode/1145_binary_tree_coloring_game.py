"""
Solution for 1145. Binary Tree Coloring Game
https://leetcode.com/problems/binary-tree-coloring-game/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    """
    Runtime: 36 ms, faster than 100.00% of Python3 online submissions for Binary Tree Coloring Game.
    Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Binary Tree Coloring Game.
    """
    def btreeGameWinningMove(self, root, n, x):
        """
        Two players play a turn based game on a binary tree.  We are given the root of this binary tree, and the number of nodes n in the tree.  n is odd, and each node has a distinct value from 1 to n.

        Initially, the first player names a value x with 1 <= x <= n, and the second player names a value y with 1 <= y <= n and y != x.  The first player colors the node with value x red, and the second player colors the node with value y blue.

        Then, the players take turns starting with the first player.  In each turn, that player chooses a node of their color (red if player 1, blue if player 2) and colors an uncolored neighbor of the chosen node (either the left child, right child, or parent of the chosen node.)

        If (and only if) a player cannot choose such a node in this way, they must pass their turn.  If both players pass their turn, the game ends, and the winner is the player that colored more nodes.

        You are the second player.  If it is possible to choose such a y to ensure you win the game, return true.  If it is not possible, return false.



        Example 1:


        Input: root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
        Output: true
        Explanation: The second player can choose the node with value 2.


        Constraints:

        root is the root of a binary tree with n nodes and distinct node values from 1 to n.
        n is odd.
        1 <= x <= n <= 100
        Args:
            root: TreeNode as the root
            n: int value
            x: int value

        Returns:
            bool:
        """
        def count_nodes(node):
            """
            Counts # of nodes
            Args:
                node: TreeNode

            Returns:
                int: # of nodes
            """
            if not node:
                return 0
            return count_nodes(node.left) + count_nodes(node.right) + 1

        queue = deque([root])
        while queue:
            temp_queue = deque([])
            while queue:
                node = queue.popleft()
                if node.val == x:
                    left_count = count_nodes(node.left)
                    right_count = count_nodes(node.right)
                    parent_count = n - left_count - right_count - 1

                    if left_count > right_count + parent_count + 1:
                        return True
                    elif right_count > left_count + parent_count + 1:
                        return True
                    elif parent_count > left_count + right_count + 1:
                        return True
                    else:
                        return False

                if node.left:
                    temp_queue.append(node.left)
                if node.right:
                    temp_queue.append(node.right)
            queue = temp_queue
