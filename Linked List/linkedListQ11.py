#Q11) How to reverse a singly linked list 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.header = None
        self.tail = None
        self.size = 0
    def reverseList(self):
        current = self.header
        previous = None
        next = None
        while(current != None):
            next = current.next
            current.next = previous
            previous = current 
            current = next 
        self.header = previous 
        