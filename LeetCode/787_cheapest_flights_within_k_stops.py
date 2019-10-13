"""
Solution for 787. Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""
import heapq
from collections import defaultdict
from collections import deque

class Solution(object):
    """
    Runtime: 72 ms, faster than 77.57% of Python online submissions for Cheapest Flights Within K Stops.
    Memory Usage: 17.9 MB, less than 15.79% of Python online submissions for Cheapest Flights Within K Stops.
    """
    def dijkstra(self, n, flights, src, dst, K):
        """
        A dijkstra algorithm that runs in O(E + Vlog(V)) in time and O(V) in space

        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((w, v))
        pq = [(0, 0, src)]
        while pq:
            w, k, u = heapq.heappop(pq)
            if u == dst:
                return w
            if k > K:
                continue
            for ww, v in graph[u]:
                heapq.heappush(pq, (w + ww, k + 1, v))
        return -1

    def bfs(self, n, flights, src, dst, K):
        """
        A BFS solution that runs in O(E+V) in time and O(V) in space

        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((w, v))

        queue = deque([(0, K, src)])
        min_cost = float('inf')

        while queue:
            w, k, u = queue.popleft()
            if u == dst:
                min_cost = min(min_cost, w)
                continue
            if k >= 0 and w <= min_cost:
                for ww, v in graph[u]:
                    queue.append((ww + w, k - 1, v))
        return min_cost if min_cost != float('inf') else -1

    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

        Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

        Example 1:
        Input:
        n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0, dst = 2, k = 1
        Output: 200
        Explanation:
        The graph looks like this:


        The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
        Example 2:
        Input:
        n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0, dst = 2, k = 0
        Output: 500
        Explanation:
        The graph looks like this:


        The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
        Note:

        The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
        The size of flights will be in range [0, n * (n - 1) / 2].
        The format of each flight will be (src, dst, price).
        The price of each flight will be in the range [1, 10000].
        k is in the range of [0, n - 1].
        There will not be any duplicated flights or self cycles.

        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        return self.dijkstra(n, flights, src, dst, K)

    """
    dijkstra algorithm
    1. 
    """