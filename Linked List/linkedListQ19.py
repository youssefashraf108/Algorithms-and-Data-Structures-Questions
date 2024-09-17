#Q19) Add two linked list 
class Node:
    def __init__(self,data):
        self.data = None
        self.next = None
class LinkedList:
    def __init__(self):
        self.header = None
        self.tail = None
    
    def addLinkedList(self,a,b):
        dummy = Node(0)
        tail = dummy
        carry = 0
        while(a != None or b != None):
            x = a.data if(a != None) else 0
            y = b.data if(b != None) else 0
            sum = x + y + carry
            carry = (sum//10)
            tail.next = Node(sum%10)
            if(a != None):
                a = a.next
            if(b != None):
                b = b.next
        if(carry > 0):
            tail.next = Node(carry)
        
        return dummy.next



