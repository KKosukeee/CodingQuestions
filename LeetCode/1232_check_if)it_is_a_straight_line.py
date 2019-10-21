"""
Solution for 1232. Check If It Is a Straight Line
https://leetcode.com/problems/check-if-it-is-a-straight-line/
"""

class Solution(object):
    """
    Runtime: 44 ms, faster than 100.00% of Python online submissions for Check If It Is a Straight Line.
    Memory Usage: 12 MB, less than 100.00% of Python online submissions for Check If It Is a Straight Line.
    """
    def checkStraightLine(self, coordinates):
        """
        You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.





        Example 1:



        Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
        Output: true
        Example 2:



        Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
        Output: false


        Constraints:

        2 <= coordinates.length <= 1000
        coordinates[i].length == 2
        -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
        coordinates contains no duplicate point.

        :type coordinates: List[List[int]]
        :rtype: bool
        """
        (p, q), (u, v) = coordinates[:2]
        return all((x - p) * (y - v) == (x - u) * (y - q) for x, y in coordinates[2:])

    """
    Slope = raise / run
          = run * raise
          = dx * dy
    """