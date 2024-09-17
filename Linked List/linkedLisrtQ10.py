""" Q1) create a linked list 
10 -> 1 -> 8 -> 11 
Q2) Prepeding (Adding Node to the front of the list) 
Q3) Appending (Adding Node to the end of the list) 
Q4) Printing our linked list
Q5) Remove the first node 
Q6) Remove the last node 
Q7) Inserting node in a certain position 
Q8) Removing node at certain position 
Q9) How to find the length of the linked list 
Q10) How to search an element in linked list  """

#Prepending and printing linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def prepend(self,data):
        new_node = Node(data)
        if(self.size == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
    
    #Q3) Appending (Adding Node to the end of the list)
    def append(self,data):
        new_node = Node(data)
        if(self.size == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        
    def printList(self):
        temp = self.head 
        while(temp != None):
            print(temp.data,end='->')
            temp = temp.next
        print("None")
    
    #Q5) Remove the first node 
    #Q6) Remove the last node
    def removeFirst(self):
        if(self.size == 0):
            return None
        removed_node = self.head
        if(self.size == 1):
            self.head = None
            self.tail = None
        else: 
            self.head = self.head.next
        self.size -= 1
        return removed_node
    
    def removeLast(self):
        if(self.size == 0):
            return None
        removed_node = self.tail
        if(self.size == 1):
            self.head = None
            self.tail = None
        else:
            current = self.head
            while(current.next != self.tail):
                current = current.next
            self.tail = current
            self.tail.next = None
        self.size -= 1
        return removed_node
    
    #inserting node at position
    def insertNodeAt(self,data,pos):
        if(pos < 0 or pos > self.size):
            return None
        if(pos == 0):
            self.prepend(data)
        elif(pos == self.size):
            self.append(data)
        else:
            new_node = Node(data)
            counter = 0
            prev = None
            current = self.head 
            while(counter != pos):
                prev = current
                current = current.next
                counter += 1
            prev.next = new_node
            new_node.next = current
            self.size += 1
    
    #removing node at certain position
    def removeAt(self,pos):
        if(pos < 0 or pos >= self.size):
            return None
        elif(pos == 0):
            return self.removeFirst()
        elif(pos == self.size-1):
            return self.removeLast()
        else:
            counter = 0
            current = self.head
            prev = None
            while(counter != pos):
                prev = current
                current = current.next
                counter += 1
            prev.next = current.next  
            self.size -= 1
            return current
    #Q9) How to find the length of the linked list 
    def findLen(self):
        current = self.head
        counter = 0
        while(current != None):
            current = current.next
            counter += 1
        return counter   
    #Q10) How to search an element in a linked list 
    def searchElement(self,key):
        current = self.head
        counter = 0
        while(current != None):
            if(current.data == key):
                return True
            current = current.next 
        return False 
def main():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.insertNodeAt(15,0)
    ll.printList()
    print(ll.findLen())
    found = ll.searchElement(15)
    if(found):
        print(f"Element has been found: {found}")



if __name__ =='__main__':
    main()