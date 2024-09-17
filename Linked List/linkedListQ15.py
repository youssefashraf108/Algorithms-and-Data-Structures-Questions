#Q15) How to detact loop in linked list 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.header = None
        self.tail = None
        self.size = 0

    def createLoop(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)

        self.header =node1 
        node1.next = node2
        node2.next = node3
        node3.next = node4 
        node4.next = node5
        node5.next = node6
        node6.next = node3
    
    def detectLoop(self):
        fastPtr = self.header
        slowPtr = self.header
        while(fastPtr != None and fastPtr.next != None ):
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next
            if(fastPtr == slowPtr):
                return True
        return False 
