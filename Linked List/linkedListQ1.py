class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.header = None
        self.tail = None
        self.size = 0

    def createLinkedList(self):
        n = Node(9)
        n1 = Node(8)
        n2 = Node(7)
        n3 = Node(6)

        n.next = n1 
        n1.next = n2
        n2.next = n3 
        n3.next = None
        self.header = n

    def printLinkedList(self):
        current = self.header
        while current is not None:
            print(current.data, end='->')
            current = current.next
        print("None")

# Create an instance of LinkedList and call the methods
ll = LinkedList()
ll.createLinkedList()
ll.printLinkedList()



