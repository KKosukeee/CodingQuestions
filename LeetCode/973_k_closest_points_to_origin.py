"""
Solution for 973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/
"""
import heapq
import math
from typing import List

class Solution:
    def heap(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        A heap solution that runs in O(N+Klog(N)) in time and O(N) in space

        Args:
            points:
            K:

        Returns:

        """
        for i, pt in enumerate(points):
            points[i] = [self.dist(pt, (0, 0)), pt[0], pt[1]]
        heapq.heapify(points)
        result = []
        for _ in range(K):
            d, x, y = heapq.heappop(points)
            result.append([x, y])
        return result

    def sort(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        A sort solution that runs in O(Nlog(N)) in time and O(1) in space

        Args:
            points:
            K:

        Returns:

        """
        points.sort(key=lambda pt: self.dist(pt, (0, 0)))
        return points[:K]

    def optimal(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        An optimal solution that runs in O(Klog(N)) in time and O(K) in space

        Args:
            points:
            K:

        Returns:

        """
        pq = []
        for i, j in points:
            dist = self.dist((i, j), (0, 0))
            heapq.heappush(pq, (-dist, i, j))
            if len(pq) > K:
                _ = heapq.heappop(pq)

        return [p[1:] for p in pq]

    def optimal_onelinear(self, points: List[List[int]], K: int) -> List[
        List[int]]:
        """
        One-linear

        Args:
            points:
            K:

        Returns:

        """
        return heapq.nsmallest(K, points, lambda x: x[0] ** 2 + x[1] ** 2)

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

        (Here, the distance between two points on a plane is the Euclidean distance.)

        You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)



        Example 1:

        Input: points = [[1,3],[-2,2]], K = 1
        Output: [[-2,2]]
        Explanation:
        The distance between (1, 3) and the origin is sqrt(10).
        The distance between (-2, 2) and the origin is sqrt(8).
        Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
        We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
        Example 2:

        Input: points = [[3,3],[5,-1],[-2,4]], K = 2
        Output: [[3,3],[-2,4]]
        (The answer [[-2,4],[3,3]] would also be accepted.)


        Note:

        1 <= K <= points.length <= 10000
        -10000 < points[i][0] < 10000
        -10000 < points[i][1] < 10000

        Args:
            points:
            K:

        Returns:

        """
        return self.optimal_onelinear(points, K)

    def dist(self, pt, origin):
        """
        A helper method

        Args:
            pt:
            origin:

        Returns:

        """
        return math.sqrt((pt[0] - origin[0]) ** 2 + (pt[1] - origin[1]) ** 2)