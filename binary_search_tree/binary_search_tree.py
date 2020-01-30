import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else: 
                self.left.insert(value)
        # if < or = go to right child
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        # go left and check for None
        elif target < self.value and self.left is not None: 
                return self.left.contains(target)
        # target at this point is >= than self.value, so go right and check for None
        elif target > self.value and self.right is not None: 
                return self.right.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # if next value is none, you're at the end/max amount
        if self.right == None:
            #return the value you're at
            return self.value
        else:
            # self.get_max() also passes, but gives error
            return self.right.get_max()


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # this is the base case. it is your current node
        cb(self.value)
        # if left isn't None, you can keep going left. 
        if self.left != None:
            # this will push us to the next left node, and run it again until cant go left
            self.left.for_each(cb)
        # once the above finishes going left, this will start to go right
        if self.right != None:
            # this will push us to the next left right, and run it again until cant go right
            self.right.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is not None:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # make queue
        queue = Queue()
        # add node to queue, enqueue is push
        queue.enqueue(node)
        # while loop theres stuff in the queue
        while queue.size != 0:
            # save in temp
            temp = queue.dequeue()
            # DO THE THING!!!!
            print(temp.value)
            # if temp.left add to queue
            if temp.left is not None:
                queue.enqueue(temp.left)
            # if temp.right add to queue
            if temp.right is not None:
                queue.enqueue(temp.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # make a stack
        stack = Stack()
        # add root to stack
        stack.push(node)
        # while there is stuff in the stack
        while stack.size != 0:
            # pop root and save in temp
            temp = stack.pop()
            # DO THE THING!!!!
            print(temp.value)
            # if temp.left add to stack
            if temp.left is not None:
                stack.push(temp.left)
            # if temp.right add to stack
            if temp.right is not None:
                stack.push(temp.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
