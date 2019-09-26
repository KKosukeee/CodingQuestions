"""
Solution for 536. Construct Binary Tree from String
https://leetcode.com/problems/construct-binary-tree-from-string/
"""


# Definition for a binary tree node.
class TreeNode:
    """
    TreeNode object
    """
    def __init__(self, x):
        """
        Initialization method

        Args:
            x(int):
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 120 ms, faster than 48.70% of Python3 online submissions for Construct Binary Tree from String.
    Memory Usage: 14.5 MB, less than 33.33% of Python3 online submissions for Construct Binary Tree from String.
    """
    def stack_solution(self, s: str) -> TreeNode:
        """
        A stack solution that runs in O(N) in time and space

        Args:
            s(str):

        Returns:
            TreeNode:

        """
        if not s:
            return None
        if s.isdigit():
            return TreeNode(int(s))
        stack, i = [], 0
        while i < len(s):
            if s[i] == '-' or s[i].isdigit():
                num = ''
                while i < len(s) and (s[i].isdigit() or s[i] == '-'):
                    num += s[i]
                    i += 1
                stack.append(TreeNode(int(num)))
                continue
            elif s[i] == ')':
                node = stack.pop()
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            i += 1
        return stack.pop()

    def recursive_solution(self, s: str) -> TreeNode:
        """
        Similar to the stack solution, but it does it so recursive mannter
        It runs in O(N) in time and space

        Args:
            s(s):

        Returns:
            TreeNode:

        """
        start = s.find('(')
        if start < 0:
            return None if not s else TreeNode(int(s))
        balance = 0
        end = start
        for char in s[start:]:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance == 0:
                break
            end += 1
        root = TreeNode(int(s[:start]))
        root.left = self.recursive_solution(s[start + 1:end])
        root.right = self.recursive_solution(s[end + 2:-1])
        return root

    """
      *     *
    4(2(3)(1)) (6(5))
    """

    def str2tree(self, s: str) -> TreeNode:
        """
        You need to construct a binary tree from a string consisting of parenthesis and integers.

        The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

        You always start to construct the left child node of the parent first if it exists.

        Example:
        Input: "4(2(3)(1))(6(5))"
        Output: return the tree root node representing the following tree:

               4
             /   \
            2     6
           / \   /
          3   1 5
        Note:
        There will only be '(', ')', '-' and '0' ~ '9' in the input string.
        An empty tree is represented by "" instead of "()".

        Args:
            s(str):

        Returns:
            TreeNode:

        """
        return self.stack_solution(s)

    """
    Stack solution: T->O(N), S->O(N)
    1. Loop through the string
        1.1 Keep count of open paren as a level pointer
        1.2 If the char is num, append it with the level pointer after converting to a TreeNode
        1.3 If the char is close paren, get the element from the stack with the pointer, then assign it as a child node of one level above after the pointer decremented
    2. Return the popped element

    Recursive stack solution
    Base case:
    1. If the input string is empty
    2. If the input string is digit

    Recursive case:
    1. Find the start and end parenthese
    2. Call recursive function with sliced string


    [[4],[2,6],[3,1,5]]
    [[4],[2],[3]]
    [4]
                   *
    4(2(3)(1))(6(5))
    """