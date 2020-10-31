# Queue: A queue.
# Your implementation should pass the tests in test_queue.py.
# Baleria Reyes

# Hint: pip3 install llist
from llist import sllist

class Queue:

    def __init__(self):
        self.data = sllist()

    def enqueue(self, item):
        self.data.append(item)   

    def dequeue(self):
        return self.data.popleft()

    def is_empty(self):
        return len(self.data) == 0

