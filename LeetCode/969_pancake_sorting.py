"""
Solution for 969. Pancake Sorting
https://leetcode.com/problems/pancake-sorting/
"""
from typing import List

class Solution:
  """
  Runtime: 28 ms, faster than 99.37% of Python3 online submissions for Pancake Sorting.
  Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Pancake Sorting.
  """
  def pancakeSort(self, A: List[int]) -> List[int]:
    """
    Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length, then reverse the order of the first k elements of A.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.

    Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.



    Example 1:

    Input: [3,2,4,1]
    Output: [4,2,4,3]
    Explanation:
    We perform 4 pancake flips, with k values 4, 2, 4, and 3.
    Starting state: A = [3, 2, 4, 1]
    After 1st flip (k=4): A = [1, 4, 2, 3]
    After 2nd flip (k=2): A = [4, 1, 2, 3]
    After 3rd flip (k=4): A = [3, 2, 1, 4]
    After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted.
    Example 2:

    Input: [1,2,3]
    Output: []
    Explanation: The input is already sorted, so there is no need to flip anything.
    Note that other answers, such as [3, 3], would also be accepted.


    Note:

    1 <= A.length <= 100
    A[i] is a permutation of [1, 2, ..., A.length]

    Args:
      A:

    Returns:

    """
    res, n = [], len(A)
    for i in range(len(A)):
      j = A.index(max(A[:n-i]))
      A[:j+1] = reversed(A[:j+1])
      res.append(j+1)
      A[:n-i] = reversed(A[:n-i])
      res.append(n-i)
    return res
  """
    [3,2,4,1]
    [2,3,4,1]
    [4,3,2,1]
    [1,2,3,4]
  ->[2, 3, 4]
  """