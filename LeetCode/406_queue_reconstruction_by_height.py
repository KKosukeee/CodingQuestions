"""
Solution for 406. Queue Reconstruction by Height
https://leetcode.com/problems/queue-reconstruction-by-height/
"""

class Solution:
    """
    Runtime: 84 ms, faster than 84.03% of Python3 online submissions for Queue Reconstruction by
        Height.
    Memory Usage: 13.6 MB, less than 5.71% of Python3 online submissions for Queue Reconstruction
        by Height.
    """
    def reconstructQueue(self, people):
        """
        Suppose you have a random list of people standing in a queue. Each person is described by
        a pair of integers (h, k), where h is the height of the person and k is the number of
        people in front of this person who have a height greater than or equal to h. Write an
        algorithm to reconstruct the queue.

        Note:
        The number of people is less than 1,100.


        Example

        Input:
        [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

        Output:
        [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
        Args:
            people: list of list of integers where the array[0] is the height, and array[1] is the
                people he sees in front of him

        Returns:
            list<list<int>>: where queue is properly sorted
        """
        # sort in descending order
        people.sort(key=lambda x: (-x[0], x[1]))

        # create result array
        result = []

        # fix the position for the heighest person one by one
        for person in people:
            result.insert(person[1], person)

        return result
