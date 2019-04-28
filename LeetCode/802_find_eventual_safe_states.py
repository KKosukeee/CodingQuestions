"""
Solution for 802. Find Eventual Safe States
https://leetcode.com/problems/find-eventual-safe-states/
"""
from collections import deque

class Solution:
    """
    Runtime: 336 ms, faster than 25.50% of Python3 online submissions for Find Eventual
        Safe States.
    Memory Usage: 24.3 MB, less than 6.52% of Python3 online submissions for Find Eventual
        Safe States.
    """
    def eventualSafeNodes(self, graph):
        """
        In a directed graph, we start at some node and every turn, walk along a directed edge of
        the graph.  If we reach a node that is terminal (that is, it has no outgoing directed
        edges), we stop.

        Now, say our starting node is eventually safe if and only if we must eventually walk to a
        terminal node.  More specifically, there exists a natural number K so that for any choice
        of where to walk, we must have stopped at a terminal node in less than K steps.

        Which nodes are eventually safe?  Return them as an array in sorted order.

        The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.
        The graph is given in the following form: graph[i] is a list of labels j such that (i, j)
        is a directed edge of the graph.

        Example:
        Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
        Output: [2,4,5,6]
        Here is a diagram of the above graph.
        Args:
            graph:

        Returns:

        """
        # Initialize boolean list initially set as False
        N = len(graph)
        safe = [False] * N

        # Create a incoming and outgoing lists
        graph = list(map(set, graph))
        rgraph = [set() for _ in range(N)]

        # Initialize a queue to store safe nodes
        q = deque()

        # Create incoming list
        for i, js in enumerate(graph):
            # If there is no outgoing edge, this means it's a safe node
            if not js:
                q.append(i)
            for j in js:
                rgraph[j].add(i)

        # Loop while there is a safe node left in the queue
        while q:
            j = q.popleft()
            safe[j] = True

            # Look for all vertices which has edges to the safe node
            for i in rgraph[j]:
                graph[i].remove(j)

                # If there is only one edge which is going to the safe node, this mean it's a safe
                if len(graph[i]) == 0:
                    q.append(i)

        # Now simply return the indices for each safe node
        return [i for i, v in enumerate(safe) if v]
