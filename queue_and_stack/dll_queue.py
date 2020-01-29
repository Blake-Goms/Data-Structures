import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

'''
QUEUE: First In First Out
Imagine 10 people walk in line to order food
The 1st person orders, then leaves the line,
the 2nd person orders, then leaves the line, 
etc.
'''

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        #add value to the tail
        self.storage.add_to_tail(value)
        self.size += 1
        return self.size

    def dequeue(self):
        # remove from head
        if self.size < 1:
            return None
        self.size -= 1
        return self.storage.remove_from_head()
        
    def len(self):
        return self.size