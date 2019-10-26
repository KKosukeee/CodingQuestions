"""
Solution for 838. Push Dominoes
https://leetcode.com/problems/push-dominoes/
"""
class Solution:
    """
    Runtime: 136 ms, faster than 73.10% of Python3 online submissions for Push Dominoes.
    Memory Usage: 21 MB, less than 25.00% of Python3 online submissions for Push Dominoes.
    """
    def simple_solution(self, dominoes: str) -> str:
        """
        A simple solution that runs in O(N) in time and space

        Args:
            dominoes:

        Returns:

        """
        dominoes = list(dominoes)
        nodes = [(-1, 'L')] + [(i, x) for i, x in enumerate(dominoes) if x != '.'] + [
            (len(dominoes), 'R')]
        for (i, x), (j, y) in zip(nodes, nodes[1:]):
            if x == y:
                for k in range(i + 1, j):
                    dominoes[k] = x
            elif x == 'R' and y == 'L':
                k, l = i, j
                while k < l:
                    dominoes[k] = x
                    dominoes[l] = y
                    k, l = k + 1, l - 1
                if ((j - i + 1) % 2) != 0:
                    dominoes[(j + i) // 2] = '.'
        return ''.join(dominoes)

    def prefix_sums(self, dominoes: str) -> str:
        """
        Another solution that runs in O(N) in time and space

        Args:
            dominoes:

        Returns:

        """
        dominoes = list(dominoes)
        R = [1 if dominoes[0] == 'R' else 0]
        L = [1 if dominoes[-1] == 'L' else 0]
        for domino in dominoes[1:]:
            if domino == 'L':
                R.append(0)
            elif domino == 'R':
                R.append(1)
            else:
                R.append(R[-1] + 1 if R[-1] > 0 else 0)
        for domino in reversed(dominoes[:-1]):
            if domino == 'R':
                L.append(0)
            elif domino == 'L':
                L.append(1)
            else:
                L.append(L[-1] + 1 if L[-1] > 0 else 0)

        for i in range(len(dominoes)):
            j = len(dominoes) - i - 1
            if R[i] == L[j]:
                dominoes[i] = '.'
            elif R[i] == 0 or L[j] == 0:
                dominoes[i] = 'R' if L[j] == 0 else 'L'
            else:
                dominoes[i] = 'R' if R[i] < L[j] else 'L'
        return ''.join(dominoes)

    def pushDominoes(self, dominoes: str) -> str:
        """
        There are N dominoes in a line, and we place each domino vertically upright.

        In the beginning, we simultaneously push some of the dominoes either to the left or to the right.



        After each second, each domino that is falling to the left pushes the adjacent domino on the left.

        Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

        When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

        For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

        Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

        Return a string representing the final state.

        Example 1:

        Input: ".L.R...LR..L.."
        Output: "LL.RR.LLRRLL.."
        Example 2:

        Input: "RR.L"
        Output: "RR.L"
        Explanation: The first domino expends no additional force on the second domino.
        Note:

        0 <= N <= 10^5
        String dominoes contains only 'L', 'R' and '.'

        Args:
            dominoes:

        Returns:

        """
        return self.simple_solution(dominoes)

    """
    Two prefix sums
    T: O(N), S: O(N)
    1. Loop through left to right
        1.1 If 'R' is found, updates everything to the R until a L is found
    2. Loop thorugh right to left
        2.1 If 'L' is found, updates everything to the L until a R is found
    3. Loop through the dominoes
        3.1 Compare the distance for each domino to the left and right
        3.2 If R[i] < L[i], then it becomes R
        3.3 If R[i] > L[i], then it becomes L
        3.4 If R[i] == L[i], then it stays upright!
    4. Return the modified dominoes

     [0, 0, 0, 1, 2, 3, 4, 0, 1, 2, 3, 0, 0, 0] -> R
    +[2, 1, 0, 0, 4, 3, 2, 1, 0, 3, 2, 1, 0, 0] -> L
    -------------------------------------------
     [L, L, ., R, R, ., L, L, R, R, L, L, ., .]
    """