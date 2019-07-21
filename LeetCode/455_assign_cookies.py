"""
Solution for 455. Assign Cookies
https://leetcode.com/problems/assign-cookies/
"""

class Solution:
    """
    Runtime: 200 ms, faster than 10.37% of Python3 online submissions for Assign Cookies.
    Memory Usage: 15.4 MB, less than 5.53% of Python3 online submissions for Assign Cookies.
    """
    def findContentChildren(self, g, s):
        """
        Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

        Note:
        You may assume the greed factor is always positive.
        You cannot assign more than one cookie to one child.

        Example 1:
        Input: [1,2,3], [1,1]

        Output: 1

        Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
        And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
        You need to output 1.
        Example 2:
        Input: [1,2], [1,2,3]

        Output: 2

        Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
        You have 3 cookies and their sizes are big enough to gratify all of the children,
        You need to output 2.
        Args:
            g: list<int> for the greedy kids
            s: list<int> for the cookies the parents have

        Returns:
            int: representing the number of kids who can get the cookies
        """
        # 1,2) Sorting
        g.sort()
        s.sort()

        # 3) Do the rest
        i, j = 0, 0
        max_g = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
                j += 1
                max_g += 1
            else:
                j += 1

        return max_g
