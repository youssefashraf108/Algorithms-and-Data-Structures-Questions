#Q6) Create Queue data structure 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.isEmpty():
            # When queue is empty, both front and rear should point to the new node
            self.front = new_node
            self.rear = new_node
        else:
            # Link the current rear to the new node and update the rear pointer
            self.rear.next = new_node
            self.rear = new_node

    def deque(self):
        if self.isEmpty():
            return None
        else:
            # Remove the front element and return its data
            data = self.front.data
            self.front = self.front.next
            # If the front becomes None, set rear to None as well
            if self.front is None:
                self.rear = None
            return data
            


# Test the Queue
ll = Queue()
ll.enqueue(10)
ll.enqueue(20)
ll.enqueue(30)

print(ll.deque())  # Output: 10
print(ll.deque())  # Output: 20
print(ll.deque())  # Output: 30
print(ll.deque())  # Output: None (queue is empty)
