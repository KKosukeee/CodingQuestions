"""
Solution for 380. Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/
"""
import random
class RandomizedSet:
    """
    RandomizedSet class
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        Args:
            val(int):
        Returns:
            bool:
        """
        if val in self.dict:
            return False
        self.list.append(val)
        self.dict[val] = len(self.list)-1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        Args:
            val(int):
        Returns:
            bool:
        """
        if val not in self.dict:
            return False
        i, j = self.dict[val], self.dict[self.list[-1]]
        self.dict[self.list[-1]] = self.dict[val]
        self.list[i], self.list[j] = self.list[j], self.list[i]
        del self.dict[self.list.pop()]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        Returns:
            int:
        """
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()