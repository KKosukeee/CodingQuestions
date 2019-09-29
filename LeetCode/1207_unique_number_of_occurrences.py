"""
Solution for 1207. Unique Number of Occurrences
https://leetcode.com/problems/unique-number-of-occurrences/
"""
from collections import Counter

class Solution(object):
    """
    Runtime: 28 ms, faster than 100.00% of Python online submissions for Unique Number of Occurrences.
    Memory Usage: 11.7 MB, less than 100.00% of Python online submissions for Unique Number of Occurrences.
    """
    def initial_solution(self, arr):
        """
        Initial solution that runs in O(N) in space and time where N = len(arr)

        Args:
            arr(list[int]):

        Returns:
            bool:

        """
        counter = Counter(arr)
        count_set = set()
        for key in counter.keys():
            if counter[key] in count_set:
                return False
            count_set.add(counter[key])
        return True

    def cleaner_solution(self, arr):
        """
        Same as the initial_solution but slightly simpler

        Args:
            arr(list[int]):

        Returns:
            bool:

        """
        counter = Counter(arr)
        return len(set(counter.keys())) == len(set(counter.values()))

    def uniqueOccurrences(self, arr):
        """
        Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.



        Example 1:

        Input: arr = [1,2,2,1,1,3]
        Output: true
        Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
        Example 2:

        Input: arr = [1,2]
        Output: false
        Example 3:

        Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
        Output: true


        Constraints:

        1 <= arr.length <= 1000
        -1000 <= arr[i] <= 1000

        :type arr: List[int]
        :rtype: bool
        """
        return self.initial_solution(arr)