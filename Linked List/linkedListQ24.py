#Q24) How to create circular linked list  and
#Q25) How to traverse and print a cicular linked list and
#Q26) How to insert node at the beggining of a circular linked list 
#Q26) How to add node at the begginning of circular linked list
#Q27) How to add node at the end of the circular linked list 
#Q28) How to remove first Node from a cicular linked list 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.last = None

    def printList(last):
        if last is None:
            print("List is Empty")
            return
        head = last.next
        while True:
            print(head.data, end=" ")
            head = head.next
            if head == last.next:
                break
    print()
    def prepend(self, data):
        new_node = Node(data)

        if self.last is None:  # Case when the list is empty
            self.last = new_node
            new_node.next = new_node  # Circular reference to itself
        else:
            # Insert the new node at the beginning
            new_node.next = self.last.next  # New node points to the current head
            self.last.next = new_node  # Last node now points to the new node

        # Return the last node to maintain the reference
        return self.last
    
    def append(self, data):
        new_node = Node(data)
        if self.last is None:  # Case when the list is empty
            self.last = new_node
            new_node.next = new_node  # Circular reference to itself
        else:
            new_node.next = self.last.next  # New node points to the head (first node)
            self.last.next = new_node  # Old last node points to the new node
            self.last = new_node  # Update last to the new node
    
    def removeFirst(self):
        if self.last is None:
            return
        removed_node = self.last.next
        if self.last.next == self.last:
            self.last = None
        else:
            self.last.next = self.last.next.next 
        return removed_node
