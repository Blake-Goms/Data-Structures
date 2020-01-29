import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

'''
STACK: Last In First Out
Imagine stacking a plate of dishes. 
The first dish goes on the bottom,
the 2nd on top, etc.
The last dish gets taken off first, 
the first dish gets taken off last
'''

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)
        return self.size

    def pop(self):
        if self.size < 1:
            return None
        self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
        return self.size
