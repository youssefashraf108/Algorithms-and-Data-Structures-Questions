#2) Prepeding (Adding Node to the front of the list)
#3) Appedning (Adding Node to the end of the list)
#4) Remove the first Node
#5) Iterate through the list 
#6) Remove the last Node 
#7) Inserting node in a certain position
#8) Removing a node at certain position 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.header = None
        self.tail = None
        self.size = 0

#question 2
    def prepend(self,data):
        n = Node(data)
        if(self.size == 0):
            self.header = n
            self.tail = n
        else:
            n.next = self.header
            self.header = n
        self.size += 1

#question 3
    def append(self,data):
        n = Node(data)
        if(self.size == 0):
            self.header = n
            self.tail = n
        else: 
            temp = self.tail
            self.tail = n
            temp.next = n
        self.size += 1

#question 4
    def removeFirst(self):
        if(self.size== 0):
            return None
        data = self.header.data
        if(self.size == 1):
            self.header = None
            self.tail = None
        else:
            self.header = self.header.next 
        self.size -= 1
        return data

#Question 7 Itearate through the list 
    def display(self):
        current = self.header
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#Question 6 Remove Last Node 
    def removeLast(self):
        if(self.size == 0):
            return None
        data = self.tail.data
        if(self.size == 1):
            self.header = None
            self.tail = None
        else:
            current = self.header
            while(current.next.next != None):
                current = current.next
            self.tail = current 
            self.tail.next = None
        self.size -= 1
        return data
        
#Question 7 insert at certain position
def insertAt(self,data,pos):
    if(pos < 0 or pos > self.size):
        return 
    if(pos == 0):
        self.prepend(data)
    elif(pos == self.size):
        self.append(data)
    else:
        n = Node(data)
        prev = None
        current = self.header 
        counter = 0
        while(counter < pos):
            prev = current 
            current = current.next
            counter += 1
        prev.next = n
        n.next = current 
        self.size += 1 

#8) Removing a node at certain position 
def removeAt(self,pos):
    if(pos < 0 or pos >= self.size):
        return
    elif(pos == 0):
        return self.removeFirst()
    elif(pos == self.size-1):
        return self.removeLast()
    else:
        prev = None
        current = self.header 
        counter = 0
        while(counter < pos):
            prev = current 
            current = current.next
            counter += 1 
        prev.next = current.next
        self.size -= 1
        return current.data


# Create a linked list instance
ll = LinkedList()

# Prepend nodes to the linked list
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

ll.removeFirst()
ll.removeFirst()
# Display the linked list
ll.display()
