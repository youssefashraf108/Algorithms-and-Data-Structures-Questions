#Q29) How to create a stack using linked list  
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        print(f"Pushed {data} onto the stack")  # Corrected reference

    def pop(self):
        if self.top is None:
            return "Stack is Empty"
        removed_node = self.top.data
        self.top = self.top.next
        self.size -= 1
        print(f"Removed {removed_node} from the stack")
        return removed_node

    def peek(self):
        """Return the top element without removing it."""
        if self.top is None:
            print("Stack is empty.")
            return None
        return self.top.data

def main():
    stack = Stack()
    stack.push(10)
    stack.push(11)
    stack.push(12)
    print(f"Top element is {stack.peek()}")
    stack.pop()
    stack.pop()
    stack.pop()
    print(f"Top element after pops is {stack.peek()}")

if __name__ == '__main__':  # Corrected the name check
    main()
