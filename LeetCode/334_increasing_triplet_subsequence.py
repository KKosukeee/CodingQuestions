"""
Solution for 334. Increasing Triplet Subsequence
https://leetcode.com/problems/increasing-triplet-subsequence/
"""

class Solution:
    """
    Runtime: 40 ms, faster than 75.02% of Python3 online submissions for Increasing Triplet
        Subsequence.
    Memory Usage: 13.5 MB, less than 6.80% of Python3 online submissions for Increasing Triplet
        Subsequence.
    """
    def increasingTriplet(self, nums):
        """
        Given an unsorted array return whether an increasing subsequence of length 3 exists or not
        in the array.

        Formally the function should:

        Return true if there exists i, j, k
        such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
        Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

        Example 1:

        Input: [1,2,3,4,5]
        Output: true
        Example 2:

        Input: [5,4,3,2,1]
        Output: false
        Args:
            nums:

        Returns:

        """
        seq = []

        # loop for each number in nums array
        for num in nums:

            # check if seq array is empty or num is greather than its previous
            if not seq or num > seq[-1]:

                # if so, append the num in seq array
                seq.append(num)

                # if you found i, j and k such that i < j < k, the return True
                if len(seq) == 3:
                    return True

            # check if ith element in seq is greater than current num
            elif num <= seq[0]:
                # if so, replace that element
                seq[0] = num

            # check if jth element is seq is greater than current num
            elif num <= seq[1]:
                # if so, replace that element
                seq[1] = num

        return False
