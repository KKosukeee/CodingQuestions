"""
Solution for 743. Network Delay Time
https://leetcode.com/problems/network-delay-time/
"""
from collections import defaultdict
import heapq

class Solution(object):
    """
    Runtime: 432 ms, faster than 70.34% of Python online submissions for Network Delay Time.
    Memory Usage: 14.1 MB, less than 64.29% of Python online submissions for Network Delay Time.
    """
    def dijkstra(self, times, N, K):
        """
        A dijkstra algorithm that runs in O(E+Vlog(V)) in time and O(E+V) in space

        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        pq, visited = [(0, K)], defaultdict(lambda: float('inf'))
        while pq:
            w, v = heapq.heappop(pq)
            if v not in visited:
                visited[v] = w
                for vv, ww in graph[v]:
                    if vv not in visited:
                        heapq.heappush(pq, (w + ww, vv))
        return max(visited.values()) if len(visited) == N else -1

    def networkDelayTime(self, times, N, K):
        """
        There are N network nodes, labelled 1 to N.

        Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

        Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.



        Example 1:



        Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
        Output: 2


        Note:

        N will be in the range [1, 100].
        K will be in the range [1, N].
        The length of times will be in the range [1, 6000].
        All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.

        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        return self.dijkstra(times, N, K)

    """
    DFS solution
    1. Loop through times
        1.1 Construct graph with u, v and w
    2. Initialize a stack with K
    3. Loop while stack isn't empty
        3.1 At any given node, do the depth first search
        3.2 Take the maximum depth out of all adjacent nodes
        3.3 Return the maximum depth starting from the node
    4. Return the maximum depth

    Dijkstra's algorithm
    1. Loop through times
        1.1 Construct graph with u, v and w
    2. Initialize a priority queue with K
    3. Loop while priority queue isn't empty
        3.1 Do the dijkstra's algorithm
        3.2 Remember which node has visited with the minimum step
    4. Return smallest values of the minimum values from the hash_map
    """