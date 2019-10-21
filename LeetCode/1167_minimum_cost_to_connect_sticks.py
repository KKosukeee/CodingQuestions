"""
Solution for 1167. Minimum Cost to Connect Sticks
https://leetcode.com/problems/minimum-cost-to-connect-sticks/https://leetcode.com/problems/minimum-cost-to-connect-sticks/
"""
import heapq

class Solution(object):
    """
    Runtime: 360 ms, faster than 99.52% of Python online submissions for Minimum Cost to Connect Sticks.
    Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for Minimum Cost to Connect Sticks.
    """
    def first_solution(self, sticks):
        """
        First solution that runs in O(Nlog(N)) in time and O(1) in space

        :type sticks: List[int]
        :rtype: int
        """
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            first, second = heapq.heappop(sticks), heapq.heappop(sticks)
            cost += first + second
            heapq.heappush(sticks, first + second)
        return cost

    def second_solution(self, sticks):
        """
        Second solution that runs in O(Nlog(N)) in time and O(N) in space

        :type sticks: List[int]
        :rtype: int
        """
        cost, combined = 0, []
        sticks.sort()
        i, j = 0, 0

        while i < len(sticks) or j < len(combined):
            first, second = float('inf'), float('inf')
            if i < len(sticks):
                first = sticks[i]
            if j < len(combined):
                second = combined[j]
            if first < second:
                i += 1
            else:
                j += 1
            first_smallest = min(first, second)

            if i < len(sticks) or j < len(combined):
                first, second = float('inf'), float('inf')
                if i < len(sticks):
                    first = sticks[i]
                if j < len(combined):
                    second = combined[j]
                if first < second:
                    i += 1
                else:
                    j += 1
                second_smallest = min(first, second)
                cost += first_smallest + second_smallest
                combined.append(first_smallest + second_smallest)

        return cost

    def connectSticks(self, sticks):
        """
        You have some sticks with positive integer lengths.

        You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  You perform this action until there is one stick remaining.

        Return the minimum cost of connecting all the given sticks into one stick in this way.



        Example 1:

        Input: sticks = [2,4,3]
        Output: 14
        Example 2:

        Input: sticks = [1,8,3,5]
        Output: 30


        Constraints:

        1 <= sticks.length <= 10^4
        1 <= sticks[i] <= 10^4

        :type sticks: List[int]
        :rtype: int
        """
        return self.second_solution(sticks)
    