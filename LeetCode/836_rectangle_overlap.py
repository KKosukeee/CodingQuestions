"""
Solution for 836. Rectangle Overlap
https://leetcode.com/problems/rectangle-overlap/
"""
class Solution:
    """
    Runtime: 36 ms, faster than 68.28% of Python3 online submissions for Rectangle Overlap.
    Memory Usage: 13.8 MB, less than 8.33% of Python3 online submissions for Rectangle Overlap.
    """
    def isRectangleOverlap(self, rec1, rec2):
        """
        A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

        Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

        Given two (axis-aligned) rectangles, return whether they overlap.

        Example 1:

        Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
        Output: true
        Example 2:

        Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
        Output: false
        Notes:

        Both rectangles rec1 and rec2 are lists of 4 integers.
        All coordinates in rectangles will be between -10^9 and 10^9.
        Args:
            rec1(list[int]):
            rec2(list[int]):

        Returns:
            bool:
        """
        horizontal = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
        vertical = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])
        if horizontal > 0 and vertical > 0:
            return horizontal * vertical > 0
        return False
