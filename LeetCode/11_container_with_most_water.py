"""
Solution for 11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
"""

class Solution:
    """
    Runtime: 68 ms, faster than 58.85% of Python3 online submissions for Container With Most Water.
    Memory Usage: 14.4 MB, less than 5.18% of Python3 online submissions for Container With Most
    Water
    """
    def recursive_approach(self, height):
        """
        Recursive approach which results time limit exceeded error :(
        Args:
            height: list of integers to calculate most water

        Returns:
            int: maximum water you can fill in
        """
        if len(height) == 2:
            return min(height[0], height[1])
        else:
            last_element = height[-1]
            first_element = height[0]
            area = min(last_element, first_element) * (len(height) - 1)

            if first_element > last_element:
                return max(area, self.recursive_approach(height[:-1]))
            else:
                return max(area, self.recursive_approach(height[1:]))

    def iterative_approach(self, height):
        """
        Iterative approach which is accepted in this question
        Args:
            height: list of integers to calculate most water

        Returns:
            int: maximum water you can fill in
        """
        start_pointer = 0
        end_pointer = len(height) - 1
        max_area = 0

        while start_pointer != end_pointer:
            max_area = max(max_area, min(height[start_pointer], height[end_pointer]) * (
                        end_pointer - start_pointer))
            if height[start_pointer] > height[end_pointer]:
                end_pointer -= 1
            else:
                start_pointer += 1

        return max_area

    def maxArea(self, height):
        """
        Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate
        (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and
        (i, 0). Find two lines, which together with x-axis forms a container, such that the
        container contains the most water.

        Note: You may not slant the container and n is at least 2.

        The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the
        max area of water (blue section) the container can contain is 49.

        Example:

        Input: [1,8,6,2,5,4,8,3,7]
        Output: 49
        Args:
            height: list of integers to calculate most water

        Returns:
            int: maximum water you can fill in
        """
        return self.iterative_approach(height)
