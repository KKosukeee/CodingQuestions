"""
Solution or 1235. Maximum Profit in Job Scheduling
https://leetcode.com/problems/maximum-profit-in-job-scheduling/
"""
import bisect

class Solution(object):
    def recursive(self, startTime, endTime, profit):
        """
        A recurisve solution that runs in O(N^N) in time and space

        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        start_time, end_time, sorted_profit = [], [], []
        for s, e, p in sorted(zip(startTime, endTime, profit)):
            start_time.append(s)
            end_time.append(e)
            sorted_profit.append(p)
        startTime = start_time
        endTime = end_time
        profit = sorted_profit

        def rec(i):
            if not i < len(profit):
                return 0
            max_profit = 0
            ii = bisect.bisect_left(startTime, endTime[i])
            for j in range(ii, len(profit)):
                max_profit = max(max_profit, rec(j))
            return profit[i] + max_profit

        return max([rec(i) for i in range(len(profit))])

    def dp(self, startTime, endTime, profit):
        """
        A dp solution that runs in O(N^2) in time and O(N) in space

        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        start_time, end_time, sorted_profit = [], [], []
        for s, e, p in sorted(zip(startTime, endTime, profit), key=lambda x: x[0]):
            start_time.append(s)
            end_time.append(e)
            sorted_profit.append(p)
        dp = {}

        def rec(i):
            if not i < len(sorted_profit):
                return 0
            if i in dp:
                return dp[i]
            ii = bisect.bisect_left(start_time, end_time[i])
            if not ii < len(sorted_profit):
                return sorted_profit[i]
            dp[i] = sorted_profit[i] + max([rec(j) for j in range(ii, len(sorted_profit))])
            return dp[i]

        return max([rec(i) for i in range(len(sorted_profit))])

    def bottom_up(self, startTime, endTime, profit):
        """
        A bottom-up solution that runs in O(Nlog(N)) in time and O(N) in space

        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        dp = [[0, 0]]  # [[3, 50],[4, 10],[]]
        for e, s, p in sorted(zip(endTime, startTime, profit)):
            i = bisect.bisect(dp, [s + 1]) - 1
            if p + dp[i][1] > dp[-1][1]:
                dp.append([e, p + dp[i][1]])
        return dp[-1][1]

    def jobScheduling(self, startTime, endTime, profit):
        """
        We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

        You're given the startTime , endTime and profit arrays, you need to output the maximum profit you can take such that there are no 2 jobs in the subset with overlapping time range.

        If you choose a job that ends at time X you will be able to start another job that starts at time X.



        Example 1:



        Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
        Output: 120
        Explanation: The subset chosen is the first and fourth job.
        Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
        Example 2:




        Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
        Output: 150
        Explanation: The subset chosen is the first, fourth and fifth job.
        Profit obtained 150 = 20 + 70 + 60.
        Example 3:



        Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
        Output: 6


        Constraints:

        1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
        1 <= startTime[i] < endTime[i] <= 10^9
        1 <= profit[i] <= 10^4

        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        return self.bottom_up(startTime, endTime, profit)

    """
    Brute force
    T: O(N!), S: O(N)
    1. Try to find the maximum profit starting from the ith job
    2. Do it for N jobs, and return the maximum

    Recursive solution
    T: O(N!), S: O(N)
    Base case
    1. When i exceeds the length job array
    Recursive case
    1. Loop through all jobs that start after the i-th job
        1.1 Call the recursive function with j-th job
        1.2 Take the maximum profit of starting from j-th job
    2. Add the maximum value with the current profit
    3. Return it

    DP solution:
    T: O(N), S:O(N)
    Base case
    1. When i exceeds the length of job array
    2. When i is in the dp hash map
    Recursive case
    1. Same as the Recursive solution
    ...
    2. Store the maximum value starting from the j-th job in dp hash map
    3. Return the current profit + the maximum value
    """