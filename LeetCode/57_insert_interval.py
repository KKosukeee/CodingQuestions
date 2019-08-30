"""
Solution for 57. Insert Interval
https://leetcode.com/problems/insert-interval/
"""
import bisect

class Solution:
    """
    Runtime: 88 ms, faster than 91.51% of Python3 online submissions for Insert Interval.
    Memory Usage: 17.2 MB, less than 8.00% of Python3 online submissions for Insert Interval.
    """
    def insert(self, intervals, newInterval):
        """
        Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

        You may assume that the intervals were initially sorted according to their start times.

        Example 1:

        Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
        Output: [[1,5],[6,9]]
        Example 2:

        Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
        Output: [[1,2],[3,10],[12,16]]
        Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
        NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

        Args:
            intervals(list[list[int]]):
            newInterval(list[int]):

        Returns:
            list[list[int]]:

        """
        left_position = bisect.bisect_left(intervals, newInterval)
        intervals.insert(left_position, newInterval)
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            if merged[-1][1] >= intervals[i][0]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])
        return merged

    # [1,6] 0
    # 1. interval falls into an interval
    # 2. interval's start time falls into an interval
    # 3. interval's end time falls into an interval
    # 4. interval doesn't fall into an interval at all.
    # If one side falls into an interval, while other doesn't, update the one that doesn't

    # Find the left and right position
    # Check if both pointers fall into the interval or not
    # Binary search the left and right positions, and check if they overlap or not
