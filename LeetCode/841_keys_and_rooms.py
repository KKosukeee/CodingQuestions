"""
Solution for 841. Keys and Rooms
https://leetcode.com/problems/keys-and-rooms/
"""
class Solution:
    """
    Runtime: 48 ms, faster than 35.36% of Python3 online submissions for Keys and Rooms.
    Memory Usage: 13.4 MB, less than 14.52% of Python3 online submissions for Keys and Rooms.
    """
    def canVisitAllRooms(self, rooms):
        """
        There are N rooms and you start in room 0.  Each room has a distinct number in
        0, 1, 2, ..., N-1, and each room may have some keys to access the next room.

        Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer
        in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with
        number v.

        Initially, all the rooms start locked (except for room 0).

        You can walk back and forth between rooms freely.

        Return true if and only if you can enter every room.

        Example 1:

        Input: [[1],[2],[3],[]]
        Output: true
        Explanation:
        We start in room 0, and pick up key 1.
        We then go to room 1, and pick up key 2.
        We then go to room 2, and pick up key 3.
        We then go to room 3.  Since we were able to go to every room, we return true.
        Example 2:

        Input: [[1,3],[3,0,1],[2],[0]]
        Output: false
        Explanation: We can't enter the room with number 2.
        Args:
            rooms: 2D arrays containing keys as integers

        Returns:
            bool: if you can visit all rooms or not
        """
        # initialize keys with key for room 0
        keys = [0]

        # initialize visited
        visited = set()

        # loop WHILE len(keys) > 0
        while keys:
            # pop an element from keys
            key = keys.pop()

            # check if room is visited
            if key not in visited: # O(1)
                # if not visited, add keys in the rooms
                keys.extend(rooms[key])

                # append the room in visited array
                visited.add(key)

            # check if all rooms are visited
            if len(visited) == len(rooms):
                # if so, return True
                return True

            # otherwise keep looping.

        # return False
        return False
