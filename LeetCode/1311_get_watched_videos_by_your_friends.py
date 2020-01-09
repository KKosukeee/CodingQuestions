"""
Solution for 1311. Get Watched Videos by Your Friends
https://leetcode.com/problems/get-watched-videos-by-your-friends/
"""
from collections import Counter
from collections import deque
from typing import List

class Solution:
  """
  Runtime: 288 ms, faster than 97.11% of Python3 online submissions for Get Watched Videos by Your Friends.
  Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Get Watched Videos by Your Friends.
  """
  def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
    """
    There are n people, each person has a unique id between 0 and n-1. Given the arrays watchedVideos and friends, where watchedVideos[i] and friends[i] contain the list of watched videos and the list of friends respectively for the person with id = i.

    Level 1 of videos are all watched videos by your friends, level 2 of videos are all watched videos by the friends of your friends and so on. In general, the level k of videos are all watched videos by people with the shortest path equal to k with you. Given your id and the level of videos, return the list of videos ordered by their frequencies (increasing). For videos with the same frequency order them alphabetically from least to greatest.



    Example 1:



    Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
    Output: ["B","C"]
    Explanation:
    You have id = 0 (green color in the figure) and your friends are (yellow color in the figure):
    Person with id = 1 -> watchedVideos = ["C"]
    Person with id = 2 -> watchedVideos = ["B","C"]
    The frequencies of watchedVideos by your friends are:
    B -> 1
    C -> 2
    Example 2:



    Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2
    Output: ["D"]
    Explanation:
    You have id = 0 (green color in the figure) and the only friend of your friends is the person with id = 3 (yellow color in the figure).


    Constraints:

    n == watchedVideos.length == friends.length
    2 <= n <= 100
    1 <= watchedVideos[i].length <= 100
    1 <= watchedVideos[i][j].length <= 8
    0 <= friends[i].length < n
    0 <= friends[i][j] < n
    0 <= id < n
    1 <= level < n
    if friends[i] contains j, then friends[j] contains i

    Args:
      watchedVideos:
      friends:
      id:
      level:

    Returns:

    """
    return self.short_bfs(watchedVideos, friends, id, level)

  def bfs(self, watchedVideos: List[List[str]], friends: List[List[int]],
          id: int, level: int) -> List[str]:
    """
    A solution using a BFS that runs in O(N+Mlog(M)) where N = # of friends and
    M = # of videos in time and O(N+M) in space

    Args:
      watchedVideos:
      friends:
      id:
      level:

    Returns:

    """
    q, visited = deque([(id, level)]), set([id])
    videos = []
    while q:
      node, remain = q.popleft()
      if remain == 0:
        videos.extend(watchedVideos[node])
        continue
      for friend in friends[node]:
        if friend not in visited:
          q.append((friend, remain - 1))
          visited.add(friend)

    counter = Counter(videos)
    return sorted(counter.keys(), key=lambda x: (counter[x], x))

  def short_bfs(self, watchedVideos: List[List[str]], friends: List[List[int]],
                id: int, level: int) -> List[str]:
    """
    A solution using a BFS that runs in O(N+Mlog(M)) where N = # of friends and
    M = # of videos in time and O(N+M) in space

    Args:
      watchedVideos:
      friends:
      id:
      level:

    Returns:

    """
    visited, q = set([id]), deque([id])
    for _ in range(level):
      q = {j for i in q for j in friends[i] if j not in visited}
      visited |= q
    counter = Counter([video for i in q for video in watchedVideos[i]])
    return sorted(counter.keys(), key=lambda x: (counter[x], x))
