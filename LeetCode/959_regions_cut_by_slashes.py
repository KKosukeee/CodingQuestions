"""
Solution for 959. Regions Cut By Slashes
https://leetcode.com/problems/regions-cut-by-slashes/
"""

class DSU:
    """
    Disjoint Set Union data structure
    """
    def __init__(self, N):
        """
        Initialization method
        Args:
            N:
        """
        self.p = [i for i in range(N)]

    def find(self, x):
        """
        This finds a root node given any node in a graph
        Args:
            x: int value

        Returns:
            int: as a parent node
        """
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        """
        This connects two node
        Args:
            x: int value
            y: int value

        Returns:

        """
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution(object):
    """
    Runtime: 392 ms, faster than 34.38% of Python3 online submissions for Regions Cut By Slashes.
    Memory Usage: 14 MB, less than 84.85% of Python3 online submissions for Regions Cut By Slashes.
    """
    def regionsBySlashes(self, grid):
        """
        In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

        (Note that backslash characters are escaped, so a \ is represented as "\\".)

        Return the number of regions.



        Example 1:

        Input:
        [
          " /",
          "/ "
        ]
        Output: 2
        Explanation: The 2x2 grid is as follows:

        Example 2:

        Input:
        [
          " /",
          "  "
        ]
        Output: 1
        Explanation: The 2x2 grid is as follows:

        Example 3:

        Input:
        [
          "\\/",
          "/\\"
        ]
        Output: 4
        Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
        The 2x2 grid is as follows:

        Example 4:

        Input:
        [
          "/\\",
          "\\/"
        ]
        Output: 5
        Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
        The 2x2 grid is as follows:

        Example 5:

        Input:
        [
          "//",
          "/ "
        ]
        Output: 3
        Explanation: The 2x2 grid is as follows:

        Args:
            grid: list<list<str>>

        Returns:
            int: represents number of region cut by slashes
        """
        N = len(grid)
        dsu = DSU(4 * N * N)
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4 * (r*N + c)
                if val in '/ ':
                    dsu.union(root + 0, root + 1)
                    dsu.union(root + 2, root + 3)
                if val in '\ ':
                    dsu.union(root + 0, root + 2)
                    dsu.union(root + 1, root + 3)

                # north/south
                if r+1 < N: dsu.union(root + 3, (root+4*N) + 0)
                if r-1 >= 0: dsu.union(root + 0, (root-4*N) + 3)
                # east/west
                if c+1 < N: dsu.union(root + 2, (root+4) + 1)
                if c-1 >= 0: dsu.union(root + 1, (root-4) + 2)

        return sum(dsu.find(x) == x for x in range(4*N*N))
