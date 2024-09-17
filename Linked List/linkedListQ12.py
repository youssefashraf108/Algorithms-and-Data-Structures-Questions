#Q12) Find the nth node of the linked list 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.header = None
        self.tail = None
        self.size = 0
    def findNode(self,pos):
        current = self.header
        count = 0
        while(count != pos):
            current = current.next
            count += 1
        return current.data  