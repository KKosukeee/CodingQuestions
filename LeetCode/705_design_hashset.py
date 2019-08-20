"""
Solution for 705. Design HashSet
https://leetcode.com/problems/design-hashset/submissions/
"""
class ListNode:
    """
    ListNode object
    """
    def __init__(self, key, val=True):
        """
        Initialization method
        Args:
            key(int):
            val(bool):
        """
        self.key = key
        self.val = val
        self.next = None

class MyHashSet:
    """
    Runtime: 220 ms, faster than 60.87% of Python3 online submissions for Design HashSet.
    Memory Usage: 19 MB, less than 23.08% of Python3 online submissions for Design HashSet.
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 1000
        self.list = [None] * self.capacity

    def add(self, key):
        """
        Adds key to the set
        Args:
            key(int):

        Returns:

        """
        if not self.list[self.hash_fn(key)]:
            self.list[self.hash_fn(key)] = ListNode(key)
        else:
            node = self.list[self.hash_fn(key)]
            self.list[self.hash_fn(key)] = ListNode(key)
            self.list[self.hash_fn(key)].next = node

    def remove(self, key):
        """
        Removes a key from the set
        Args:
            key(int):

        Returns:

        """
        if not self.list[self.hash_fn(key)]:
            return
        node = self.list[self.hash_fn(key)]
        while node:
            if node.key == key:
                node.val = False
            node = node.next

    def contains(self, key):
        """
        Check if the value exists in the set or not
        Args:
            key(int):

        Returns:
            bool:
        """
        if not self.list[self.hash_fn(key)]:
            return False
        node = self.list[self.hash_fn(key)]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return False

    def hash_fn(self, key):
        """
        Generate index given hash key
        Args:
            key(int):

        Returns:
            int:
        """
        return key % self.capacity

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)