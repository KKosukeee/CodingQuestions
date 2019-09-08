"""
Solution for 955. Delete Columns to Make Sorted II
https://leetcode.com/problems/delete-columns-to-make-sorted-ii/
"""
from typing import List

class Solution:
    """
    Runtime: 52 ms, faster than 49.39% of Python3 online submissions for Delete Columns to Make Sorted II.
    Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Delete Columns to Make Sorted II.
    """
    def minDeletionSize(self, A: List[str]) -> int:
        """
        We are given an array A of N lowercase letter strings, all of the same length.

        Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

        For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef","vyz"].

        Suppose we chose a set of deletion indices D such that after deletions, the final array has its elements in lexicographic order (A[0] <= A[1] <= A[2] ... <= A[A.length - 1]).

        Return the minimum possible value of D.length.



        Example 1:

        Input: ["ca","bb","ac"]
        Output: 1
        Explanation:
        After deleting the first column, A = ["a", "b", "c"].
        Now A is in lexicographic order (ie. A[0] <= A[1] <= A[2]).
        We require at least 1 deletion since initially A was not in lexicographic order, so the answer is 1.
        Example 2:

        Input: ["xc","yb","za"]
        Output: 0
        Explanation:
        A is already in lexicographic order, so we don't need to delete anything.
        Note that the rows of A are not necessarily in lexicographic order:
        ie. it is NOT necessarily true that (A[0][0] <= A[0][1] <= ...)
        Example 3:

        Input: ["zyx","wvu","tsr"]
        Output: 3
        Explanation:
        We have to delete every column.


        Note:

        1 <= A.length <= 100
        1 <= A[i].length <= 100

        Args:
            A(list[str]):

        Returns:
            int:

        """
        count, valid = 0, [False] * len(A)
        for col in zip(*A):
            if all(valid[i] or col[i] <= col[i + 1] for i in range(len(col) - 1)):
                for i in range(len(A) - 1):
                    valid[i] = valid[i] or col[i] < col[i + 1]
            else:
                count += 1
        return count

    # oxx
    # abx
    # agz
    # bgc
    # bfc

    # aabb bggf xzcc
    # FTFF

    #  ?xo
    #  aba
    #  aab
    #  bcc

    #  *
    # ca
    # bb
    # ac

    # *
    # xc
    # yb
    # za

    #    *
    # zyx
    # wvu
    # tsr

    #  **
    #  aa
    #  ab
    #  bc

    #  * *
    #  ab
    #  aa
    #  bc

    # ac
    # ab
    # bd

