class Stack:
    def __init__(self, size):
        self.stack = [None] * size  # Pre-allocate space for the stack
        self.size = size
        self.top = -1

    def push(self, data):
        if self.top == self.size - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.stack[self.top] = data
        print(f"Pushed {data} onto the stack")
    
    def pop(self):
        if self.top == -1:
            print("Empty Stack")
            return None
        removed_data = self.stack[self.top]
        self.stack[self.top] = None  # Use None to represent empty
        self.top -= 1
        print(f"Removed {removed_data} from the stack")
        return removed_data
    
    def is_empty(self):
        return self.top == -1
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[self.top]
    
    def nextGreaterElement(self, arr):
        result = [0] * len(arr)
        
        # Traverse the array from right to left
        for i in range(len(arr) - 1, -1, -1):
            # Pop elements that are smaller than or equal to arr[i]
            while not self.is_empty() and self.peek() <= arr[i]:
                self.pop()
            
            # If stack is empty, no greater element
            if self.is_empty():
                result[i] = -1
            else:
                # The top of the stack is the next greater element
                result[i] = self.peek()
            
            # Push current element onto the stack
            self.push(arr[i])
        
        return result

def main():
    arr = [4, 7, 3, 4, 8, -1]
    stack = Stack(len(arr))
    print("Next Greater Element for each element:")
    print(stack.nextGreaterElement(arr))

if __name__ == '__main__':
    main()
