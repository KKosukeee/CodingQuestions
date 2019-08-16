"""
Solution for 1041. Robot Bounded In Circle
https://leetcode.com/problems/robot-bounded-in-circle/
"""
class Solution:
    """
    Runtime: 32 ms, faster than 92.93% of Python3 online submissions for Robot Bounded In Circle.
    Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Robot Bounded In Circle.
    """
    def isRobotBounded(self, instructions):
        """
        On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

        "G": go straight 1 unit;
        "L": turn 90 degrees to the left;
        "R": turn 90 degress to the right.
        The robot performs the instructions given in order, and repeats them forever.

        Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.



        Example 1:

        Input: "GGLLGG"
        Output: true
        Explanation:
        The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
        When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
        Example 2:

        Input: "GG"
        Output: false
        Explanation:
        The robot moves north indefinitely.
        Example 3:

        Input: "GL"
        Output: true
        Explanation:
        The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...


        Note:

        1 <= instructions.length <= 100
        instructions[i] is in {'G', 'L', 'R'}
        Args:
            instructions(str):

        Returns:
            bool:
        """
        # UP, LEFT, DOWN and RIGHT
        movements = {0: [0, 1], 1: [-1, 0], 2: [0, -1], 3: [1, 0]}
        direction = 0
        coordinate = [0, 0]
        for i in instructions:
            if i == 'G':
                coordinate[0] += movements[direction][0]
                coordinate[1] += movements[direction][1]
            else:
                if i == 'L':
                    direction = (direction + 1) % 4
                else:
                    direction = (direction - 1) % 4
        return direction != 0 or coordinate == [0, 0]
