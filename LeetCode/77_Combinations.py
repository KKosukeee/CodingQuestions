"""
Solution for 77. Combinations
"""
class Solution:
    """
    Runtime: 700 ms, faster than 24.60% of Python3 online submissions for Combinations.
    Memory Usage: 14.9 MB, less than 7.73% of Python3 online submissions for Combinations.
    """
    def combine(self, n, k):
        """
        Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
        Example:

        Input: n = 4, k = 2
        Output:
        [
          [2,4],
          [3,4],
          [2,3],
          [1,2],
          [1,3],
          [1,4],
        ]

        Args:
            n: range of numbers for the combination
            k: number of elements in each combination

        Returns:
            list<list>: two-dimensional array containing all combinations
        """
        # create range_array
        range_array = [i for i in range(1, n + 1)]

        # initialize a result array
        result = []

        # create a helper function with array and index as inputs
        def backtrack(nums, index, combo):

            # if index is out of the range, then it's a base case
            if len(combo) == k:
                result.append(combo)

            # otherwise, go into recursive block
            else:

                # loop through the array
                for i in range(index, len(nums)):
                    # call helper function recursively with index incremented by one
                    backtrack(nums, i + 1, combo + [nums[i]])

        # call the helper function with range_array, and index set to 0
        backtrack(range_array, 0, [])

        # return the result array
        return result
