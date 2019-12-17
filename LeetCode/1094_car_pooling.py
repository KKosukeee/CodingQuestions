"""
Solution for 1094. Car Pooling
https://leetcode.com/problems/car-pooling/
"""
from collections import defaultdict
import heapq
from typing import List

class Solution:
  def initial_solution(self, trips: List[List[int]], capacity: int) -> bool:
    """
    An initial solution that runs in O(NlogN) in time and O(N) in space

    Args:
      trips:
      capacity:

    Returns:

    """
    pass_map = defaultdict(int)

    for num, start, end in trips:
      pass_map[start] += num
      pass_map[end] -= num

    passengers = 0
    for t in sorted(pass_map.keys()):
      passengers += pass_map[t]
      if passengers > capacity:
        return False
    return True

  def heap_solution(self, trips: List[List[int]], capacity: int) -> bool:
    """
    A heap solution that runs in O(NlogN) in time and O(N) in space

    Args:
      trips:
      capacity:

    Returns:

    """
    trips.sort(key=lambda x: x[1])
    pq = []

    for num, start, end in trips:
      while pq and start >= pq[0][0]:
        capacity += heapq.heappop(pq)[-1]
      heapq.heappush(pq, (end, start, num))
      capacity -= num
      if capacity < 0:
        return False
    return True

  def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    """
    You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

    Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

    Return true if and only if it is possible to pick up and drop off all passengers for all the given trips.



    Example 1:

    Input: trips = [[2,1,5],[3,3,7]], capacity = 4
    Output: false
    Example 2:

    Input: trips = [[2,1,5],[3,3,7]], capacity = 5
    Output: true
    Example 3:

    Input: trips = [[2,1,5],[3,5,7]], capacity = 3
    Output: true
    Example 4:

    Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
    Output: true



    Constraints:

    trips.length <= 1000
    trips[i].length == 3
    1 <= trips[i][0] <= 100
    0 <= trips[i][1] < trips[i][2] <= 1000
    1 <= capacity <= 100000

    Args:
      trips:
      capacity:

    Returns:

    """
    return self.heap_solution(trips, capacity)