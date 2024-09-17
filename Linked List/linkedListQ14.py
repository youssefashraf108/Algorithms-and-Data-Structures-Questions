#Q14) Remove a given key from the linked list 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.header = None
        self.tail = None
        self.size = 0
        
    def removeKey(self,key):
        current = self.header
        prev = None
        while(current != None and current.data != key):
            prev = current
            current = current.next
        if current is None:
            return None
        prev = current.next
        return current.data