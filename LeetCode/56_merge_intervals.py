"""
Solution for 56. Merge Intervals
https://leetcode.com/problems/merge-intervals/
"""

class Solution:
    """
    Runtime: 52 ms, faster than 96.73% of Python3 online submissions for Merge Intervals.
    Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Merge Intervals.
    """
    # Time: O(n^2), Space: O(1)
    def naive_approach(self, intervals):
        """
        Merges the sub-array if there is a overlap
        Args:
            intervals: 2D matrix where each element is integer data type

        Returns:
            list<list<int>>: merged intervals representing [[start, end]...]
        """
        # Sort the array
        intervals.sort()

        # Initialize i and j
        i, j = 0, 1

        # Loop for each array within the intervals
        while i <= j and j < len(intervals):

            # Check for current[1] and checking[0]
            if intervals[i][1] >= intervals[j][0]:

                # If condition meets, then update current
                intervals[i][0] = min(intervals[i][0], intervals[j][0])
                intervals[i][1] = max(intervals[i][1], intervals[j][1])

                # Remove the jth element in the array
                intervals = intervals[:j] + intervals[j + 1:]
            else:
                j += 1

            if not j < len(intervals):
                i += 1
                j = i + 1

        return intervals

    # Time: O(nlog(n)), Space: O(n)
    def optimal_approach(self, intervals):
        """
        Merges the sub-array if there is a overlap
        Args:
            intervals: 2D matrix where each element is integer data type

        Returns:
            list<list<int>>: merged intervals representing [[start, end]...]
        """
        merged = []
        intervals.sort()

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][0] = min(merged[-1][0], interval[0])
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

    def merge(self, intervals):
        """
        Main function for merging intervals
        Args:
            intervals: 2D matrix where each element is integer data type

        Returns:
            list<list<int>>: merged intervals representing [[start, end]...]
        """
        return self.optimal_approach(intervals)
