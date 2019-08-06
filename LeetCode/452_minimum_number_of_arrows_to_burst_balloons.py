"""
Solution for 452. Minimum Number of Arrows to Burst Balloons
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
"""

class Solution:
    """
    Runtime: 504 ms, faster than 20.75% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.
    Memory Usage: 19.3 MB, less than 5.72% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.
    """
    def findMinArrowShots(self, points):
        """
        There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

        An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

        Example:

        Input:
        [[10,16], [2,8], [1,6], [7,12]]

        Output:
        2

        Explanation:
        One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
        Args:
            points: list<list<int>>

        Returns:
            int
        """
        total_arrows = 0
        points.sort(key=lambda x: (x[0], x[1]))
        i, n = 0, len(points)

        while i < n:
            j = i + 1
            m = points[i][1]
            while j < n and m >= points[j][0]:
                m = min(m, points[j][1])
                j += 1
            total_arrows += 1
            i = j
        return total_arrows
