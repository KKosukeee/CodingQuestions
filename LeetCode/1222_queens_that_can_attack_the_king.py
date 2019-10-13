"""
Solution for 1222. Queens That Can Attack the King
https://leetcode.com/problems/queens-that-can-attack-the-king/
"""

class Solution(object):
    """
    Runtime: 24 ms, faster than 100.00% of Python online submissions for Queens That Can Attack the King.
    Memory Usage: 11.9 MB, less than 100.00% of Python online submissions for Queens That Can Attack the King.
    """
    def initial_solution(self, queens, king):
        """
        An initial solution that runs in O(1) in time and O(N) in space

        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        queen_set = set(tuple(queen) for queen in queens)
        result = []
        for i, j in self.diagonal_forward(king):
            if (i, j) in queen_set:
                result.append([i, j])
                break
        for i, j in self.diagonal_backward(king):
            if (i, j) in queen_set:
                result.append([i, j])
                break
        for i, j in self.vertical_up(king):
            if (i, j) in queen_set:
                result.append([i, j])
                break
        for i, j in self.diagonal_forward2(king):
            if (i, j) in queen_set:
                result.append([i, j])
                break
        for i, j in self.diagonal_backward2(king):
            if (i, j) in queen_set:
                result.append([i, j])
                break
        for i, j in self.vertical_down(king):
            if (i, j) in queen_set:
                result.append([i, j])
                break
        for i, j in self.horizontal_left(king):
            if (i, j) in queen_set:
                result.append([i, j])
                break
        for i, j in self.horizontal_right(king):
            if (i, j) in queen_set:
                result.append([i, j])
                break
        return result

    def clean_solution(self, queens, king):
        """
        A cleaner solution that runs in O(1) in time and O(N) in space

        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        queens = set(tuple(queen) for queen in queens)
        directions = [
            (-1, 0), (1, 0),
            (0, -1), (0, 1),
            (1, 1), (-1, -1),
            (-1, 1), (1, -1),
        ]
        result = []
        for id, jd in directions:
            i, j = king
            while 0 <= i + id < 8 and 0 <= j + jd < 8:
                if (i + id, j + jd) in queens:
                    result.append((i + id, j + jd))
                    break
                i, j = i + id, j + jd
        return result

    def queensAttacktheKing(self, queens, king):
        """
        On an 8x8 chessboard, there can be multiple Black Queens and one White King.

        Given an array of integer coordinates queens that represents the positions of the Black Queens, and a pair of coordinates king that represent the position of the White King, return the coordinates of all the queens (in any order) that can attack the King.



        Example 1:



        Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
        Output: [[0,1],[1,0],[3,3]]
        Explanation:
        The queen at [0,1] can attack the king cause they're in the same row.
        The queen at [1,0] can attack the king cause they're in the same column.
        The queen at [3,3] can attack the king cause they're in the same diagnal.
        The queen at [0,4] can't attack the king cause it's blocked by the queen at [0,1].
        The queen at [4,0] can't attack the king cause it's blocked by the queen at [1,0].
        The queen at [2,4] can't attack the king cause it's not in the same row/column/diagnal as the king.
        Example 2:



        Input: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
        Output: [[2,2],[3,4],[4,4]]
        Example 3:



        Input: queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]
        Output: [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]


        Constraints:

        1 <= queens.length <= 63
        queens[0].length == 2
        0 <= queens[i][j] < 8
        king.length == 2
        0 <= king[0], king[1] < 8
        At most one piece is allowed in a cell.

        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        return self.clean_solution(queens, king)

    def diagonal_forward(self, king):
        cells = []
        i, j = 0, 0
        while 0 <= king[0] + i < 8 and 0 <= king[1] + j < 8:
            cells.append([king[0] + i, king[1] + j])
            i, j = i + 1, j + 1
        return cells

    def diagonal_backward(self, king):
        cells = []
        i, j = 0, 0
        while 0 <= king[0] + i < 8 and 0 <= king[1] + j < 8:
            cells.append([king[0] + i, king[1] + j])
            i, j = i - 1, j - 1
        return cells

    def diagonal_forward2(self, king):
        cells = []
        i, j = 0, 0
        while 0 <= king[0] + i < 8 and 0 <= king[1] + j < 8:
            cells.append([king[0] + i, king[1] + j])
            i, j = i - 1, j + 1
        return cells

    def diagonal_backward2(self, king):
        cells = []
        i, j = 0, 0
        while 0 <= king[0] + i < 8 and 0 <= king[1] + j < 8:
            cells.append([king[0] + i, king[1] + j])
            i, j = i + 1, j - 1
        return cells

    def vertical_up(self, king):
        cells = []
        i, j = 0, 0
        while 0 <= king[0] + i < 8 and 0 <= king[1] + j < 8:
            cells.append([king[0] + i, king[1] + j])
            i -= 1
        return cells

    def vertical_down(self, king):
        cells = []
        i, j = 0, 0
        while 0 <= king[0] + i < 8 and 0 <= king[1] + j < 8:
            cells.append([king[0] + i, king[1] + j])
            i += 1
        return cells

    def horizontal_left(self, king):
        cells = []
        i, j = 0, 0
        while 0 <= king[0] + i < 8 and 0 <= king[1] + j < 8:
            cells.append([king[0] + i, king[1] + j])
            j -= 1
        return cells

    def horizontal_right(self, king):
        cells = []
        i, j = 0, 0
        while 0 <= king[0] + i < 8 and 0 <= king[1] + j < 8:
            cells.append([king[0] + i, king[1] + j])
            j += 1
        return cells
    