#Q18) Merge two sorted linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.header = None
        self.tail = None
        self.size = 0
    
    def merge(self,a,b):
        dummy = Node(0)
        tail = dummy
        while(a != None and b != None):
            if(a.data <= b.data):
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next  
        if(a == None):
            tail.next = b
        else:
            tail.next = a 