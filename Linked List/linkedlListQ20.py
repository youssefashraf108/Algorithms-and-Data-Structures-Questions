#Q20) Implement doubly linked list 
#Q21) prepend doubly linked list  
#Q22) How to insert node at the end at doubly linked list
#Q23) How to delete first node in a doubly linked list 
#Q24 How to delete last node from a doubly linked list 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class linkedList:
    def __init__(self):
        self.header = None
        self.tail = None
        self.size = 0
    def prepend(self,data):
        new_node = Node(data)
        if self.size == 0:
            self.header = new_node
            self.tail = new_node
        else:
            self.header.prev = new_node
            new_node.next = self.header
            self.header = new_node
        self.size += 1 
    #Q22) How to insert node at the end at doubly linked list
    def insertEnd(self,data):
        new_node = Node(data)
        if self.size == 0:
            self.header = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
    #Q23) How to delete first node in a doubly linked list
    def removeBeginning(self):
        if self.size == 0:
            return None

        removed_node = self.header

        if self.size == 1:
            self.header = None
            self.tail = None
        else:
            self.header = self.header.next
            self.header.prev = None

        # Detach the removed node
        removed_node.next = None

        # Decrement the size
        self.size -= 1

        return removed_node
    
    #Q24 How to delete last node from a doubly linked list 
    def removeLast(self):
        if self.size == 0:
            return None
        removed_node = self.tail

        if self.size == 1:
            self.header = None
            self.tail = None
        else:
            self.tail = self.tail.prev 
            self.tail.next = None
        removed_node.prev = None
        self.size -= 1
        return removed_node
