"""
Solution for 573. Squirrel Simulation
https://leetcode.com/problems/squirrel-simulation/
"""
from typing import List

class Solution:
    """
    Runtime: 160 ms, faster than 96.30% of Python3 online submissions for Squirrel Simulation.
    Memory Usage: 14.8 MB, less than 50.00% of Python3 online submissions for Squirrel Simulation.
    """
    def two_pass(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        """
        Two pass solutio that runs in O(n) in time and O(1) in space

        Args:
            height:
            width:
            tree:
            squirrel:
            nuts:

        Returns:

        """
        dist = lambda p, q: abs(p[0] - q[0]) + abs(p[1] - q[1])
        total = sum(dist(nut, tree) for nut in nuts) * 2
        return min(total - dist(nut, tree) + dist(nut, squirrel) for nut in nuts)

    def one_pass(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        """
        One-pass solution that runs in O(n) in time and O(1) in space

        Args:
            height:
            width:
            tree:
            squirrel:
            nuts:

        Returns:

        """
        dist = lambda p, q: abs(p[0] - q[0]) + abs(p[1] - q[1])
        total, bonus = 0, float('-inf')
        for nut in nuts:
            total += dist(nut, tree) * 2
            bonus = max(bonus, dist(nut, tree) - dist(nut, squirrel))
        return total - bonus

    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        """
        There's a tree, a squirrel, and several nuts. Positions are represented by the cells in a 2D grid. Your goal is to find the minimal distance for the squirrel to collect all the nuts and put them under the tree one by one. The squirrel can only take at most one nut at one time and can move in four directions - up, down, left and right, to the adjacent cell. The distance is represented by the number of moves.
        Example 1:

        Input:
        Height : 5
        Width : 7
        Tree position : [2,2]
        Squirrel : [4,4]
        Nuts : [[3,0], [2,5]]
        Output: 12
        Explanation:
        ​​​​​
        Note:

        All given positions won't overlap.
        The squirrel can take at most one nut at one time.
        The given positions of nuts have no order.
        Height and width are positive integers. 3 <= height * width <= 10,000.
        The given positions contain at least one nut, only one tree and one squirrel.

        Args:
            height:
            width:
            tree:
            squirrel:
            nuts:

        Returns:

        """
        return self.one_pass(height, width, tree, squirrel, nuts)

    """
    1. Calculate distances between nuts to the tree, store in the array
    2. Calculate the distance between squirrel to the closest nut
    3. Add doubled distances between nuts and the tree and distance between squirrel and the 
    """
