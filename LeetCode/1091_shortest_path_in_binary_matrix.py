"""
Solution for 1091. Shortest Path in Binary Matrix
https://leetcode.com/problems/shortest-path-in-binary-matrix/
"""
from collections import deque
from typing import List
from heapq import heappush, heappop

class Solution:
    """
    Runtime: 940 ms, faster than 23.14% of Python3 online submissions for Shortest Path in Binary Matrix.
    Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Shortest Path in Binary Matrix.
    """
    def bfs(self, grid: List[List[int]]) -> int:
        """
        A BFS solution that runs an error due to the maximum recursion matter

        Args:
            grid(list[list[int]]):

        Returns:
            int:

        """
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        queue = deque([(0, 0, 1)])
        while queue:
            i, j, v = queue.popleft()
            if grid[i][j] == 1:
                continue
            if i == len(grid) - 1 and j == len(grid) - 1:
                return v
            for ii, jj in self.neighbours(i, j, grid):
                queue.append((ii, jj, v + 1))
            grid[i][j] = 1
        return -1

    def neighbours(self, i, j, grid):
        """
        Returns neighbour cells

        Args:
            i(int):
            j(int):
            grid(list[list[int]]):

        Returns:
            list[tuple[int, int]]

        """
        neighbours = []
        for ii, jj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            if 0 <= i + ii < len(grid) and 0 <= j + jj < len(grid[0]) and grid[i + ii][j + jj] == 0:
                neighbours.append((i + ii, j + jj))
        return neighbours

    def a_star(self, grid):
        """
        An A* algorithm

        Args:
            grid(list[list[int]]):

        Returns:
            int:

        """

        def a_star_graph_search(start, goal_function, successor_function, heuristic):
            visited = set()
            came_from = dict()
            distance = {start: 0}
            frontier = PriorityQueue()
            frontier.add(start)
            while frontier:
                node = frontier.pop()
                if node in visited:
                    continue
                if goal_function(node):
                    return reconstruct_path(came_from, start, node)
                visited.add(node)
                for successor in successor_function(node):
                    frontier.add(successor, distance[node] + 1 + heuristic(successor))
                    if (successor not in distance or distance[node] + 1 < distance[successor]):
                        distance[successor] = distance[node] + 1
                        came_from[successor] = node
            return None

        def reconstruct_path(came_from, start, end):
            """
            >>> came_from = {'b': 'a', 'c': 'a', 'd': 'c', 'e': 'd', 'f': 'd'}
            >>> reconstruct_path(came_from, 'a', 'e')
            ['a', 'c', 'd', 'e']
            """
            reverse_path = [end]
            while end != start:
                end = came_from[end]
                reverse_path.append(end)
            return list(reversed(reverse_path))

        def get_goal_function(grid):
            M = len(grid)
            N = len(grid[0])

            def is_bottom_right(cell):
                return cell == (M - 1, N - 1)

            return is_bottom_right

        def get_successor_function(grid):
            def get_clear_adjacent_cells(cell):
                i, j = cell
                return (
                    (i + a, j + b)
                    for a in (-1, 0, 1)
                    for b in (-1, 0, 1)
                    if a != 0 or b != 0
                    if 0 <= i + a < len(grid)
                    if 0 <= j + b < len(grid[0])
                    if grid[i + a][j + b] == 0
                )

            return get_clear_adjacent_cells

        def get_heuristic(grid):
            M, N = len(grid), len(grid[0])
            (a, b) = goal_cell = (M - 1, N - 1)

            def get_clear_path_distance_from_goal(cell):
                (i, j) = cell
                return max(abs(a - i), abs(b - j))

            return get_clear_path_distance_from_goal

        class PriorityQueue:

            def __init__(self, iterable=[]):
                self.heap = []
                for value in iterable:
                    heappush(self.heap, (0, value))

            def add(self, value, priority=0):
                heappush(self.heap, (priority, value))

            def pop(self):
                priority, value = heappop(self.heap)
                return value

            def __len__(self):
                return len(self.heap)

        shortest_path = a_star_graph_search((0, 0), get_goal_function(grid),
                                            get_successor_function(grid), get_heuristic(grid))
        if shortest_path is None or grid[0][0] == 1:
            return -1
        else:
            return len(shortest_path)
        return -1

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        In an N by N square grid, each cell is either empty (0) or blocked (1).

        A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

        Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
        C_1 is at location (0, 0) (ie. has value grid[0][0])
        C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
        If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
        Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.



        Example 1:

        Input: [[0,1],[1,0]]


        Output: 2

        Example 2:

        Input: [[0,0,0],[1,1,0],[1,1,0]]


        Output: 4



        Note:

        1 <= grid.length == grid[0].length <= 100
        grid[r][c] is 0 or 1

        Args:
            grid(list[list[int]]):

        Returns:
            int:

        """
        return self.bfs(grid)

    """
    [[0,0,0,0,1,1],
     [0,1,0,0,1,0],
     [1,1,0,1,0,0],
     [0,1,0,0,1,1],
     [0,1,0,0,0,1],
     [0,0,1,0,0,0]]

    DFS: T->O(N^2), S->O(N^2)
    1. Create a stack with initial position of (0, 0)
    2. Loop while stack isn't empty
        2.1 Pop a node from the stack
        2.2 Get 8 neighbours
        2.3 If the neighour cell in the visited dict, add the value and update shortest variable
        2.4 If the neighour cell isn't in the visited, append to the stack
        2.5 Append current cell to the visited dict
    3. Return the shortest variable as a result

    BFS
    """