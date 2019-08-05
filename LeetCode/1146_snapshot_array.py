"""
Solution for 1146. Snapshot Array
https://leetcode.com/problems/snapshot-array/
"""
import bisect

class SnapshotArray:
    """
    Runtime: 560 ms, faster than 100.00% of Python3 online submissions for Snapshot Array.
    Memory Usage: 45 MB, less than 100.00% of Python3 online submissions for Snapshot Array.

    Implement a SnapshotArray that supports the following interface:

    SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
    void set(index, val) sets the element at the given index to be equal to val.
    int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
    int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id


    Example 1:

    Input: ["SnapshotArray","set","snap","set","get"]
    [[3],[0,5],[],[0,6],[0,0]]
    Output: [null,null,0,null,5]
    Explanation:
    SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
    snapshotArr.set(0,5);  // Set array[0] = 5
    snapshotArr.snap();  // Take a snapshot, return snap_id = 0
    snapshotArr.set(0,6);
    snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
    """
    # O(N)
    def __init__(self, length):
        """
        Initialization method
        Args:
            length: int
        """
        self.snap_history = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0

    # O(1)
    def set(self, index, val):
        """
        Sets a value at index
        Args:
            index: int
            val: int

        Returns:

        """
        self.snap_history[index].append([self.snap_id, val])

    # O(1)
    def snap(self):
        """
        Takes a snapshot
        Returns:
            int:
        """
        self.snap_id += 1
        return self.snap_id - 1

    # O(1)
    def get(self, index, snap_id):
        """
        Gets a value with snap_id
        Args:
            index: int
            snap_id: int

        Returns:
            int
        """
        i = bisect.bisect(self.snap_history[index], [snap_id + 1])
        return self.snap_history[index][i - 1][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)