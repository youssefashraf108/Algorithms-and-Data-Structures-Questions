#Q3) How to reverse an array usig stack
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
        self.stack[self.top] = 0
        self.top -= 1
        print(f"Removed {removed_data} from the stack")
        return removed_data
    
    def reverseArray(self,arr):
        for x in arr:
            self.push(x)
        for i in range(len(arr)):
            arr[i] = self.pop()
        return ''.join(arr)
    
def main():
    stack = Stack(7)
    print(stack.reverseArray(list("Youssef")))

if __name__ == "__main__":
    main()