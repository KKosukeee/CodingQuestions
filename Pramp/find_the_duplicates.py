"""
Solution for BST Successor Search
https://www.pramp.com/challenge/MW75pP53wAtzNPVLPG2b

Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases and analyze the
time & space complexities of your solutions: M ≈ N - the array lengths are approximately the
same M ≫ N - arr2 is much bigger than arr1.

Example:

input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]

output: [3, 6, 7] # since only these three values are both in arr1 and arr2
"""


#########################################################
# CODE INSTRUCTIONS:                                    #
# 1) The method findInOrderSuccessor you're asked      #
#    to implement is located at line 30.                #
# 2) Use the helper code below to implement it.         #
# 3) In a nutshell, the helper code allows you to       #
#    to build a Binary Search Tree.                     #
# 4) Jump to line 88 to see an example for how the      #
#    helper code is used to test findInOrderSuccessor.  #
#########################################################


# A node
class Node:
    """
    Node class for BSTs
    """
    # Constructor to create a new node
    def __init__(self, key):
        """
        Initialization method
        Args:
            key: value for the Node you are creating
        """
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


# A binary search tree
class BinarySearchTree:
    """
    BinarySearchTree class to look for successor node
    """

    # Constructor to create a new BST
    def __init__(self):
        """
        Initialization method
        """
        self.root = None

    """
    avg: O(logn)
    worst: O(n) when the tree is imbalance
    Time: O(n), Space: O(1)
    input node is 9 
    output should be 11
  
    basic case
    1. initialize current with input_node.right
    2. loop, while current is not None
    3. assign current with current.left
  
    edge case
    input node is 14
    output should be 20
    1. compare input_node.val with input_node.parent.val
    2. if parent is bigger then current is left child, return parent
    3. if parent is less than the current, then go assign current as current.parent 
    4. if current.parent > current then return the parent
    """
    # Time: O(n), Space: O(1)
    def find_in_order_successor(self, inputNode):
        """
        Main function to solve the question
        Args:
            inputNode: Node object to search successor node with

        Returns:
            Node: the successor node from inpuNode
        """
        # basic case
        if inputNode.right:
            current = inputNode.right
            while current:
                if not current.left:
                    return current
                current = current.left

        # edge case
        else:
            #  20
            # /  \
            # 9   25
            # inputNode = 9
            # current = 20
            current = inputNode.parent
            while current:
                if not current.parent:
                    return current

                if current.parent.key > current.key:
                    return current.parent

                current = current.parent

    # Given a binary search tree and a number, inserts a
    # new node with the given number in the correct place
    # in the tree. Returns the new root pointer which the
    # caller should then use(the standard trick to avoid
    # using reference parameters)
    def insert(self, key):
        """
        Insertion operation for BSTs
        Args:
            key: integer value for a Node object you are inserting

        Returns:

        """

        # 1) If tree is empty, create the root
        if (self.root is None):
            self.root = Node(key)
            return

        # 2) Otherwise, create a node with the key
        #    and traverse down the tree to find where to
        #    to insert the new node
        currentNode = self.root
        newNode = Node(key)
        while (currentNode is not None):

            if (key < currentNode.key):
                if (currentNode.left is None):
                    currentNode.left = newNode;
                    newNode.parent = currentNode;
                    break
                else:
                    currentNode = currentNode.left;
            else:
                if (currentNode.right is None):
                    currentNode.right = newNode;
                    newNode.parent = currentNode;
                    break
                else:
                    currentNode = currentNode.right;

    # Return a reference to a node in the BST by its key.
    # Use this method when you need a node to test your
    # findInOrderSuccessor function on
    def getNodeByKey(self, key):
        """
        Gets a Node object with integer key
        Args:
            key: integer value for search in the BST

        Returns:
            Node: if exists in the BST. None otherwise
        """

        currentNode = self.root
        while (currentNode is not None):
            if (key == currentNode.key):
                return currentNode

            if (key < currentNode.key):
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

        return None


#########################################
# Driver program to test above function #
#########################################

# Create a Binary Search Tree
bst = BinarySearchTree()
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11)
bst.insert(14)

# Get a reference to the node whose key is 9
test = bst.getNodeByKey(12)

# Find the in order successor of test
succ = bst.find_in_order_successor(test)

# Print the key of the successor node
if succ is not None:
    print("\nInorder Successor of %d is %d " \
          % (test.key, succ.key))
else:
    print("\nInorder Successor doesn't exist")
