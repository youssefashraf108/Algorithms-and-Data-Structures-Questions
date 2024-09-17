#Q13) How to remove duplicates form sorted linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.header = None
        self.tail = None
        self.size = 0
    def insertSorted(self,data):
        n = Node(data)
        current = self.header
        prev = None
        while(current != None and current.data < data):
            prev = current
            current = current.next
        n.next = current
        prev.next = n 